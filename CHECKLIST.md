# Deployment Checklist

## Pre-Deployment ✅

- [ ] Reviewed security settings ([SECURITY.md](SECURITY.md))
- [ ] Changed password from default `training2026`
- [ ] Updated training sessions in app (currently: Wed/Thu/Fri for 3 weeks)
- [ ] Tested app locally works correctly
- [ ] Have GitHub account ready
- [ ] Know which email addresses/domain to allow

---

## GitHub Setup 📦

**Choose ONE method:**

- [ ] **Method A:** Downloaded & installed GitHub Desktop
  - [ ] Created repository in GitHub Desktop
  - [ ] Published to GitHub

OR

- [ ] **Method B:** Used GitHub Web Interface
  - [ ] Created new repository on github.com
  - [ ] Uploaded files (excluding venv, .csv, __pycache__)

OR

- [ ] **Method C:** Used Git Command Line
  - [ ] Ran `git init` and pushed to GitHub

---

## Streamlit Cloud Deployment 🚀

- [ ] Went to https://share.streamlit.io
- [ ] Signed in with GitHub
- [ ] Clicked "New app"
- [ ] Selected correct repository
- [ ] Set main file: `availability_submission_app.py`
- [ ] Clicked "Advanced settings"
- [ ] Added password to Secrets section:
  ```
  ACCESS_PASSWORD = "your_password_here"
  ```
- [ ] Clicked "Deploy!"
- [ ] Waited for deployment to complete (2-3 min)
- [ ] Got app URL: `https://_________________.streamlit.app`

---

## Email Restrictions (CRITICAL!) 🔒

- [ ] Went to app settings (three dots menu)
- [ ] Clicked "Settings" → "Sharing" tab
- [ ] Enabled "Restrict viewing access"
- [ ] Added allowed email addresses OR domain
  - Option 1: Individual emails (john@company.com, jane@company.com)
  - Option 2: Entire domain (@yourcompany.com)
- [ ] Saved settings

---

## Testing ✅

- [ ] Opened app URL in incognito window
- [ ] Tested Google sign-in with allowed email - **SUCCESS ✓**
- [ ] Tested password entry - **SUCCESS ✓**
- [ ] Submitted test availability - **SUCCESS ✓**
- [ ] Downloaded CSV from sidebar - **SUCCESS ✓**
- [ ] (Optional) Tested with non-allowed email - **BLOCKED ✓**

---

## Share with Team 📧

- [ ] Prepared team email with:
  - [ ] App URL
  - [ ] Access password
  - [ ] Instructions
  - [ ] Deadline to respond
- [ ] Sent email to team
- [ ] Confirmed team can access

---

## Ongoing Management 📊

- [ ] Set calendar reminder to download CSV weekly (for backup)
- [ ] Documented who has access password
- [ ] Planned deadline for submissions
- [ ] Prepared to analyze results with planner app

---

## Post-Collection 📈

- [ ] All responses collected
- [ ] Downloaded final CSV from app sidebar
- [ ] Opened `training_availability_planner.py` to analyze
- [ ] Uploaded CSV to planner
- [ ] Reviewed ranked sessions
- [ ] Made training schedule decision
- [ ] Communicated final dates to team

---

## Optional Enhancements 🎨

If you want to improve the app further:

- [ ] Add custom domain (Streamlit paid plan)
- [ ] Integrate database for persistent storage
- [ ] Add email notifications on submission
- [ ] Export to Google Sheets automatically
- [ ] Add data visualization dashboard
- [ ] Set up automated backups

---

## Resources 📚

- [DEPLOY_NOW.md](DEPLOY_NOW.md) - Detailed deployment guide
- [SECURITY.md](SECURITY.md) - Security considerations
- [DEPLOYMENT.md](DEPLOYMENT.md) - Alternative deployment options
- [README.md](README.md) - Project overview

---

**Current Status:** ⬜ Not Started

Update this as you progress! 🎯
