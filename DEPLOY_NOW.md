# Quick Deployment to Streamlit Cloud with Email Restrictions

## Step-by-Step Guide

### Step 1: Prepare Your Files ✅

Your files are ready! You have:
- ✅ `availability_submission_app.py` - Main app
- ✅ `requirements.txt` - Dependencies
- ✅ `.streamlit/config.toml` - Configuration
- ✅ `.gitignore` - Git ignore rules

---

### Step 2: Push to GitHub

**Option A: Using GitHub Desktop (Recommended if no git installed)**

1. **Download GitHub Desktop:**
   - Go to: https://desktop.github.com/
   - Install and sign in with your GitHub account

2. **Create Repository:**
   - File → New Repository
   - Name: `training-availability`
   - Local Path: `C:\CTP\Python\availability`
   - Click "Create Repository"

3. **Publish to GitHub:**
   - Click "Publish repository"
   - Uncheck "Keep this code private" OR keep it private (both work)
   - Click "Publish Repository"

**Option B: Using Web Interface (No tools needed)**

1. **Go to GitHub.com** and sign in
2. **Create new repository:**
   - Click "+" → "New repository"
   - Name: `training-availability`
   - Choose Public or Private
   - DON'T initialize with README
   - Click "Create repository"

3. **Upload files manually:**
   - Click "uploading an existing file"
   - Drag all files from `C:\CTP\Python\availability` 
   - EXCEPT: `venv` folder, `availability_responses.csv`, `__pycache__`
   - Commit files

**Option C: Using Git Command Line (If installed)**

```bash
cd C:\CTP\Python\availability
git init
git add .
git commit -m "Initial commit - availability app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/training-availability.git
git push -u origin main
```

---

### Step 3: Deploy to Streamlit Cloud 🚀

1. **Go to Streamlit Cloud:**
   - Visit: https://share.streamlit.io
   - Sign in with GitHub (if not already signed in)

2. **Create New App:**
   - Click "New app" button
   - Select your repository: `training-availability`
   - Branch: `main` (or `master`)
   - Main file path: `availability_submission_app.py`

3. **Configure Secrets (Important!):**
   - Before deploying, click "Advanced settings"
   - In "Secrets" section, paste:
   ```toml
   ACCESS_PASSWORD = "YourSecurePassword123"
   ```
   - Replace with your actual password
   - Click "Save"

4. **Deploy:**
   - Click "Deploy!"
   - Wait 2-3 minutes for deployment
   - Your app URL will be: `https://training-availability-xxxxx.streamlit.app`

---

### Step 4: Enable Email Restrictions (CRITICAL for Security!) 🔒

This is the most important step for security!

1. **In Streamlit Cloud Dashboard:**
   - Go to your app's settings (three dots menu)
   - Click "Settings"

2. **Configure Sharing:**
   - Go to "Sharing" tab
   - Enable "Restrict viewing access"
   
3. **Add Allowed Users:**
   
   **Option 1 - Specific Emails:**
   ```
   john.smith@company.com
   jane.doe@company.com
   bob.wilson@company.com
   ```
   
   **Option 2 - Entire Domain (Better!):**
   ```
   @yourcompany.com
   ```
   This allows anyone with `@yourcompany.com` email to access

4. **Save Settings**

Now only people with allowed email addresses can access the app after signing in with Google!

---

### Step 5: Test Your Deployment ✅

1. **Open your app URL** (e.g., `https://training-availability-xxxxx.streamlit.app`)

2. **You should see:**
   - Google sign-in prompt (if email restrictions enabled)
   - After sign-in: Password entry screen
   - After password: Availability form

3. **Test the flow:**
   - Sign in with allowed email
   - Enter password
   - Submit test availability
   - Check if response is saved
   - Download CSV from sidebar

4. **Test with non-allowed email** (if email restrictions enabled):
   - Should see "Access denied" message
   - This confirms security is working!

---

### Step 6: Share with Your Team 📧

**Email template:**

```
Subject: Training Availability - Please Submit Your Response

Hi Team,

Please submit your availability for the upcoming training sessions:

🔗 App URL: https://training-availability-xxxxx.streamlit.app

📝 Instructions:
1. Sign in with your company Google account (@yourcompany.com)
2. Enter the access password: [PASSWORD HERE]
3. Fill in your name and availability
4. Click Submit

The training sessions are:
- Week 1: Wed 8 Jul, Thu 9 Jul, Fri 10 Jul
- Week 2: Wed 15 Jul, Thu 16 Jul, Fri 17 Jul
- Week 3: Wed 22 Jul, Thu 23 Jul, Fri 24 Jul

Please respond by [DEADLINE].

Thanks!
```

---

## Security Summary 🛡️

With this setup, you have:

✅ **Email Restrictions** - Only approved emails can access
✅ **Google Sign-In** - Proper authentication
✅ **Password Protection** - Additional layer of security
✅ **Secrets Management** - Password stored securely in Streamlit Cloud
✅ **HTTPS** - All traffic encrypted
✅ **No Public Access** - General public cannot see or submit

**This is enterprise-grade security for a Streamlit app!**

---

## Managing Users

**To add/remove users later:**

1. Go to Streamlit Cloud dashboard
2. Select your app → Settings → Sharing
3. Add or remove email addresses
4. Changes take effect immediately

**To change password:**

1. Go to Streamlit Cloud dashboard
2. Select your app → Settings → Secrets
3. Update `ACCESS_PASSWORD = "new_password"`
4. Save (app will restart automatically)
5. Notify team of new password

---

## Troubleshooting

**Problem: "App is taking too long to load"**
- Solution: Wait 1-2 minutes for first startup after deploy
- Apps sleep after inactivity, take ~30 seconds to wake up

**Problem: "Access denied" for team member**
- Check their email is in allowed list
- Check they're signing in with correct Google account
- Case-sensitive for emails

**Problem: "Incorrect password"**
- Verify password in Secrets matches what you shared
- Check for typos/spaces
- Password is case-sensitive

**Problem: "Lost data after app restart"**
- CSV files are ephemeral on Streamlit Cloud
- Download CSV regularly from sidebar
- Consider database for production (see DEPLOYMENT.md)

**Problem: Git not installed**
- Use GitHub Desktop or web upload (see Step 2)
- No command line needed!

---

## Next Steps (Optional)

After deployment, you might want to:

1. **Custom Domain** (Streamlit Cloud paid plans)
2. **Database Integration** for persistent storage
3. **Email Notifications** when someone submits
4. **Export to Google Sheets** automatically
5. **Analytics Dashboard** for organizers

Let me know if you want help with any of these!

---

## Cost

**Streamlit Cloud:**
- ✅ Free tier includes:
  - 1 private app
  - 3 public apps
  - Email restrictions
  - Secrets management
  - HTTPS
- No credit card required!

---

## Support

If you need help:
1. Check troubleshooting section above
2. Review [SECURITY.md](SECURITY.md) for security details
3. Review [DEPLOYMENT.md](DEPLOYMENT.md) for alternative platforms
4. Streamlit docs: https://docs.streamlit.io

---

**Ready to deploy? Follow the steps above!** 🚀
