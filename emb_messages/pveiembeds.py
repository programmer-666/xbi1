# pveiembeds.py

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


def em_basic_all_status(pvei_data: dict):
    def node_field(node_dict: dict):
        result: str = ''
        for nodep in node_dict:
            tmp: str = ''
            tmp += '- **' + str(nodep).title() + '**\n'
            for nodeps in node_dict[nodep]:
                tmp += ' - **' + str(nodeps).title() + '**: '
                if str(nodep) in ['rootfs', 'memory']:
                    tmp += str(togigabyte(node_dict[nodep][nodeps])) + '\n'
                else:
                    tmp += str(node_dict[nodep][nodeps]) + '\n'
            result += tmp + '\n'

        return result

    def vm_lxc_field(vm_dict: dict):
        result: str = ''

        for vm in vm_dict:
            result += '- **[ ' + str(vm['vmid']) + ':' + vm['name'] + ' ]**\n'

            result += ' - **Status:** ' + str(vm['status']) + '\n'
            result += ' - **Uptime:** ' + str(sec_to_datetime(vm['uptime'])) + '\n'
            result += ' - **CPU:** ' + str(round(vm['cpu'], 2)) + '%\n'

            result += ' - **Memory:** ' + str(avg_mem(vm['mem'], vm['maxmem'])) + '%'
            result += ' (' + str(togigabyte(vm['mem']))
            result += '/' + str(togigabyte(vm['maxmem'])) + ')\n'

            result += ' - **CPUs:** ' + str(vm['cpus']) + '\n'
            result += ' - **MaxDisk:** ' + str(togigabyte(vm['maxdisk'])) + '\n'

            result += ' - **DiskWrite:** ' + str(vm['diskwrite']) + '\n'
            result += ' - **DiskRead:** ' + str(vm['diskread']) + '\n'

            result += ' - **NetIn:** ' + str(vm['netin']) + '\n'
            result += ' - **NetOut:** ' + str(vm['netout']) + '\n\n'

        return result

    def disks_field(disk_dict: dict):
        result: str = ''

        for disk in disk_dict:
            result += '- **' + str(disk['model']) + '**\n'
            result += ' - **Size: **' + str(togigabyte(disk['size'])) + '\n'
            result += ' - **Type: **' + str(disk['type']) + '\n'
            result += ' - **RPM: **' + str(disk['rpm']) + '\n'
            result += ' - **Vendor: **' + str(disk['vendor']) + '\n'
            result += ' - **Health: **' + str(disk['health']) + '\n'
            result += ' - **GPT: **' + str(disk['gpt']) + '\n'
            result += ' - **Used: **' + str(disk['used']) + '\n\n'

        return result

    embed = Embed(
        title=list(pvei_data)[0],
        url=pvei_url,
        description='Basic All Status',
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
        value=node_field(pvei_data[list(pvei_data)[0]]),
        inline=False
    )
    embed.add_field(
        name='Virtual Machines',
        value=vm_lxc_field(pvei_data[list(pvei_data)[1]]),
        inline=False
    )
    embed.add_field(
        name='LXCs',
        value=vm_lxc_field(pvei_data[list(pvei_data)[3]]),
        inline=False
    )
    embed.add_field(
        name='Disks',
        value=disks_field(pvei_data[list(pvei_data)[2]]),
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
