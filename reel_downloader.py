import os
import yt_dlp
import time
import random

SAVE_DIR = "instagram_reels"
os.makedirs(SAVE_DIR, exist_ok=True)

def download_reels(reel_codes):
    if not reel_codes:
        print("[INFO] No reels to download.")
        return

    for code in reel_codes:
        url = f"https://www.instagram.com/reel/{code}/"
        print(f"[⬇️] Downloading: {url}")

        try:
            ydl_opts = {
                'outtmpl': os.path.join(SAVE_DIR, '%(title)s.%(ext)s'),
                'quiet': True,
                'noplaylist': True,
                'format': 'mp4/best',
                'user_agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'merge_output_format': 'mp4'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            print(f"[✅] Downloaded reel {code}")

        except Exception as e:
            print(f"[ERROR] Failed to download {code}: {e}")

        # Random delay between downloads (3 to 8 seconds)
        sleep_time = random.uniform(3.0, 8.0)
        print(f"[⏳] Sleeping {sleep_time:.2f} seconds before next download...")
        time.sleep(sleep_time)
