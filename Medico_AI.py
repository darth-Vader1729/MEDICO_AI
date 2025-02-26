import streamlit as st
import sqlite3
import bcrypt
import time
from PIL import Image

def create_users_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON;")
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def add_user(username, password):
    hashed_password = hash_password(password)
    try:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    if user and check_password(password, user[0]):
        return True
    return False

def main():
    st.set_page_config(layout="wide")
    st.title("Diagnostic Assistant")
    create_users_table()
    
    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "past_conversations" not in st.session_state:
        st.session_state.past_conversations = []
    if "show_file_uploader" not in st.session_state:
        st.session_state.show_file_uploader = False
    
    st.sidebar.subheader("Past Conversations")
    for i, conv in enumerate(st.session_state.past_conversations):
        st.sidebar.button(conv, key=f"conv_{i}")
    
    if st.session_state.authenticated:
        st.success("Logged in successfully!")
        st.session_state.past_conversations.append("New Conversation")
        with st.spinner("Redirecting..."):
            time.sleep(2)
        
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()
        
        st.subheader("Diagnostic Assistant")
        st.write("This AI-powered assistant can analyze medical images, patient data, and symptoms to assist healthcare professionals in diagnosing diseases accurately and efficiently.")
        
        # Mimic ChatGPT's input row with a paperclip icon button
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            if st.button("📎", key="paperclip"):
                st.session_state.show_file_uploader = True
        with col2:
            user_input = st.text_area("Enter patient symptoms:", placeholder="Describe symptoms here...")
        
        # Show file uploader if the paperclip icon was clicked
        if st.session_state.show_file_uploader:
            uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Analyze"):
            st.write("Mock analysis: Based on the symptoms, the AI suggests further testing for a more accurate diagnosis.")
    else:
        if choice == "Sign Up":
            st.subheader("Create New Account")
            new_user = st.text_input("Username")
            new_password = st.text_input("Password", type="password")
            if st.button("Sign Up"):
                if add_user(new_user, new_password):
                    st.success("Account created successfully! You can now log in.")
                else:
                    st.error("Username already exists! Try a different one.")
        elif choice == "Login":
            st.subheader("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if authenticate_user(username, password):
                    st.session_state.authenticated = True
                    st.success("Logged in successfully! Redirecting...")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Invalid username or password")

if __name__ == "__main__":
    main()
