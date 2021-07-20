import discord
import os
import requests
import json
import random

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  jd= json.loads(response.text)
  quote = jd[0]['q']
  return quote

@client.event
async def on_ready():
  print('I am ready as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hey' or 'hello'):
    await message.channel.send('Hello Sir')

  if message.content.startswith('inspire'):
    await message.channel.send(get_quote)

client.run(os.environ['token'])




