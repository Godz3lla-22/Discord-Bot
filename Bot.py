import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme/SoccerMeme')
  print(response.text)
  json_data = json.loads(response.text)
  return json_data['url']

strike = 0
async def monitor(message):
  global strike
  if 'curse' in message.content.lower() or 'cursing' in message.content.lower() or 'curser' in message.content.lower():
    if strike == 0:
      reply = "don't curse, That's your first strike"
      strike += 1
    elif strike == 1:
      reply = "don't curse, That's your second strike"
      strike += 1
    elif strike == 2:
      reply = "That's it, you will be kicked out!!"
      strike = 0
    await message.channel.send(reply)


class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      meme_url = get_meme()
      await message.channel.send(meme_url)
    if 'curse' in message.content.lower():
      await monitor(message)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(Token)