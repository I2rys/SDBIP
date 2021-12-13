#Dependencies
import discord
from discord.ext import commands

#Variables
bot = commands.Bot(command_prefix=".", description="Simple Discord bot in Python")

#Main
@bot.event
async def on_ready():
    print("Discord bot is running.")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run("DiscordBotTokenHere")
