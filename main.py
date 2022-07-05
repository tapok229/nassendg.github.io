import discord
from discord.ext import commands

config = {
    'token': 'OTkzODUyNzYwOTk2OTg2OTcw.Gg4kHI.HYyc2HHzdsNHU_QQuuJS_kGUL1PvL40QcPxiuM',
    'prefix': '?',
}

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()
async def статус(ctx):
    if ctx.author != bot.user:
        await ctx.reply("Статус: `В данный момент многие функции в разработке`.")

bot.run(config['token'])
