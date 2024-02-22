#!.venv/bin/python
# app.py

import json
import discord
from datetime import datetime
from discord.ext import commands, tasks

from __init__ import pvei, config
from dc_messages import pveiembeds, pveimessages


with open('dc_ids.json') as dcj_file:
    dc_ids: dict = json.load(dcj_file)
# dc_ids.json file holds guld and channel id's
# bot interact channels with theese data

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)
# discord bot defination

dtime = datetime.now()
# dtime declared for timed jobs


@tasks.loop(seconds=1)
async def basic_all_status_loop() -> None:
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
# and checks hourly, minutely jobs
# this is look not good but now it works, will be update...


@bot.event
async def on_ready():
    # basic_all_status_loop.start()
    pass


@bot.command(name='b_status')
async def basic_all_status_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_all_status(pvei.basic_all_status())
    )
# b_status command sends basicly embed report
# takes embed message from dc_messages, pveiembeds


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
# this command gets various data from lxc and qemu machines


@bot.command(name='mtables')
async def all_mtables(ctx: commands.context.Context, *args):
    await ctx.send(
        pveimessages.all_machines_table(
            pvei.all_machines()
        )
    )
# sends information about lxc and qemu machines
# but not embed, ascii table with code marks ```


@bot.command(name='version')
async def version(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_proxmox_version(
            pvei.proxmox_version()
        )
    )

bot.run(config['DISCORD']['bot_token'])
