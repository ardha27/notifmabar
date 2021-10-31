import os
import discord
import requests

# for local environment
from dotenv import load_dotenv
load_dotenv()

# get environment variables
DISCORD_BOT_ACCESS_TOKEN = os.environ["OTA0MzcwMDE5NDU3MjAwMTI5.YX6iNw.saBg6H4DtZ74KlsWTetjZMbkeHs"]
LINE_NOTIFY_ACCESS_TOKEN = os.environ["vetajiaNHjtu073BEHFV360rRD59gY4PhIen7DSb4XD"]
VOICE_CHANNEL_ID1 = os.environ["664097385558966272"]
VOICE_CHANNEL_ID2 = os.environ["578242481674518551"]

LINE_NOTIFY_API_URL = "https://notify-api.line.me/api/notify"
HEADERS = {"Authorization": "Bearer " + LINE_NOTIFY_ACCESS_TOKEN}

client = discord.Client()


@client.event
async def on_voice_state_update(member, before, after):
    # This function is called when not only member join to the voice channel,
    # but also member changed their status to mute.
    # So, it is necessary to catch only events that joining channel.
    if before.channel != after.channel:
        if after.channel is not None and after.channel.id == int(VOICE_CHANNEL_ID1):
            _name = member.nick if member.nick else member.name
            message = {
                "message": "\n" + _name + "In The Discord Livestream"
            }
            requests.post(LINE_NOTIFY_API_URL, headers=HEADERS, data=message)
        if after.channel is not None and after.channel.id == int(VOICE_CHANNEL_ID2):
            _name = member.nick if member.nick else member.name
            message = {
                "message": "\n" + _name + "In The Discord Nongskuy"
            }
            requests.post(LINE_NOTIFY_API_URL, headers=HEADERS, data=message)

client.run(DISCORD_BOT_ACCESS_TOKEN)
