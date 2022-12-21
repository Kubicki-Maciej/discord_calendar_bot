import discord

from discord import app_commands
import json

import logs
from os import listdir
from os.path import isfile, join
from discord.ext.commands import command


def load_json(file_name='token.json'):
    with open(file_name) as f:
        return json.loads(f.read())


def discord_token():
    return load_json()['token']


class MyClient(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        for guild in client.guilds:
            if guild.name == '1054932144515985561':
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
        )

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

# Logs
logs.logger.addHandler(logs.handler)

# intents
# intents = discord.Intents.default()
# intents.message_content = True

# Get list of commands_discord
# command_list = [f for f in listdir('commands_discord') if isfile(join('commands_discord', f)) and f.endswith('.py')]


# Client
client = MyClient()
client.run(discord_token(), log_handler=None)
