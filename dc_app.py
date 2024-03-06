#!.venv/bin/python
# app.py

import json
import discord
from datetime import datetime
from discord.ext import commands, tasks

from __init__ import pvei, config
from dc_messages import pveiembeds, pveimessages


with open('timed_tasks.json') as timet:
    t_tasks: dict = json.load(timet)
# loads time and command data for scheduled tasks


def em_messages_table() -> dict:
    return {
        "version": pveiembeds.em_proxmox_version(
            pvei.proxmox_version()
        ),
        "b_status": pveiembeds.em_basic_all_status(
            pvei.basic_all_status()
        ),
        "n_information": pveiembeds.em_node_information(
            pvei.node_information()
        ),
        "machines": pveiembeds.em_all_machines(
            pvei.all_machines()
        )
    }


def messages_table() -> dict:
    return {
        "mtables": pveimessages.machines_table(pvei.all_machines())
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

    if datetime.now().year > dtime.year:
        # checks last datetime every second
        # if datetime is updated it updates dtime variable
        dtime = datetime.now()

        for command in em_messages_table():
            for sce_command in t_tasks['yearly']['commands']:
                if command == sce_command:
                    for channel in t_tasks['yearly']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            embed=em_messages_table()[command]
                        )
        # for embed messages

        for command in messages_table():
            for sce_command in t_tasks['yearly']['commands']:
                if command == sce_command:
                    for channel in t_tasks['yearly']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            messages_table()[command]
                        )
        # for not embed messages

    if datetime.now().month > dtime.month:
        dtime = datetime.now()

        for command in em_messages_table():
            for sce_command in t_tasks['monthly']['commands']:
                if command == sce_command:
                    for channel in t_tasks['monthly']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            embed=em_messages_table()[command]
                        )
        # for embed messages

        for command in messages_table():
            for sce_command in t_tasks['monthly']['commands']:
                if command == sce_command:
                    for channel in t_tasks['monthly']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            messages_table()[command]
                        )
        # for not embed messages

    if datetime.now().hour > dtime.hour:
        dtime = datetime.now()

        for command in em_messages_table():
            for sce_command in t_tasks['minutely']['commands']:
                if command == sce_command:
                    for channel in t_tasks['minutely']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            embed=em_messages_table()[command]
                        )
        # for embed messages

        for command in messages_table():
            for sce_command in t_tasks['minutely']['commands']:
                if command == sce_command:
                    for channel in t_tasks['minutely']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            messages_table()[command]
                        )
        # for not embed messages

    if datetime.now().minute > dtime.minute:
        dtime = datetime.now()

        for command in em_messages_table():
            for sce_command in t_tasks['minutely']['commands']:
                if command == sce_command:
                    for channel in t_tasks['minutely']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            embed=em_messages_table()[command]
                        )
        # for embed messages

        for command in messages_table():
            for sce_command in t_tasks['minutely']['commands']:
                if command == sce_command:
                    for channel in t_tasks['minutely']['channels']:
                        notf_channel = bot.get_channel(channel)
                        await bot.wait_until_ready()
                        await notf_channel.send(
                            messages_table()[command]
                        )
        # for not embed messages


# t_tasks function works every 1 second
# and checks hourly, minutely... jobs
# this is look not good but now it works, will be update...


@bot.event
async def on_ready():
    timed_tasks.start()


@bot.command(name='nodes')
async def nodes(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_nodes(
            pvei.nodes()
        )
    )
# b_status command sends basicly embed report
# takes embed message from dc_messages, pveiembeds


@bot.command(name='b_status')
async def basic_all_status_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_basic_all_status(
            pvei.basic_all_status()
        )
    )
# b_status command sends basicly embed report
# takes embed message from dc_messages, pveiembeds


@bot.command(name='n_information')
async def node_information_report(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_node_information(
            pvei.node_information()
        )
    )
# n_information sends information about node


@bot.command(name='machines')
async def all_lxcs(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_all_machines(
            pvei.all_machines()
        )
    )
# this command gets various data from lxc and qemu machines


@bot.command(name='machines_table')
async def machines_table(ctx: commands.context.Context, *args):
    await ctx.send(
        pveimessages.machines_table(
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


@bot.command(name='versions')
async def versions(ctx: commands.context.Context, *args):
    await ctx.send(
        embed=pveiembeds.em_proxmox_versions(
            pvei.proxmox_versions()
        )
    )
# returns node's proxmox version


@bot.command(name='ch_node')
async def ch_node(ctx: commands.context.Context, *args):
    await ctx.send(
        str(
            pvei.change_node(
                str(args[0])
            )
        )
    )
# changes active node

bot.run(config['DISCORD']['bot_token'])
