# 🚀 Blood Health Advisor — Deployment & Configuration Guide

## Project Structure

```
blood_project/
├── frontend/
│   ├── config.js          ← API configuration (LOCAL vs PRODUCTION)
│   ├── app.js             ← Main application logic
│   ├── index.html         ← HTML structure
│   └── styles.css         ← Styling
├── backend/
│   ├── main.py            ← FastAPI backend server
│   ├── train.py           ← Model training
│   ├── evaluate.py        ← Model evaluation
│   ├── predict.py         ← Prediction logic
│   └── requirements.txt    ← Python dependencies
└── vercel.json            ← Vercel deployment configuration
```

---

## 🔧 Configuration System

### Frontend URL Management (`frontend/config.js`)

The application has a **dual-environment configuration system** for seamless switching between development and production:

#### **For Local Development:**
1. Open `frontend/config.js`
2. Change the active environment:
   ```javascript
   const ACTIVE_ENV = ENVIRONMENT.LOCAL;
   ```
3. This will use: `http://127.0.0.1:8022`
4. Start your local backend server and test

#### **For Production/Vercel Deployment:**
1. Open `frontend/config.js`
2. Change the active environment:
   ```javascript
   const ACTIVE_ENV = ENVIRONMENT.PRODUCTION;
   ```
3. This will use: `https://server.uemcseaiml.org:8022/blood`
4. Commit and push to GitHub (Vercel will auto-deploy)

---

## 📋 Workflow

### Step 1: Local Development & Testing
```bash
# Terminal 1: Start backend server
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8022

# Terminal 2: Test frontend locally
# In frontend/config.js, set:
const ACTIVE_ENV = ENVIRONMENT.LOCAL;
# Open index.html in browser or use Live Server
```

### Step 2: Before Push to GitHub (Production)
```bash
# Update frontend/config.js:
const ACTIVE_ENV = ENVIRONMENT.PRODUCTION;

# Commit changes
git add .
git commit -m "Switch to production backend URL"
git push origin main
```

### Step 3: Vercel Auto-Deployment
- Vercel automatically deploys when you push to GitHub
- Frontend accesses backend at: `https://server.uemcseaiml.org:8022/blood`

---

## 🌐 Deployment Details

### Frontend
- **Platform**: Vercel
- **Configuration**: `vercel.json`
- **Environment**: Production backend URL (`https://server.uemcseaiml.org:8022/blood`)
- **Auto-Deploy**: Triggered on GitHub push

### Backend
- **Platform**: UEM Custom Server
- **URL**: `https://server.uemcseaiml.org:8022/blood`
- **Port**: 8022
- **API Endpoints**: All prefixed with `/api/` or direct routes (`/predict`, `/health`)

### CORS Configuration
The backend (`main.py`) is configured to accept requests from:
- All origins (`allow_origins=["*"]`)
- All methods and headers
- This allows the Vercel frontend to communicate freely

---

## 🔄 Environment Switching Rules

| Task | Config Setting | Base URL |
|------|---|---|
| Local Backend Testing | `ENVIRONMENT.LOCAL` | `http://127.0.0.1:8022` |
| Vercel Production | `ENVIRONMENT.PRODUCTION` | `https://server.uemcseaiml.org:8022/blood` |
| Backend Dev Server Port | (in main.py) | `8022` |

---

## 🚨 Important Notes

1. **Always toggle `config.js` before push**: Ensure production URL is set before committing
2. **Local testing**: You need a running local backend server on port 8022
3. **CORS**: Backend allows all origins, so any frontend can access it (adjust if needed)
4. **Model Files**: Ensure `vgg16_best.keras` is in `backend/` or `backend/models/`
5. **Environment Variables**: Set in `.env` file if needed (see `backend/main.py`)

---

## 📱 Testing the Application

### Local Test
1. Start backend: `python -m uvicorn backend/main:app --host 127.0.0.1 --port 8022`
2. Set `config.js` to `ENVIRONMENT.LOCAL`
3. Open frontend in browser: `http://localhost:[frontend-port]`

### Production Test
1. Verify backend is running at: `https://server.uemcseaiml.org:8022/blood`
2. Set `config.js` to `ENVIRONMENT.PRODUCTION`
3. Access Vercel frontend URL

---

## 💾 Files Modified

- ✅ `frontend/config.js` — Created (new configuration system)
- ✅ `frontend/app.js` — Updated (removed hardcoded URLs)
- ✅ `frontend/index.html` — Updated (added config.js script)
- ✅ `DEPLOYMENT.md` — Created (this file)

---

## 🆘 Troubleshooting

**Q: Frontend says backend not found**
- Check `config.js` - ensure correct environment is selected
- For local: verify backend is running on `http://127.0.0.1:8022`
- For production: verify server is up at `https://server.uemcseaiml.org:8022/blood`

**Q: CORS errors in browser console**
- Backend CORS already allows all origins
- Check network tab to see which URL is being called
- Verify BASE_URL in browser console: `console.log(BASE_URL)`

**Q: Changes not reflecting on Vercel**
- Ensure you pushed to GitHub
- Check Vercel dashboard for build status
- Verify `config.js` has production URL before push

---

## 🎯 Next Steps

1. Test locally with `ENVIRONMENT.LOCAL`
2. Switch to `ENVIRONMENT.PRODUCTION` before pushing
3. Monitor Vercel deployment
4. Verify backend connectivity from Vercel frontend

---

**Last Updated**: March 31, 2026
