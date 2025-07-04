import json
import os

HISTORY_FILE = "reel_history.json"

def load_seen_reel_codes():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return set(json.load(f))
        except json.JSONDecodeError:
            print("[WARN] ⚠️ Corrupted history file. Starting fresh.")
            return set()
    else:
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)
        return set()

def save_reel_codes(reel_codes, existing_codes):
    new_codes = set(reel_codes) - existing_codes
    all_codes = list(existing_codes.union(new_codes))

    with open(HISTORY_FILE, "w") as f:
        json.dump(all_codes, f, indent=2)

    if new_codes:
        print(f"[✅] Saved {len(new_codes)} new reel(s) to history.")
    else:
        print("[ℹ️] No new reels. History updated anyway.")

def extract_reel_code_from_messages(messages):
    reel_codes = []

    for message in messages:
        try:
            clip = getattr(message, "clip", None)
            if clip and hasattr(clip, "code"):
                reel_code = clip.code
                print(f"[DEBUG] 🎥 Extracted from clip: {reel_code}")
                reel_codes.append(reel_code)
                continue

            text = getattr(message, "text", None)
            if text and "instagram.com/reel/" in text:
                reel_code = text.split("instagram.com/reel/")[1].split("/")[0]
                print(f"[DEBUG] 📝 Extracted from text: {reel_code}")
                reel_codes.append(reel_code)
        except Exception as e:
            print(f"[ERROR] Failed to extract reel code: {e}")
            continue

    if not reel_codes:
        print("[WARN] ❌ No reel code could be extracted.")
        return []

    existing_codes = load_seen_reel_codes()
    unique_new_reels = list(set(reel_codes) - existing_codes)

    if unique_new_reels:
        print(f"[✅] Found {len(unique_new_reels)} new reel(s).")
    else:
        print("[INFO] No new reels found.")

    save_reel_codes(reel_codes, existing_codes)

    return unique_new_reels
