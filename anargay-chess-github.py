import discord
import time
import random
from discord.ext import commands

# invite me to your server: https://discord.com/api/oauth2/authorize?client_id=1208444590475051088&permissions=274945018880&scope=bot

TOKEN = "TOKEN"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='en$', intents=intents)
en_passant = ["google en passant", "holy hell", "new response just dropped", "actual zombie", "call the exorcist", "bishop goes on vacation, never comes back",
           "knightmare fuel", "pawn storm incoming", "checkmate or riot", "queen sacrifice, anyone", "rook in the corner, plotting world domination",
           "ignite the chessboard"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name=":3"))
    for guild in bot.guilds:
        await guild.me.edit(nick="Anargay Chess")

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    content = message.content.lower()

    # reply to $brick
    if content.startswith('$brick'):
        time.sleep(15)
        await message.channel.send('dont decline en passant again >:3')
    
    # reply to $bread
    if content.startswith('$bread'):
        if random.randint(1, 100) == 1:
            time.sleep(1)
            await message.channel.send('🍞 :3')
        elif random.randint(1, 5) == 1:
            time.sleep(1)
            await message.channel.send('bread :3')

    # reply to :boop:
    if content in ['<:boop:1158242566085541959>', ':boop:', '*boop*', 'boop']:
        await message.reply('<:boop:1158242566085541959>')

    # reply to :3
    if content == ':3':
        await message.reply(':3')

    # reply to en passant chain
    if content in en_passant:
        reply_value = int(en_passant.index(content)) + 1
        if reply_value != 12:
            await message.reply(f'{en_passant[reply_value]} :3')

    await bot.process_commands(message)

# $$echo [text]
@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)

# $$github
@bot.command()
async def github(ctx):
    await ctx.send('<https://github.com/Bananattttx/Anargay-Chess>')

bot.run(TOKEN)