import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

PREFIX = os.getenv("PREFIX")
TOKEN = os.getenv("TOKEN") # Coloque seu token no .env / put your token in .env

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Connected as {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('------')
    
    
    await bot.tree.sync()
    print("synchronized commands...")


async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Cog {filename} uploaded successfully!')
            except Exception as e:
                print(f'Failed to load cog {filename}: {e}')

async def main():
    await load_cogs()
    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())