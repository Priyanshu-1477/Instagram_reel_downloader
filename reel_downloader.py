import os
import yt_dlp

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
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"[✅] Downloaded reel {code}")
        except Exception as e:
            print(f"[ERROR] Failed to download {code}: {e}")
