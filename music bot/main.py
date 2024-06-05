import os
from discord.ext import commands

TOKEN = ''

bot = commands.Bot(command_prefix="/")

for filename in os.listdir('/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is now online.')

bot.run(TOKEN)