from discord.ext.commands import Bot
from discord import Intents, Message, Embed
from random import randint


class Client:
    def __init__(self, settings: dict[str, str]) -> None:
        intents = Intents.default()
        intents.reactions = True
        intents.message_content = True
        self.bot = Bot(
            command_prefix="%",
            intents=intents,
        )

        self.TOKEN = settings["TOKEN"]
        self.POST_TO = int(settings["POST_TO_ID"])
        self.POST_FROM = int(settings["POST_FROM_ID"])

        self.on_message = self.bot.event(self.on_message)

    def run(self):
        self.bot.run(self.TOKEN)

    async def on_message(self, message: Message):
        if message.channel.id != self.POST_FROM:
            return

        if len(message.attachments) == 0 or message.content == "":
            await message.delete()
            return

        await message.add_reaction("⭐")

        embed = Embed(
            color=randint(0, 0xFFFFFF),
            title=message.content,
            url=message.jump_url,
        )

        embed.set_author(
            name=message.author.name,
            url=f"https://discord.com/users/{message.author.id}",
            icon_url=message.author.avatar.url,
        )

        attachment = message.attachments[0].url
        embed.set_image(url=attachment)

        channel = await self.bot.fetch_channel(self.POST_TO)
        await channel.send(embed=embed)
