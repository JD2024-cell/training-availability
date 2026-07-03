# Deployment Guide

## Option 1: Streamlit Community Cloud (Recommended - FREE)

**Best for:** Quick deployment, free hosting, easy to use

### Steps:

1. **Prepare your repository:**
   ```bash
   # Initialize git if you haven't already
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub:**
   - Create a new repository on [GitHub](https://github.com/new)
   - Push your code:
     ```bash
     git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
     git branch -M main
     git push -u origin main
     ```

3. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Set main file path: `availability_submission_app.py`
   - Click "Deploy"

4. **Share the URL:** You'll get a URL like `https://your-app-name.streamlit.app`

### Notes:
- ✅ Free forever
- ✅ Automatic HTTPS
- ✅ Restarts automatically when you push to GitHub
- ✅ No credit card required
- ⚠️ Apps sleep after inactivity (wake up on first visit)
- ⚠️ Limited resources (sufficient for small-medium teams)

---

## Option 2: Azure App Service

**Best for:** Corporate environments with Azure subscriptions

### Quick Deploy:

```bash
# Install Azure CLI
# Then:
az login
az webapp up --name your-availability-app --runtime "PYTHON:3.11" --sku B1
```

### Cost: ~$13/month for basic tier

---

## Option 3: Render (Easy Alternative)

**Best for:** Simple deployment with automatic SSL

### Steps:
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. New Web Service → Connect repository
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `streamlit run availability_submission_app.py --server.port=$PORT --server.address=0.0.0.0`

### Cost: Free tier available (limited), paid starts at $7/month

---

## Option 4: Railway

**Best for:** Developer-friendly deployment

### Steps:
1. Go to [railway.app](https://railway.app)
2. New Project → Deploy from GitHub
3. Select your repository
4. Railway auto-detects Python and deploys

### Cost: $5/month starter plan

---

## Option 5: Heroku

**Best for:** Traditional PaaS hosting

### Steps:

1. **Create Procfile:**
   ```
   web: streamlit run availability_submission_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create runtime.txt:**
   ```
   python-3.11.9
   ```

3. **Deploy:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### Cost: ~$7-25/month (no free tier anymore)

---

## Data Persistence Note

⚠️ **Important:** Most cloud platforms have ephemeral file systems. Your CSV file will be lost on restart.

### Solutions:

1. **For Streamlit Cloud:** Use Streamlit's session state + download functionality (current setup works fine)

2. **For production:** Consider using a database:
   - PostgreSQL (free tier on most platforms)
   - MongoDB Atlas (free tier)
   - Google Sheets API (simple integration)

3. **Quick database setup example:**
   ```python
   # Use environment variables for DB connection
   import os
   DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://...")
   ```

---

## Security Considerations

### For public deployment:

1. **Add password protection** (optional):
   ```python
   import streamlit as st
   
   if "authenticated" not in st.session_state:
       password = st.text_input("Enter password:", type="password")
       if password == "YOUR_SECRET_PASSWORD":
           st.session_state.authenticated = True
           st.rerun()
       else:
           st.stop()
   ```

2. **Use Streamlit secrets** for sensitive data:
   - Create `.streamlit/secrets.toml` locally
   - Add secrets in Streamlit Cloud dashboard
   - Access via: `st.secrets["PASSWORD"]`

3. **Limit access by email** (Streamlit Cloud feature available)

---

## Recommended Approach for Your Use Case

Given firewall restrictions and need for team access:

**→ Use Streamlit Community Cloud**
- Free
- No infrastructure management
- Accessible from anywhere
- Easy to update
- Built for Streamlit apps

**Next best:** Railway or Render (if you need more control)
