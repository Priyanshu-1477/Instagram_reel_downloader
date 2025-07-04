# main.py
import os
import time
import random
from dotenv import load_dotenv
from insta_handler import login_instagram
from dm_listener import extract_reel_code_from_messages
from reel_downloader import download_reels

# Load credentials
load_dotenv()
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

# Login
client = login_instagram(IG_USERNAME, IG_PASSWORD)
if not client:
    exit("[❌] Instagram login failed. Exiting...")

# Get threads
threads = client.direct_threads()
print(f"[INFO] Checking {len(threads)} DM threads for reel links...")

# Extract all reel codes
all_new_reels = []

for thread in threads:
    if thread.users:
        print(f"[DEBUG] Checking messages in thread with user: {thread.users[0].username}")
    else:
        print("[DEBUG] No users found in this thread.")

    # Random delay before fetching messages
    time.sleep(random.uniform(3.0, 7.5))

    try:
        messages = client.direct_messages(thread.id)

        # Random delay after messages are fetched
        time.sleep(random.uniform(2.5, 6.0))

        new_reels = extract_reel_code_from_messages(messages)
        all_new_reels.extend(new_reels)

    except Exception as e:
        print(f"[ERROR] Failed to process thread {thread.id}: {e}")
        continue

    # Random delay before moving to the next thread
    time.sleep(random.uniform(5.0, 10.0))

# Download all new reels
download_reels(all_new_reels)
print("✅ Done checking all messages.")
