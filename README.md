# 🎬 Instagram Reel Downloader & Organizer

A powerful Python automation tool that **listens to your Instagram DMs**, extracts shared **Reels**, and **saves them automatically** to a local folder (`instagram_reels/`).  
This project was built with simplicity and automation in mind — no manual downloading or forwarding needed.

---

## 📌 Features

- ✅ **Auto login** using stored session or `.env` credentials  
- 🎯 **DM monitoring** for Instagram Reels sent by specific friends  
- 🔍 **Smart extraction** from multiple reel formats (`clip`, `media_share`, `reel_share`, etc.)  
- 📁 **Local storage** of Reels inside `instagram_reels/`  
- 📜 **History tracking** using `reel_history.json` to avoid re-downloading  
- 🔄 **Fully automated** using `systemd timers` every 30 minutes (or adjustable)  

---

## 🚀 How It Works

1. You share a **reel in Instagram DM** from a selected friend.
2. Every 30 minutes, the app:
   - Logs into Instagram using `instagrapi`
   - Checks latest messages in DMs
   - Extracts any new Reel links
   - Downloads them using `yt-dlp`
   - Saves them neatly to the `instagram_reels/` folder
   - Stores the reel code in `reel_history.json` to prevent duplicates

---

## 📁 Project Structure

```
insta2wa/
├── instagram_reels/        # 💾 Folder where all reels are saved
├── .gitignore              # 📄 Ensures sensitive/data files aren't pushed
├── cron.log                # 📓 Logs from systemd/cron (optional)
├── dm_listener.py          # 🧠 Extracts reel codes from DMs
├── insta_handler.py        # 🔐 Handles Instagram login/session
├── main.py                 # 🎬 Main runner script
├── reel_downloader.py      # ⬇️ Downloads reels using yt-dlp
├── reel_history.json       # 🧠 Stores previously downloaded reel codes
└── .env                    # 🔐 Stores IG_USERNAME and IG_PASSWORD
```

---

## ⚙️ Requirements

- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- `instagrapi`, `python-dotenv`

Install dependencies:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
instagrapi
python-dotenv
yt-dlp
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory with your credentials:

```env
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
```

---

## 🛠️ Automation Using systemd Timer (Recommended for Linux)

To run the script every 30 minutes, create the following files:

### 📄 `~/.config/systemd/user/insta2wa.service`

```ini
[Unit]
Description=Run Insta2WA Reel Downloader

[Service]
Type=simple
WorkingDirectory=/home/YOUR_USERNAME/insta2wa
ExecStart=/usr/bin/python3 /home/YOUR_USERNAME/insta2wa/main.py
StandardOutput=append:/home/YOUR_USERNAME/insta2wa/cron.log
StandardError=append:/home/YOUR_USERNAME/insta2wa/cron.log
```

### ⏱️ `~/.config/systemd/user/insta2wa.timer`

```ini
[Unit]
Description=Run Insta2WA every 30 minutes

[Timer]
OnBootSec=2min
OnUnitActiveSec=30min
Persistent=true

[Install]
WantedBy=timers.target
```

Replace `YOUR_USERNAME` with your actual Linux username and adjust paths accordingly.

Enable and start the timer:

```bash
systemctl --user daemon-reexec
systemctl --user enable insta2wa.timer
systemctl --user start insta2wa.timer
systemctl --user status insta2wa.timer
```

> ✅ Make sure you enable **user lingering** if you want the timer to run even when you're logged out:

```bash
sudo loginctl enable-linger YOUR_USERNAME
```

---

## 🧠 Notes

- The script remembers downloaded reels using `reel_history.json` so you never get duplicates.
- All videos are saved in the `instagram_reels/` folder in the same directory.
- Credentials and sessions are handled securely with `.env` and session caching.

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Author

Made with ❤️ by [Priyanshu Raj](https://github.com/Priyanshu-1477)
