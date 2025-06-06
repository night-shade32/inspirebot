
# ✨ InspireBot

A simple Discord bot that responds with a random inspirational quote when a user types `$inspire`. It uses the [RealInspire API](https://api.realinspire.live) to fetch quotes.

## 💡 Features

- Fetches motivational quotes from an external API
- Replies to the `$inspire` command in any channel it's present
- Easy to set up using a `.env` file for your Discord bot token

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/inspirebot.git
cd inspirebot
````

### 2. Install Requirements

Make sure Python 3.7+ is installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

**`requirements.txt` should contain:**

```
discord.py
requests
python-dotenv
```

### 3. Create `.env` File

In the root of your project, create a `.env` file and add your bot token:

```
DISCORD_TOKEN=your_discord_bot_token_here
```

> 🔒 Never share your bot token publicly.

---

## 🧠 Usage

Start the bot:

```bash
python bot.py
```

In any Discord channel your bot has access to, type:

```
$inspire
```

And the bot will reply with an inspirational quote 🎯

---

## 📦 Project Structure

```
.
├── bot.py           # Main bot script
├── .env             # Environment variables (not committed to Git)
├── README.md        # This file
└── requirements.txt # Python dependencies
```

---

## 🛠️ Tech Stack

* [Discord.py](https://discordpy.readthedocs.io/)
* [Requests](https://docs.python-requests.org/)
* [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🤖 Example

> **User**: `$inspire`
> **Bot**: *"You must live in the present, launch yourself on every wave..."* — **Henry David Thoreau**


