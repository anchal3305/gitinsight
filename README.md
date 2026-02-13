# GitInsight – GitHub Portfolio Analyzer & Enhancer

## 🚀 Overview
GitInsight is a full-stack web application that analyzes GitHub profiles from a recruiter’s perspective. It generates a structured portfolio score and provides actionable insights to help developers improve their GitHub presence.

## 🎯 Problem Statement
Students often struggle to understand how recruiters evaluate GitHub profiles. Incomplete documentation, poor repository structure, and inconsistent activity reduce hiring visibility.

GitInsight bridges this gap by objectively analyzing public repositories and highlighting improvement areas.

## 🛠 Tech Stack
- Frontend: React (Vite)
- Backend: Django + Django REST Framework
- API: GitHub REST API
- Authentication: GitHub Personal Access Token
- Styling: CSS

## ✨ Features
- GitHub Profile Analysis
- Structured Portfolio Score (0–100)
- Repository & Language Analysis
- README Detection
- Recruiter-Focused Suggestions
- Rate Limit Handling
- Secure Token Management via .env

## 📊 Scoring Dimensions
- Documentation Quality
- Repository Structure
- Language Diversity
- Activity Signals
- Project Visibility

## 🔐 Setup Instructions

### Backend Setup

cd backend

pip install -r requirements.txt

create .env file:

GITHUB_TOKEN=your_token_here

python manage.py runserver

### Frontend Setup

cd GitInsight

npm install

npm run dev

## Screenshots
<img width="1429" height="1066" alt="Screenshot 2026-02-13 210738" src="https://github.com/user-attachments/assets/5b90e85a-818f-4a11-8654-82772c8673c5" />

<img width="1397" height="1069" alt="Screenshot 2026-02-13 210752" src="https://github.com/user-attachments/assets/41731ca6-4b7f-4bd5-8785-ac828267f3c0" />

## 🎥 Demo Video
(Add your screen recording link here)

## 📌 Future Improvements
- Commit frequency analysis
- AI-based README evaluation
- Contribution heatmap analysis
- Portfolio improvement roadmap
