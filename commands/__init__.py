import apply
import discord
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext


class Slash(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="apply")
    async def apply(self, ctx: SlashContext):
        await apply.apply(ctx.message, separate_args(ctx.message))


def separate_args(command: str):
    current_token = ""
    output = []
    for c in command:
        if c == " ":
            output.append(current_token)
        else:
            current_token += c

    return output


def parse(message: discord.Message):
    args = separate_args(message.content)
    if (args[1] == "apply") | (args[1] == "ans"):
        apply.apply(message, args)
    # TODO: more commands
