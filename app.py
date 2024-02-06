#!.venv/bin/python
# app.py
# :scc:1:1001:

import discord
from threading import Thread
from sourcecode_check import scc
from __init__ import pvei, config
from emb_messages import pveiembeds
from discord.ext import commands, tasks


scc_thread = Thread(target=scc.activate_scc, name='SCC Thread')
scc_thread.start()

# pvei.proxmox_version()
# pvei.basic_information()
# print(pvei.basic_status())

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)
client = discord.Client(intents=intents)


@tasks.loop(seconds=30)
async def testloop1():
    await bot.get_channel(1182785923910471691).send(embed=pveiembeds.em_basic_status(pvei.basic_status()))


@bot.event
async def on_ready():
    sct_guild = bot.get_guild(1182784272403267684)
    for cat in sct_guild.categories:
        print(cat)
    # testloop1.start()


@bot.command(name='b_status')
async def basic_status_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_status(pvei.basic_status())
    )


bot.run(config['DISCORD']['bot_token'])
