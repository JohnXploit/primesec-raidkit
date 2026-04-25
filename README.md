
<div align="center">
  <h1>PRIMESEC // RAIDKIT</h1>
  <p><strong>Advanced User-Installable Discord Raid Bot • Silent Payload Delivery System 2026</strong></p>

  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Discord.py-2.4+-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="discord.py"/>
  <img src="https://img.shields.io/badge/STATUS-ARMED-red?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/THREAT%20LEVEL-CRITICAL-8B0000?style=for-the-badge" alt="Threat Level"/>
</div>

---

## ⚠️ PRIMESEC RAIDKIT — USER INSTALLABLE DISCORD RAID BOT

**PRIMESEC RAIDKIT** is a powerful, lightweight, **user-installable** Discord raid tool for fast and silent payload deployment.

Works without needing bot permissions on the target server.

### 🔥 KEY FEATURES
- **`/primeraid`** — Official PRIMESEC signature raid (5x payload)
- **`/customraid [message] [count]`** — Deploy your own custom payload (1-5 strikes)
- **`/say [message]`** — Speak through the bot cleanly
- **`/ping`** — Real-time system diagnostics
- **`/help`** — Full command manual
- **`/join`** — Access to PRIMESEC

**Built-in Safety:**
- Per-user cooldown
- Payload length limit (1900 chars)
- Auto-reconnect + keep-alive

---

## 🚀 STEP-BY-STEP INSTALLATION

### 1. Clone the Repository
```bash
git clone https://github.com/YOURUSERNAME/primesec-raidkit.git
cd primesec-raidkit
```

### 2. Add Your Discord Token
1. Open the `.env` file (it should already exist)
2. Edit it and add your **Discord User Token** like this:

```env
DISCORD_TOKEN=your_discord_user_token_here
```

> **How to get your User Token:**
> - Open Discord in your browser (discord.com)
> - Press `Ctrl + Shift + I` to open Developer Tools
> - Go to the **Application** tab (or **Storage** → **Local Storage**)
> - Find `https://discord.com` and copy the value of the `token` key (it starts with `M` and is very long)
> - Paste it inside the `.env` file (remove any quotes if present)

**⚠️ Never share your token with anyone.**

### 3. Run the Bot
```bash
python main.py
```

The script will:
- Automatically install required packages (`discord.py`, `python-dotenv`)
- Start the bot
- Keep it alive 24/7

---

## ⚙️ CONFIGURATION (`config.py`)

You can fully customize the bot:

```python
SERVER_INVITE = "https://discord.gg/primesec"
BOT_NAME = "PRIME RAIDER"
BOT_COLOR = 0x0a0a0a
BOT_VERSION = "RAIDKIT v1.0"

PRIME_RAID_MSG = """# ɎØɄ ₳ⱤɆ ₳ⱠⱤɆ₳ĐɎ ɆӾ₱Ø₴ɆĐ..."""
PRIME_RAID_COUNT = 5
CUSTOM_RAID_MAX = 5
RAID_COOLDOWN = 1
```

**Fully customizable** — Change the raid message, count, cooldown, and appearance as you like.

---

## 🔗 Join PRIMESEC
```
https://discord.gg/primesec-1414146515139559495
```

---

*© 2026 Primesec Ops - Raid-Bot*  
*Licensed for educational/disruption research only*  
*Darkweb verified: primesec.toolkits*

---
