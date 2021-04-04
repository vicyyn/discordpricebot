import discord
import time
from pycoingecko import CoinGeckoAPI
import random

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
    await client.guilds[1].me.edit(nick = price + " USD")
  except Exception as e:
    print(e)
  print('updated')

async def main():
  starttime = time.time()
  while True:
      coin = cg.get_price(include_24hr_change='true',ids='cope', vs_currencies='usd')
      print(coin['cope']['usd'])
      price = str("{:.2f}".format(coin['cope']['usd'] + (random.randint(1,3)/100)))
      change = str(coin['cope']['usd_24h_change'])
      change = "{:.2f}".format(float(change))
      print("price is : " + price + " change : " + change)
      await update(price,change)
      time.sleep(20.0 - ((time.time() - starttime) % 20.0))


client = discord.Client()
cg = CoinGeckoAPI()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await main()

client.run(token,  reconnect = true)
