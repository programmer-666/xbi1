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
# dc_ids.json file holds guild and channel id's
# bot interact channels with theese data

with open('timed_tasks.json') as timet:
    t_tasks: dict = json.load(timet)
# loads time and command data for scheduled tasks

em_messages_table: dict = {
    "version": pveiembeds.em_proxmox_version(pvei.proxmox_version()),
    "b_status": pveiembeds.em_basic_all_status(pvei.basic_all_status()),
    "b_information": pveiembeds.em_basic_information(pvei.basic_information()),
    "machines": pveiembeds.em_all_machines(pvei.all_machines())
}
# embed messages dict for scheduled tasks

messages_table: dict = {
    "mtables": pveimessages.all_machines_table(pvei.all_machines())
}
# embed messages dict for scheduled tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)
# discord bot defination

dtime = datetime.now()
# dtime declared for timed jobs


@tasks.loop(seconds=1)
async def timed_tasks() -> None:
    global dtime

    # there is a counter logic here
    # dtime holds last time
    # t_tasks function checks every second dtimes if its up to date

    if datetime.now().hour > dtime.hour:
        # checks last datetime every second
        # if datetime is updated it updates dtime variable
        dtime = datetime.now()

        for command in em_messages_table:
            for sce_command in t_tasks['hourly']['commands']:
                if command == sce_command:
                    for channel in t_tasks['hourly']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            embed=em_messages_table[command]
                        )

    if datetime.now().minute > dtime.minute:
        # same function but works minutely
        dtime = datetime.now()

        for command in em_messages_table:
            for sce_command in t_tasks['minutely']['commands']:
                if command == sce_command:
                    for channel in t_tasks['minutely']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            embed=em_messages_table[command]
                        )
        # for embed messages

        for command in messages_table:
            for sce_command in t_tasks['minutely']['commands']:
                if command == sce_command:
                    for channel in t_tasks['minutely']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            messages_table[command]
                        )
        # for not embed messages


# t_tasks function works every 1 second
# and checks hourly, minutely jobs
# this is look not good but now it works, will be update...


@bot.event
async def on_ready():
    timed_tasks.start()


@bot.command(name='b_status')
async def basic_all_status_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_all_status(
            pvei.basic_all_status()
        )
    )
# b_status command sends basicly embed report
# takes embed message from dc_messages, pveiembeds


@bot.command(name='b_information')
async def basic_information_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_information(
            pvei.basic_information()
        )
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
# returns node's proxmox version


@bot.command(name='ch_node')
async def ch_node(ctx: commands.context.Context, *args):
    await ctx.send(
        str(
            pvei.change_node(
                int(args[0])
            )
        )
    )
# changes active node

bot.run(config['DISCORD']['bot_token'])
