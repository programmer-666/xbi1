# embeds.py

from json import dumps
from discord import Embed
from datetime import datetime, timedelta


pvei_url: str = 'https://172.16.1.150:8006'
author_url: str = 'https://github.com/programmer-666/xbi1'
bot_image_url: str = 'https://cdn.discordapp.com/app-icons/1176948443839737996/4750381453e4a1b72513529c8cbe4423.png?size=256'


def togigabyte(memory: int) -> float:
    return round(memory / 1024 / 1024 / 1024, 2)


def avg_mem(mem: int, maxmem: int):
    return round((mem / maxmem) * 100, 2)


def sec_to_datetime(seconds):
    return str(timedelta(seconds=seconds))


def code_mark(dict_data: dict):
    return '```' + str(dumps(dict_data, indent=4)) + '```'


def virtual_machines(vm_dict: dict):
    result: str = ''

    for vm in vm_dict:
        result += '- **[' + str(vm['vmid']) + ':' + vm['name'] + ']**\n'

        result += ' - **Status:** ' + str(vm['status']) + '\n'
        result += ' - **Uptime:** ' + str(sec_to_datetime(vm['uptime'])) + '\n'
        result += ' - **CPU:** ' + str(round(vm['cpu'], 2)) + '%\n'

        result += ' - **Memory:** ' + str(avg_mem(vm['mem'], vm['maxmem'])) + '%'
        result += ' (' + str(togigabyte(vm['mem']))
        result += '/' + str(togigabyte(vm['maxmem'])) + ')\n'

        result += ' - **CPUs:** ' + str(vm['cpus']) + '\n'
        result += ' - **MaxDisk:** ' + str(togigabyte(vm['maxdisk'])) + '\n\n'

    return result


def em_basic_status(pvei_data: dict):
    embed = Embed(
        title=list(pvei_data)[0],
        url=pvei_url,
        description='Basic Status',
        colour=0xc65059,
        timestamp=datetime.now()
    )

    embed.set_author(
        name='XBI1 - Notification Bot',
        url=author_url,
        icon_url=bot_image_url
    )

    embed.add_field(
        name='Node',
        value=code_mark(pvei_data[list(pvei_data)[0]]),
        inline=False
    )
    embed.add_field(
        name='Virtual Machines',
        value=virtual_machines(pvei_data[list(pvei_data)[1]]),
        inline=False
    )
    embed.add_field(
        name='Disks',
        value=code_mark(pvei_data[list(pvei_data)[2]]),
        inline=False
    )

    embed.set_thumbnail(
        url=bot_image_url
    )

    embed.set_image(
        url=bot_image_url
    )
    embed.set_footer(
        text='Proxmox',
        icon_url=bot_image_url
    )

    return embed
