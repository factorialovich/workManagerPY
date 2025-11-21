# 🔮 Universal Bot & Site Manager

A multifunctional TUI (terminal UI) panel for managing:

- Telegram bots (Python / Node.js)
- Sites served by **Nginx** or **Apache2**

All from a single, soft-colored console dashboard.

---

## ✨ Features

- 🔎 **Automatic bot discovery**  
  Recursively scans all folders starting from the directory where `manager.py` lives.
- 🐍 **Python bots support**  
  Detects `index.py`, `main.py`, `bot.py`, `app.py` (configurable).
- 🟢 **Node.js bots support**  
  Detects `package.json` + `index.js`, `main.js`, `bot.js`, `app.js`.
- 🧪 **Virtualenv detection**  
  Uses `venv`, `.venv`, or `env` Python virtual environments automatically.
- 🌐 **Nginx & Apache2 site management**
  - Reads configs from:
    - `/etc/nginx/sites-available/`
    - `/etc/apache2/sites-available/`
  - Shows whether a site is enabled/disabled (symlink in `sites-enabled`)
  - Can enable / disable configs and reload web server.
- 📊 **Real process status via `psutil`**
  - Detects bots by working directory of running processes.
- 📜 **Logging & rotation**
  - Writes logs to `bot_folder/logs/botname.log`
  - On restart, rotates old logs with timestamp.
- 🎨 **Beautiful soft 24-bit color theme**
  - Pastel purple / beige / cyan tones.
  - Graceful fallback for terminals without truecolor.
- 🧭 **Termius / iTerm2 / Kitty / XTerm friendly**
- 🧷 **Alias auto-setup**
  - On first run, can add an alias (e.g. `panel`) to `~/.bashrc`.

---

## 📂 Project structure

Minimal typical layout:

```text
your-server/
├── manager.py           # this script
├── some-python-bot/
│   ├── venv/            # optional
│   ├── main.py
│   └── ...
└── some-node-bot/
    ├── package.json
    ├── index.js
    └── ...