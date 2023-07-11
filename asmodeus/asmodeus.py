import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user.name}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")

@bot.command()
async def hau(ctx):
    await ctx.send(f"Hello, {ctx.author.name}! I'm fine, and you?")

bot.run("MTEyMDI2MjYyMTE2MjExMTAxNg.GuX7J6.nqRy39VK1DeuLTYvjFtluUwm2TNTFN5KfraIO8")

