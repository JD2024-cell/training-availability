🚀 QUICK START: Deploy Your Availability App with Email Security
=================================================================

## What You're Getting

✅ Secure web app for collecting team availability
✅ Password protected
✅ Email-based access control (only your team)
✅ Free hosting on Streamlit Cloud
✅ No coding required to deploy

## Your Next Steps (30 minutes)

### STEP 1: Choose Your Password (2 min)

Open: `.streamlit/secrets.toml`
Change: `ACCESS_PASSWORD = "training2026"`
To: `ACCESS_PASSWORD = "YourSecurePassword123"`

Save the file.

---

### STEP 2: Upload to GitHub (10 min)

**Don't have Git installed? No problem!**

**Easiest Method - GitHub Web Upload:**

1. Go to: https://github.com/new
2. Create repository named: `training-availability`
3. **Choose:** ⭐ **Private** (recommended) or Public
4. Click "uploading an existing file"
5. Select ALL files from `C:\CTP\Python\availability\` EXCEPT:
   - ❌ `venv` folder
   - ❌ `availability_responses.csv` (if exists)
   - ❌ `__pycache__` folder (if exists)
   - ❌ `.streamlit/secrets.toml` (contains your password!)
6. **DO upload:** `.streamlit/config.toml` (this is safe - just app colors)
7. Commit files
7. Commit files
8. ✅ Done!

**Privacy Note:** 
- **Private repo** = Only you see the code
- **Public repo** = Anyone can see code on GitHub (but they still can't access your app without the password!)
- Streamlit Cloud works with both - your choice!
- **Never upload secrets.toml** - you'll add the password in Streamlit Cloud's dashboard instead (Step 3)

**OR Use GitHub Desktop (if you prefer a tool):**

1. Download: https://desktop.github.com/
2. File → New Repository → Point to this folder
3. Publish to GitHub
4. ✅ Done!

---

### STEP 3: Deploy to Streamlit Cloud (10 min)

1. **Go to:** https://share.streamlit.io
2. **Sign in** with your GitHub account
3. **Click:** "New app"
4. **Select:**
   - Repository: `training-availability`
   - Branch: `main`
   - Main file: `availability_submission_app.py`
5. **Click:** "Advanced settings" ⚙️
6. **In Secrets box, paste:**
   ```
   ACCESS_PASSWORD = "YourPasswordFromStep1"
   ```
7. **Click:** "Deploy!" 🚀
8. **Wait 2-3 minutes** ⏱️
9. **Copy your app URL** 📋 (looks like: `https://training-availability-xxxxx.streamlit.app`)

---

### STEP 4: Security Options (OPTIONAL) 🔒

**Choose your security level:**

**Option A: Password Only (Simplest - Recommended for small teams)**
- ✅ Just share the password with your team
- ✅ No Google sign-in required
- ✅ Works immediately
- ⚠️ Anyone with the password can access
- **Perfect for 5-50 trusted team members**

**Skip to Step 5!** You're already protected by password.

---

**Option B: Add Email Restrictions (Extra secure)**

Only if you want Google authentication:

1. In Streamlit Cloud, click **⋮** (three dots) on your app
2. Go to **Settings → Sharing**
3. Enable **"Restrict viewing access"**
4. Add allowed email domain: `@yourcompany.com`
5. Save ✅

Now people need both Google sign-in AND the password.

---

### STEP 5: Test It (3 min) ✅

1. **Open app URL** in incognito/private window
2. **Enter password** you set in Step 1
3. **Submit test availability**
4. **Check CSV** downloads in sidebar

**If password wrong** → check Secrets in Streamlit dashboard matches

---

### STEP 6: Share with Team 📧

**Copy this email template:**

---

**Subject:** Training Availability - Please Submit by [DATE]

Hi Team,

Please submit your availability for upcoming training sessions:

**🔗 Link:** [YOUR APP URL HERE]

**📝 Steps:**
1. Click the link
2. Enter password: `[YOUR PASSWORD HERE]`
3. Fill in your name and select availability
4. Click Submit

**📅 Training Dates:**
- Week 1: Wed 8 Jul, Thu 9 Jul, Fri 10 Jul
- Week 2: Wed 15 Jul, Thu 16 Jul, Fri 17 Jul
- Week 3: Wed 22 Jul, Thu 23 Jul, Fri 24 Jul

**⏰ Please respond by:** [YOUR DEADLINE]

Questions? Reply to this email.

Thanks!

---

✅ **DONE!** You're live!

---

## What Happens Next?

1. **Team submits** their availability through the app
2. **You download** the CSV regularly from the app sidebar
3. **When collection is done**, use `training_availability_planner.py` to analyze:
   ```bash
   .\venv\Scripts\python.exe -m streamlit run training_availability_planner.py
   ```
4. **Upload the CSV** to the planner to see ranked sessions
5. **Make your decision** on best training dates!

---

## Need Help?

📖 **Detailed Instructions:** [DEPLOY_NOW.md](DEPLOY_NOW.md)
🔒 **Security Info:** [SECURITY.md](SECURITY.md)
✅ **Step-by-step Checklist:** [CHECKLIST.md](CHECKLIST.md)

---

## Security Summary

**What's Visible to Public?**

| What | Visible? | Notes |
|------|----------|-------|
| GitHub Code | Your choice | Make repo **Private** to hide code |
| App URL | Yes (if someone finds it) | Like `https://training-availability-xxxxx.streamlit.app` |
| App Content | ❌ **NO** | Protected by password |
| Responses/Data | ❌ **NO** | Protected by password |
| People's Names | ❌ **NO** | Protected by password |

**Bottom Line:** Random public can't see anything useful without your password! 🔒

**If someone finds your app URL (e.g., via Google):**
- They see a password entry screen
- Without the password → They see nothing
- Can't submit, can't see responses, can't see names

---

**With Password-Only (Default):**
- ✅ Password protection
- ✅ Simple - no sign-in needed
- ✅ All traffic encrypted (HTTPS)
- ✅ FREE!
- ⚠️ Anyone with password can access
- **Good for: Trusted teams of 5-50 people**

**If You Add Email Restrictions (Optional):**
- ✅ All the above PLUS
- ✅ Email verification via Google sign-in
- ✅ Only approved emails can access
- **Good for: External partners or large organizations**

**Either way, you're protected from random public access!** 🛡️

---

**Ready? Start with Step 1 above!** ⬆️
