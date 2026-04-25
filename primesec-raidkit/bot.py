import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os, time, datetime, asyncio

from config import (
    SERVER_INVITE, BOT_NAME, BOT_COLOR, BOT_VERSION,
    PRIME_RAID_MSG, PRIME_RAID_COUNT, CUSTOM_RAID_MAX, RAID_COOLDOWN
)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("[CRITICAL] TOKEN MISSING -- ABORTED")
    exit(1)

class Limiter:
    def __init__(self):
        self.last = {}

    def check(self, uid):
        wait = RAID_COOLDOWN - (time.time() - self.last.get(uid, 0))
        return (False, wait) if wait > 0 else (True, 0)

    def use(self, uid):
        self.last[uid] = time.time()

lim = Limiter()

class PrimeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!", intents=discord.Intents.default(),
            allowed_contexts=app_commands.AppCommandContext(
                guild=True, dm_channel=True, private_channel=True
            ),
            allowed_installs=app_commands.AppInstallationType(
                guild=True, user=True
            ),
        )
        self.up = time.time()

    async def setup_hook(self):
        await self.tree.sync()
        print(f"[SYS] {len(self.tree.get_commands())} COMMANDS LOADED")

    async def on_ready(self):
        print("=" * 45)
        print(f"   {BOT_NAME} [{BOT_VERSION}]")
        print(f"   {self.user} ({self.user.id})")
        print(f"   LATENCY: {round(self.latency*1000)}ms")
        print(f"   STATUS: ARMED")
        print("=" * 45)
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="YOUR SERVER | /help"
            ),
            status=discord.Status.dnd
        )

    async def on_resumed(self):
        print("[SYS] CONNECTION RESTORED")

bot = PrimeBot()

def dark(title, desc):
    e = discord.Embed(
        title=title, description=desc, color=BOT_COLOR,
        timestamp=datetime.datetime.now(datetime.timezone.utc)
    )
    e.set_footer(text=f"{BOT_NAME} // discord.gg/primesec")
    return e

def threat(title, desc):
    e = discord.Embed(
        title=title, description=desc, color=0x8B0000,
        timestamp=datetime.datetime.now(datetime.timezone.utc)
    )
    e.set_footer(text=f"{BOT_NAME} // DENIED")
    return e

class LinkView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(discord.ui.Button(
            label="PRIMESEC", url=SERVER_INVITE, style=discord.ButtonStyle.link
        ))

async def strike(interaction, payload, count):
    ok, wait = lim.check(interaction.user.id)
    if not ok:
        await interaction.response.send_message(
            embed=threat(
                ">> ACCESS THROTTLED",
                f"```ansi\n"
                f"\u001b[2;31m"
                f"[LIMITER] REQUEST DENIED\n"
                f"[LIMITER] WAIT {wait:.1f}s\n"
                f"\u001b[0m"
                f"```"
            ),
            ephemeral=True
        )
        return

    lim.use(interaction.user.id)

    try:
        await interaction.response.send_message(
            "```\n[PRIME RAIDER] ARMED\n```",
            ephemeral=True
        )
    except Exception:
        return

    for _ in range(count):
        try:
            await asyncio.sleep(0.8)
            await interaction.followup.send(payload)
        except Exception:
            break

@bot.tree.command(name="help", description="Command manual.")
async def c_help(interaction: discord.Interaction):
    await interaction.response.send_message(
        embed=dark(
            ">> PRIME RAIDER",
            f"```ansi\n"
            f"\u001b[2;31m"
            f"________________________________________\n"
            f"\n"
            f"  [PRIME RAIDER] COMMAND INTERFACE\n"
            f"________________________________________\n"
            f"\n"
            f"  /primeraid\n"
            f"  PRIMESEC signature strike.\n"
            f"  count: {PRIME_RAID_COUNT} | unchangeable.\n"
            f"\n"
            f"  /customraid [message] [count]\n"
            f"  deploy your own payload.\n"
            f"  count: 1-{CUSTOM_RAID_MAX} | you choose.\n"
            f"\n"
            f"  /say [message]\n"
            f"  speak through the bot.\n"
            f"  count: 1 | unchangeable.\n"
            f"\n"
            f"  /join\n"
            f"  access point to primesec.\n"
            f"\n"
            f"  /ping\n"
            f"  system diagnostics.\n"
            f"\n"
            f"  /help\n"
            f"  you are here.\n"
            f"\n"
            f"________________________________________\n"
            f"  cooldown: {RAID_COOLDOWN}s\n"
            f"  type: user-install\n"
            f"  status: armed\n"
            f"________________________________________\n"
            f"\n"
            f"  discord.gg/primesec\n"
            f"________________________________________\n"
            f"\u001b[0m"
            f"```"
        ),
        view=LinkView()
    )

