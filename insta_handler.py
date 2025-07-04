# insta_handler.py
import json
import os
from instagrapi import Client

SESSION_FILE = "session.json"

def login_instagram(username, password):
    cl = Client()

    # Load session settings if available
    if os.path.exists(SESSION_FILE):
        print("[INFO] Loading existing Instagram session ...")
        try:
            with open(SESSION_FILE, "r") as f:
                session = json.load(f)
            cl.set_settings(session)
        except Exception as e:
            print(f"[WARN] Failed to load session settings: {e}")
    
    # Try to login
    try:
        cl.login(username, password)
        print("[SUCCESS] Logged in successfully!")
        with open(SESSION_FILE, "w") as f:
            json.dump(cl.get_settings(), f)
        return cl
    except Exception as e:
        print(f"[ERROR] Login failed: {e}")
        return None
