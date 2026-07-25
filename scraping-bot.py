import os
import discord
from discord.ext import commands
import yfinance as yf
from dotenv import load_dotenv

# 1. Carica le variabili dal file .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2. Inizializza il bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.command()
async def prezzo(ctx, ticker):
    simbolo = ticker.upper()
    
    try:
        prezzo_attuale = yf.Ticker(simbolo).fast_info['last_price']
        await ctx.send(f"📈 Il prezzo di **{simbolo}** è **${prezzo_attuale:.2f}**")
    except Exception:
        await ctx.send(f"❌ Impossibile trovare il ticker **{simbolo}**. Verifica che sia corretto!")

# 3. Avvia il bot recuperando il token sicuro
if TOKEN:
    bot.run(TOKEN)
else:
    print("ERRORE: DISCORD_TOKEN non trovato nel file .env!")