# Showcase Bot
![](https://github.com/eliseydudin/showcase-bot/blob/main/thumbnail.gif)

# How to install?
1. Get [uv](https://github.com/astral-sh/uv)
2. Do `uv venv` and `uv sync` 
3. Create a `.env` file, and put there the bot's `TOKEN`, and ids of the channels you want to post from/to (`POST_FROM_ID`, `POST_TO_ID`)
It will look something like this:
```toml
TOKEN = "yourdiscord.token"
POST_FROM_ID = "1274282222346059028"
POST_TO_ID = "1274282259637239684"
```
4. Do `uv run src/showcase_bot/__init__.py`

If you want the bot to run 24/7 then I recommend you also get [supervisor](https://github.com/Supervisor/supervisor)
