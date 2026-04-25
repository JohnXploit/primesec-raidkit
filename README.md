
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

**PRIMESEC RAIDKIT** is a powerful, lightweight, **user-installable** Discord raid tool designed for fast and silent payload deployment.

Works without needing bot permissions on the target server.

### 🔥 KEY FEATURES
- **`/primeraid`** — Official PRIMESEC signature raid (5x high-impact payload)
- **`/customraid [message] [count]`** — Deploy your own custom raid message (1-5 strikes)
- **`/say [message]`** — Speak through the bot cleanly
- **`/ping`** — Real-time latency + uptime diagnostics
- **`/help`** — Full command manual
- **`/join`** — Access to PRIMESEC network

**Built-in Protections:**
- Per-user cooldown system
- Payload length protection (1900 char limit)
- Auto-reconnect + persistent keep-alive
- Minimal detection footprint

---

## 🚀 STEP-BY-STEP INSTALLATION

### 1. Clone the Repository
```bash
git clone https://github.com/JohnXploit/primesec-raidkit.git
cd primesec-raidkit
```

### 2. Add Your Bot Token
1. Open the `.env` file
2. Paste your **Discord Bot Token** like this:

```env
DISCORD_TOKEN=your_bot_token_here
```

> **How to get your Bot Token:**
> 1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
> 2. Create a new Application (or select existing one)
> 3. Go to **Bot** section → Click **Reset Token** (or Copy Token)
> 4. Copy the token and paste it into the `.env` file

**⚠️ Important:** Keep your bot token private. Never share it publicly.

### 3. Run the Bot
```bash
python main.py
```

The launcher will automatically install required dependencies (`discord.py`, `python-dotenv`) and start the bot with keep-alive.

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

---

## 🔗 Join PRIMESEC
```
https://discord.gg/primesec-1414146515139559495
```
---

*© 2026 Primesec Ops - Raid-bot*  
*Licensed for educational/disruption research only*  
*Darkweb verified: primesec.toolkits*  

---

