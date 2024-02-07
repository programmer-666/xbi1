# embeds.py

from json import dumps
from discord import Embed
from datetime import datetime


pvei_url: str = 'https://172.16.1.150:8006'
author_url: str = 'https://github.com/programmer-666/xbi1'
bot_image_url: str = 'https://cdn.discordapp.com/app-icons/1176948443839737996/4750381453e4a1b72513529c8cbe4423.png?size=256'


def em_basic_status(pvei_data: dict):
    embed = Embed(
        title=list(pvei_data)[0],
        url=pvei_url,
        description='DESCRIPTION',
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
        value='NODE_INFORMATION',
        inline=False
    )
    embed.add_field(
        name='Virtual Machines',
        value='VM_INFOS',
        inline=False
    )
    embed.add_field(
        name='Disks',
        value='DISK_INFOS',
        inline=False
    )

    embed.set_image(
        url=bot_image_url
    )
    embed.set_footer(
        text='Proxmox',
        icon_url=bot_image_url
    )

    return embed
