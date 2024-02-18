#!.venv/bin/python
# app.py
# :scc:1:1001:

import json
import discord
from threading import Thread
from datetime import datetime
from discord.ext import commands, tasks

from sourcecode_check import scc
from __init__ import pvei, config
from dc_messages import pveiembeds, pveimessages


scc_thread: Thread = Thread(
    target=scc.activate_scc,
    name='SCC Thread'
)
scc_thread.start()
# SCC works differen thread take time

with open('dc_ids.json') as dcj_file:
    dc_ids: dict = json.load(dcj_file)
# dc_ids.json file holds guld and channel id's
# bot interact channels with theese data

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)
# discord bot defination

dtime = datetime.now()
# dtime declared for timed jobs

@tasks.loop(seconds=1)
async def basic_all_status_loop():
    global dtime

    if datetime.now().hour > dtime.hour:
        # checks last datetime every second
        # then starts sending messages to channels
        dtime = datetime.now()

        await bot.wait_until_ready()
        for guild in list(dc_ids):
            notf_channel = bot.get_channel(dc_ids[guild]['id_notfc'])

            await notf_channel.send(
                embed=pveiembeds.em_basic_all_status(
                    pvei.basic_all_status()
                )
            )
        # takes every channel id and sends messages

    if datetime.now().minute > dtime.minute:
        # same function but works minutely
        dtime = datetime.now()
        await bot.wait_until_ready()

        for guild in list(dc_ids):
            notf_channel = bot.get_channel(dc_ids[guild]['id_notfc'])
            await notf_channel.send(
                embed=pveiembeds.em_basic_all_status(
                    pvei.basic_all_status()
                )
            )
# basic_all_status_loop function works every 1 second
# and checks hourly, minutely jobs
# this is look not good but now it works, will be update...

@bot.event
async def on_ready():
    pass
    # basic_all_status_loop.start()


@bot.command(name='b_status')
async def basic_all_status_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_all_status(pvei.basic_all_status())
    )
# b_status command sends basicly embed report
# takes embed message from dc_messages, pveiembeds

@bot.command(name='b_information')
async def basic_information_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_information(pvei.basic_information())
    )
# b_information sends information about node

@bot.command(name='machines')
async def all_lxcs(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_all_machines(
            pvei.all_machines()
        )
    )
# this command gets various data from lxc and qemu machines

@bot.command(name='mtables')
async def all_mtables(ctx: commands.context.Context, *args):
    await ctx.send(
        pveimessages.all_machines_table(
            pvei.all_machines()
        )
    )
# sends information about lxc and qemu machines
# but not embed, ascii table with code marks ```

bot.run(config['DISCORD']['bot_token'])
