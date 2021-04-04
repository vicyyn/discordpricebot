import discord
from pycoingecko import CoinGeckoAPI
import asyncio

token = 'cope'
guildName = "COPE"
botToken = 'your_bot_token'

async def update(price,change):
  print('updating')
  try:
    if(float(change) > 0):
      stt = discord.Status.online
      change = "+" + change
    else:
      stt = discord.Status.dnd
    await client.change_presence(
        status= stt,
        activity=discord.Activity(type=discord.ActivityType.watching,
                                  name=change+"%" + " | copeusd coingecko price | made by @vicyyn")
    );
    guild = [ guild for guild in client.guilds if guild.name== guildName]
    await guild[0].me.edit(nick = price + " USD")
  except Exception as e:
    print(e)
  print('updated')

async def main():
  while True:
      coin = cg.get_price(include_24hr_change='true',ids=token, vs_currencies='usd')
      print(coin[token]['usd'])
      price = str("{:.2f}".format(coin[token]['usd']))
      change = str(coin[token]['usd_24h_change'])
      change = "{:.2f}".format(float(change))
      print("price is : " + price + " change : " + change)
      await update(price,change)
      await asyncio.sleep(5)


client = discord.Client()
cg = CoinGeckoAPI()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await main()

client.run(botToken,  reconnect = True)
