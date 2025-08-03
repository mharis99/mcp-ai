# MCP AI Agent on Vercel

This is a fullstack AI project with:
- 🧠 FastAPI backend using vector memory and mock LLM
- 💻 Remix frontend for user interaction
- 🚀 Ready to deploy on [Vercel](https://vercel.com)

## 🚀 Getting Started Locally

### Backend (API)
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend (Remix)
```bash
cd frontend
npm install
npm run dev
```

Access app at http://localhost:3000

## ✅ Deployment on Vercel

- Set root as the `frontend/` folder
- Vercel will auto-detect the Remix app
- Move `api/` into `api/` at project root (already done)
- Add environment variables or build settings as needed
