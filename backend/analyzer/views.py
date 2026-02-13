import os
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scoring import calculate_score, generate_suggestions

# Load token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Common headers for GitHub API
HEADERS = {
    "Accept": "application/vnd.github+json"
}

if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"


@api_view(['POST'])
def analyze_profile(request):
    profile_url = request.data.get("url")

    if not profile_url:
        return Response({"error": "No URL provided"}, status=400)

    # Extract username safely
    username = profile_url.rstrip('/').split('/')[-1]

    # GitHub API endpoints
    user_api = f"https://api.github.com/users/{username}"
    repos_api = f"https://api.github.com/users/{username}/repos"

    # Fetch user
    user_response = requests.get(user_api, headers=HEADERS)

    # Rate limit check
    if user_response.status_code == 403:
        return Response(
            {"error": "GitHub API rate limit exceeded. Try again later."},
            status=403
        )

    if user_response.status_code != 200:
        return Response({"error": "GitHub user not found"}, status=404)

    # Fetch repositories
    repos_response = requests.get(repos_api, headers=HEADERS)

    if repos_response.status_code != 200:
        return Response({"error": "Could not fetch repositories"}, status=400)

    repos = repos_response.json()

    if not isinstance(repos, list):
        return Response({"error": "Unexpected GitHub response"}, status=400)

    total_repos = len(repos)
    total_stars = 0
    readme_count = 0
    languages = set()

    for repo in repos:
        total_stars += repo.get("stargazers_count", 0)

        if repo.get("language"):
            languages.add(repo["language"])

        # Check README existence
        readme_api = f"https://api.github.com/repos/{username}/{repo['name']}/readme"
        readme_response = requests.get(readme_api, headers=HEADERS)

        if readme_response.status_code == 200:
            readme_count += 1

    readme_ratio = readme_count / total_repos if total_repos > 0 else 0

    # Calculate score
    score = calculate_score(
        total_repos,
        readme_ratio,
        total_stars,
        len(languages)
    )

    suggestions = generate_suggestions(
        total_repos,
        readme_ratio,
        total_stars
    )

    return Response({
        "score": score,
        "total_repos": total_repos,
        "stars": total_stars,
        "languages": list(languages),
        "suggestions": suggestions
    })