@bot.tree.command(name="join", description="Access point.")
async def c_join(interaction: discord.Interaction):
    await interaction.response.send_message(
        embed=dark(
            ">> ACCESS POINT",
            f"```ansi\n"
            f"\u001b[2;31m"
            f"________________________________________\n"
            f"\n"
            f"  [PRIMESEC] GATEWAY\n"
            f"________________________________________\n"
            f"\n"
            f"  SERVER   : PRIME SECURITY\n"
            f"  STATUS   : ONLINE\n"
            f"  ACCESS   : UNRESTRICTED\n"
            f"  PROTOCOL : discord.gg/primesec\n"
            f"\n"
            f"  >> ENTER AT YOUR OWN RISK.\n"
            f"\n"
            f"________________________________________\n"
            f"\u001b[0m"
            f"```\n"
            f"**>>** [discord.gg/primesec]({SERVER_INVITE})"
        ),
        view=LinkView()
    )

@bot.tree.command(name="primeraid", description="PRIMESEC signature strike. count 5. unchangeable.")
async def c_pr(interaction: discord.Interaction):
    await strike(interaction, PRIME_RAID_MSG, PRIME_RAID_COUNT)

@bot.tree.command(name="customraid", description="Deploy your own payload. count 1-5.")
@app_commands.describe(message="Your payload.", count="How many. 1-5.")
async def c_cr(
    interaction: discord.Interaction,
    message: str,
    count: app_commands.Range[int, 1, 5] = 3
):
    if len(message) > 1900:
        await interaction.response.send_message(
            embed=threat(">> REJECTED", "```\nPAYLOAD EXCEEDS 1900 CHAR LIMIT\n```"),
            ephemeral=True
        )
        return
    await strike(interaction, message, count)

@bot.tree.command(name="say", description="Speak through the bot. count 1. unchangeable.")
@app_commands.describe(message="What to say.")
async def c_say(interaction: discord.Interaction, message: str):
    if len(message) > 1900:
        await interaction.response.send_message(
            embed=threat(">> REJECTED", "```\nMESSAGE EXCEEDS 1900 CHAR LIMIT\n```"),
            ephemeral=True
        )
        return

    try:
        await interaction.response.send_message(
            "```\n[PRIME RAIDER] SENT\n```",
            ephemeral=True
        )
    except Exception:
        return

    try:
        await interaction.followup.send(message)
    except Exception:
        try:
            await interaction.followup.send(
                embed=threat(">> BLOCKED", "```\nMESSAGE COULD NOT BE DELIVERED\n```"),
                ephemeral=True
            )
        except Exception:
            pass

@bot.tree.command(name="ping", description="System diagnostics.")
async def c_ping(interaction: discord.Interaction):
    s = int(time.time() - bot.up)
    ms = round(bot.latency * 1000)
    st = "ARMED" if ms < 150 else "DEGRADED"

    await interaction.response.send_message(
        embed=dark(
            ">> DIAGNOSTICS",
            f"```ansi\n"
            f"\u001b[2;31m"
            f"________________________________________\n"
            f"\n"
            f"  [PRIME RAIDER] SYSTEM STATUS\n"
            f"________________________________________\n"
            f"\n"
            f"  LATENCY  : {ms}ms\n"
            f"  STATUS   : {st}\n"
            f"  UPTIME   : {s//86400}d {(s%86400)//3600}h {(s%3600)//60}m {s%60}s\n"
            f"  PROTOCOL : ACTIVE\n"
            f"\n"
            f"________________________________________\n"
            f"\u001b[0m"
            f"```"
        )
    )

@bot.tree.error
async def on_err(interaction: discord.Interaction, err: app_commands.AppCommandError):
    if isinstance(err, app_commands.CommandInvokeError):
        o = err.original
        if isinstance(o, discord.HTTPException):
            e = threat(">> DISCORD REJECTED", f"```\n{o.status} | {o.text[:150]}\n```")
        else:
            e = threat(">> INTERNAL FAILURE", f"```\n{str(o)[:200]}\n```")
            print(f"[ERR] {o}")
    else:
        e = threat(">> FAILURE", f"```\n{str(err)[:200]}\n```")

    try:
        if interaction.response.is_done():
            await interaction.followup.send(embed=e, ephemeral=True)
        else:
            await interaction.response.send_message(embed=e, ephemeral=True)
    except Exception:
        pass

if __name__ == "__main__":
    bot.run(TOKEN, log_handler=None, reconnect=True)