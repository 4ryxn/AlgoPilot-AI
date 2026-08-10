# AlgoPilot-AI

Complete starter project: React + Vite frontend, FastAPI backend, SQLAlchemy, PostgreSQL/Docker, JWT auth, LeetCode integration, GitHub sync, dashboard, analytics, AI starter, planner, pricing, OAuth scaffolds and CI.

## Run

### Backend
```powershell
cd backend
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
py -m uvicorn app.main:app --reload --port 8000
```

Swagger: http://127.0.0.1:8000/docs

### Frontend
Open another terminal:
```powershell
cd frontend
npm install
copy .env.example .env
npm run dev
```

Frontend: http://localhost:5173

### Docker
From project root:
```powershell
docker compose up --build
```

## Important LinkedIn note

A LinkedIn username/URL cannot legitimately expose a person's complete private LinkedIn data. Real LinkedIn profile access requires OAuth and approved permissions. This project stores the LinkedIn URL and includes an OAuth scaffold; it does not scrape LinkedIn.

## Roadmap
1-6 setup: included
7-9 login/register/JWT: included
10-11 Google/GitHub OAuth: scaffold
12-16 LeetCode profile/stats/calendar/contest/rating: profile + stats + calendar included; contest/rating are ready for extension
17-20 dashboard/statistics/heatmap/charts/topics: included starter
21-24 AI coach/review/hint/interviewer: included starter
25-27 daily/revision/company planner: included starter
28 GitHub sync: included
29 PDF report: endpoint placeholder
30-32 deployment/Docker/CI: included
33 README: included
34 screenshots: take after running the UI

## Troubleshooting

If port 8000 is already used:
```powershell
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

If login says invalid email/password, register the account first.

If CORS appears, use `http://localhost:5173` for the frontend. The backend already allows both localhost and 127.0.0.1.
