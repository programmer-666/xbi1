#!.venv/bin/python
# app.py
# :scc:1:1001:

import json
import discord
from threading import Thread
from sourcecode_check import scc
from __init__ import pvei, config
from emb_messages import pveiembeds
from discord.ext import commands, tasks


scc_thread = Thread(
    target=scc.activate_scc,
    name='SCC Thread'
)

scc_thread.start()

with open('dc_ids.json') as dcj_file:
    dc_ids: dict = json.load(dcj_file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@tasks.loop(seconds=60)
async def testloop1():
    for guild in list(dc_ids):
        notf_channel = bot.get_channel(dc_ids[guild]['id_notfc'])

        await notf_channel.send(
            embed=pveiembeds.em_basic_status(
                pvei.basic_status()
            )
        )

        break


@bot.event
async def on_ready():
    testloop1.start()


@bot.command(name='b_status')
async def basic_status_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_status(pvei.basic_status())
    )


bot.run(config['DISCORD']['bot_token'])
