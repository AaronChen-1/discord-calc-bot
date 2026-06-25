# Discord Calc Bot

A small Discord bot that adds numbers from a message and replies with the total.

## What It Does

Use the `!calc` command with numbers, plus signs, or minus signs:

```text
!calc 10 + 5 - 3
```

The bot replies:

```text
12
```

It also works with extra text because the bot pulls out the numbers and signs:

```text
!calc lunch 12.50 + tip 3.25 - discount 2
```

## Setup

1. Clone the repo:

```bash
git clone https://github.com/AaronChen-1/discord-calc-bot.git
cd discord-calc-bot
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a Discord bot in the Discord Developer Portal.

5. Enable the `Message Content Intent` for your bot.

6. Invite the bot to your server with permission to read and send messages.

7. Set your bot token as an environment variable:

```bash
export DISCORD_TOKEN="your-bot-token-here"
```

8. Run the bot:

```bash
python bot.py
```

When it starts successfully, you should see a message like:

```text
Logged in as YourBotName
```

## Usage

In Discord, type:

```text
!calc 100 + 25 - 10
```

The bot will reply with:

```text
115
```

## Future Feature Ideas

This bot is intentionally simple right now, but it can grow over time. Good next features could include:

- Multiplication and division support
- Parentheses and full calculator expressions
- A help command
- Better error messages
- Currency or tip calculations
- Slash command support
- Calculation history per user

## Notes

Keep your Discord bot token private. Do not paste it into the code or commit it to GitHub.
