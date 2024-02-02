#!.venv/bin/python
# app.py
# :scc:1:1001:

import discord
from discord.ext import commands
from json import dumps
from xbi1_pvei import pvei_logger
from __init__ import pvei, config
from threading import Thread
from sourcecode_check import scc


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

scc_thread = Thread(target=scc.activate_scc, name='SCC Thread')
scc_thread.start()

# pvei.proxmox_version()
# pvei.basic_information()
# print(pvei.basic_status())


@bot.command(name='test')
async def test(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=discord.Embed(title='Test', description=dumps(pvei.basic_information()))
    )


bot.run(config['DISCORD']['bot_token'])
