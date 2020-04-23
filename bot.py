# bot.py

import os
import discord
import json
from dotenv import load_dotenv

enhancedMention = config.enhancedMention || { user: false, role: false, channel: false};


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.AutoShardedClient()
relays = json.load('relays.json')

async def on_ready(self):
    shards = client.shard_count
    guilds = client.guilds
    users  = client.users

    print(
        f'\n Total Shard Count: {shards}',
        f'\n Connected Servers: {len(guilds)}',
        f'\n Total Users Count: {len(users)}',
    )

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise    

print(f'RavnX is X-ing the multiverse')
client.run(TOKEN)
