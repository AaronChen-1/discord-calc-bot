import os
import re
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="calc")
async def calculate(ctx, *, expression: str):
    # Replace comma decimals (e.g. 27,9 → 27.9)
    expression = re.sub(r"(\d),(\d)", r"\1.\2", expression)

    # Strip everything except digits, decimal points, + and -
    cleaned = re.sub(r"[^\d.+\-]", "", expression)

    # Extract signed numbers (e.g. -86, +41.2, 146)
    tokens = re.findall(r"[+-]?\d+(?:\.\d+)?", cleaned)

    if not tokens:
        await ctx.send("No valid numbers found.")
        return

    total = sum(float(t) for t in tokens)

    # Show as integer if result is whole, otherwise round to avoid float noise
    result = int(total) if total == int(total) else round(total, 6)
    await ctx.send(f"**{result}**")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(os.environ["DISCORD_TOKEN"])
