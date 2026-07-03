import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Training Availability Submission", layout="wide")

# Configuration
DATA_FILE = "availability_responses.csv"
AVAILABILITY_OPTIONS = ["Available", "Tentative", "Prefer not", "Unavailable"]

# Password configuration - use secrets in production
try:
    ACCESS_PASSWORD = st.secrets["ACCESS_PASSWORD"]
except:
    ACCESS_PASSWORD = "training2026"  # Fallback for local testing

# Define your training sessions here - Next 3 weeks: Wed/Thu/Fri
TRAINING_SESSIONS = [
    "Wed 8 Jul",
    "Thu 9 Jul",
    "Fri 10 Jul",
    "Wed 15 Jul",
    "Thu 16 Jul",
    "Fri 17 Jul",
    "Wed 22 Jul",
    "Thu 23 Jul",
    "Fri 24 Jul",
]

# Password protection
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 Training Availability Submission")
    st.write("Please enter the access password to continue.")
    
    password = st.text_input("Password", type="password", key="password_input")
    
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Login", type="primary"):
            if password == ACCESS_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Incorrect password. Please try again.")
    
    st.divider()
    st.info("💡 Contact your training coordinator for the access password.")
    st.stop()

st.title("📅 Training Availability Submission")
st.write("Please let us know your availability for the upcoming training sessions.")

# Initialize session state
if "submitted" not in st.session_state:
    st.session_state.submitted = False

def load_existing_data():
    """Load existing responses if file exists."""
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return None

def save_response(name: str, responses: dict):
    """Save or update a person's availability response."""
    existing_df = load_existing_data()
    
    # Create new row
    new_row = {"Name": name, "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    new_row.update(responses)
    
    if existing_df is not None:
        # Check if person already submitted
        if name in existing_df["Name"].values:
            # Update existing entry
            idx = existing_df[existing_df["Name"] == name].index[0]
            for col, value in new_row.items():
                existing_df.at[idx, col] = value
        else:
            # Append new entry
            existing_df = pd.concat([existing_df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        # Create new dataframe
        existing_df = pd.DataFrame([new_row])
    
    existing_df.to_csv(DATA_FILE, index=False)

# Main form
if not st.session_state.submitted:
    with st.form("availability_form"):
        st.subheader("Your Details")
        name = st.text_input("Your Name *", placeholder="Enter your full name")
        
        st.subheader("Your Availability")
        st.write("For each session, please indicate your availability:")
        
        responses = {}
        cols = st.columns(2)
        
        for idx, session in enumerate(TRAINING_SESSIONS):
            with cols[idx % 2]:
                responses[session] = st.radio(
                    f"**{session}**",
                    options=AVAILABILITY_OPTIONS,
                    key=f"session_{idx}",
                    horizontal=False
                )
        
        st.divider()
        
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            submitted = st.form_submit_button("Submit Availability", type="primary", use_container_width=True)
        with col2:
            clear = st.form_submit_button("Clear Form", use_container_width=True)
        
        if submitted:
            if not name or not name.strip():
                st.error("Please enter your name before submitting.")
            else:
                try:
                    save_response(name.strip(), responses)
                    st.session_state.submitted = True
                    st.rerun()
                except Exception as e:
                    st.error(f"Error saving your response: {e}")
        
        if clear:
            st.rerun()

else:
    # Success message
    st.success("✅ Thank you! Your availability has been submitted successfully.")
    st.balloons()
    
    if st.button("Submit Another Response"):
        st.session_state.submitted = False
        st.rerun()
    
    st.divider()
    
    # Show summary of responses
    st.subheader("Current Responses")
    existing_df = load_existing_data()
    if existing_df is not None:
        st.metric("Total Responses", len(existing_df))
        
        with st.expander("View all responses"):
            display_df = existing_df.drop(columns=["Timestamp"], errors="ignore")
            st.dataframe(display_df, use_container_width=True, hide_index=True)

# Sidebar information
with st.sidebar:
    st.header("ℹ️ Information")
    st.write("**Availability Options:**")
    st.write("- **Available**: You can definitely attend")
    st.write("- **Tentative**: You might be able to attend")
    st.write("- **Prefer not**: You prefer not to attend this session")
    st.write("- **Unavailable**: You cannot attend")
    
    st.divider()
    
    existing_df = load_existing_data()
    if existing_df is not None:
        st.metric("Total Submissions", len(existing_df))
        st.caption(f"Data stored in: {DATA_FILE}")
        
        # Admin download option
        if st.checkbox("Show admin options"):
            st.download_button(
                "Download responses (CSV)",
                data=existing_df.to_csv(index=False),
                file_name=f"availability_responses_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
            )
