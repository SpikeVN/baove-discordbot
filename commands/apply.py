import cfg_man
import discord
import storage
import translation
import pandas as pd
import xlsxwriter as exel


async def apply(message: discord.Message, args: list):
    """
    Processes application process.
    """
    # TODO: Allows options for DM and channel.
    cache = storage.Cache()
    dm = message.author.dm_channel
    if 0 < len(cache) <= cfg_man.read("questions"):
        # First time answering.
        cache.data["answer"].append("".join(args[3:len(args)]))
        cache.data["question-no"] += 1
        await dm.send(translation.get_str("ok"))
        await dm.send(translation.get_str(str(cache.data["question-no"])))
        cache.commit()

    elif cache.data["question-no"] == cfg_man.read("questions")+1:
        # The final question.
        await dm.send(translation.get_str(cfg_man.read("question-no")))
    else:
        await dm.send(translation.get_str("hello"))
        await dm.send(translation.get_str("prompt"))
        cache.data["answer"] = []
        cache.data["question-no"] = 1
        cache.commit()


def save_xlsx(content: dict):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = exel.Workbook("result.xlsx")
    page = res.add_worksheet()
    page.write("A1", "Username")
    page.write("B1", "Discord")
    page.write("C1", "Minecraft Account")
    # Writes down all the category
    i = 0
    for category in content["cat"]:
        page.write(alphabet[3+i] + "1", category)
        i += 1
    no = 0
    for answe
