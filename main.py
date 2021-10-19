import commands
import discord
from discord.ext.commands import Bot
import cfg_man


bot = Bot(command_prefix="bv", self_bot=True, help_command=False, intents=discord.Intents.default())


async def on_ready():
    print("Bot is online and ready.")


@bot.event
async def on_message(message: discord.Message):
    if message.content.startswith(cfg_man.read("prefix")) & (~cfg_man.read("use-slash-command")):
        commands.parse(message)


if __name__ == "__main__":
    # Multi-file bot
    bot.load_extension("cog")
    bot.run(cfg_man.read("token"))
