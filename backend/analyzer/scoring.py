# analyzer/scoring.py

def calculate_score(total_repos, readme_ratio, stars, language_count):
    score = 0

    # Repo count
    if total_repos >= 5:
        score += 20
    elif total_repos >= 3:
        score += 10

    # Documentation
    if readme_ratio > 0.7:
        score += 25
    elif readme_ratio > 0.4:
        score += 15

    # Stars
    if stars > 10:
        score += 15
    elif stars > 3:
        score += 10

    # Language diversity
    if language_count >= 3:
        score += 20
    elif language_count >= 2:
        score += 10

    return min(score, 100)


def generate_suggestions(total_repos, readme_ratio, stars):
    suggestions = []

    if readme_ratio < 0.5:
        suggestions.append("Add detailed README files to your repositories.")

    if total_repos < 5:
        suggestions.append("Build and publish more meaningful projects.")

    if stars < 5:
        suggestions.append("Improve project visibility and share your work.")

    if not suggestions:
        suggestions.append("Your GitHub profile looks strong. Keep building!")

    return suggestions
