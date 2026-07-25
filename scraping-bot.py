import os
import discord
from discord.ext import commands
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def prezzo(ctx, ticker):
    simbolo = ticker.upper()
    
    try:
        prezzo_attuale = yf.Ticker(simbolo).fast_info['last_price']
        await ctx.send(f"Il prezzo di **{simbolo}** è **${prezzo_attuale:.2f}**")
    except Exception:
        await ctx.send(f"Impossibile trovare il ticker **{simbolo}**. Verificare sia corretto.")

if TOKEN:
    bot.run(TOKEN)
else:
    print("ERRORE: DISCORD_TOKEN non trovato nel file .env")