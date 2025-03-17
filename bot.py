import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.messages = True  

#Bot Prefix:
bot = commands.Bot(command_prefix=";", intents=intents)


#Bot Events
@bot.event
async def on_ready():
    print(f'Im Currently online {bot.user}')

    

#Bot Commands

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hey, {ctx.author.mention}!')

@bot.command()
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f'Result: {result}')

@bot.command()
async def multiply(ctx, num1: int, num2: int):
    result = num1 * num2
    await ctx.send(f'Result: {result}')

@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

# Bot Token
bot.run("YOUR_BOT_TOKEN")
