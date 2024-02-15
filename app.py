#!.venv/bin/python
# app.py
# :scc:1:1001:

import json
import discord
from threading import Thread
from datetime import datetime
from sourcecode_check import scc
from __init__ import pvei, config
from discord.ext import commands, tasks
from dc_messages import pveiembeds, pveimessages


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

dtime = datetime.now()


@tasks.loop(seconds=1)
async def basic_all_status_loop():
    global dtime

    if datetime.now().hour > dtime.hour:
        dtime = datetime.now()

        await bot.wait_until_ready()
        for guild in list(dc_ids):
            notf_channel = bot.get_channel(dc_ids[guild]['id_notfc'])

            await notf_channel.send(
                embed=pveiembeds.em_basic_all_status(
                    pvei.basic_all_status()
                )
            )

    if datetime.now().minute > dtime.minute:
        dtime = datetime.now()
        await bot.wait_until_ready()

        for guild in list(dc_ids):
            notf_channel = bot.get_channel(dc_ids[guild]['id_notfc'])
            await notf_channel.send(
                embed=pveiembeds.em_basic_all_status(
                    pvei.basic_all_status()
                )
            )


@bot.event
async def on_ready():
    pass
    # basic_all_status_loop.start()


@bot.command(name='b_status')
async def basic_all_status_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_all_status(pvei.basic_all_status())
    )


@bot.command(name='b_information')
async def basic_information_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_information(pvei.basic_information())
    )


@bot.command(name='machines')
async def all_lxcs(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_all_machines(
            pvei.all_machines()
        )
    )


@bot.command(name='mtables')
async def all_mtables(ctx: commands.context.Context, *args):
    await ctx.send(
        pveimessages.all_machines_table(
            pvei.all_machines()
        )
    )

bot.run(config['DISCORD']['bot_token'])
