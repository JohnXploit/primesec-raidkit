import subprocess, sys, time

print("[PRIME RAIDER] INITIALIZING...")

try:
    subprocess.check_call([
        sys.executable, "-m", "pip", "install",
        "discord.py>=2.4.0", "python-dotenv>=1.0.0",
        "--quiet", "--disable-pip-version-check"
    ])
except Exception:
    pass

while True:
    try:
        if subprocess.call([sys.executable, "bot.py"]) == 0:
            break
        print("[SYS] RESTARTING IN 5s...")
        time.sleep(5)
    except KeyboardInterrupt:
        break