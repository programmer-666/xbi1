# pveiembeds.py

from datetime import datetime
from discord import Embed

from .embed_templates import InformationalEmbed
from .auxi_funcs import togigabyte, sec_to_datetime, avg_mem


pvei_url: str = 'https://172.16.1.150:8006'
author_url: str = 'https://github.com/programmer-666/xbi1'

em_template = Embed()


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
            result += ' - **Uptime:** ' + \
                str(sec_to_datetime(vm['uptime'])) + '\n'
            result += ' - **CPU:** ' + str(round(vm['cpu'], 2)) + '%\n'

            result += ' - **Memory:** ' + \
                str(avg_mem(vm['mem'], vm['maxmem'])) + '%'
            result += ' (' + str(togigabyte(vm['mem']))
            result += '/' + str(togigabyte(vm['maxmem'])) + ')\n'

            result += ' - **CPUs:** ' + str(vm['cpus']) + '\n'
            result += ' - **MaxDisk:** ' + \
                str(togigabyte(vm['maxdisk'])) + '\n'

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

    basic_status_embed = InformationalEmbed(
        title=list(pvei_data)[0],
        url=pvei_url,
        description='Basic All Status',
        timestamp=datetime.now()
    )
    basic_status_embed.set_author(
        name='XBI1 - Notification Bot',
        url=author_url
    )
    basic_status_embed.set_thumbnail()
    basic_status_embed.set_footer(
        text='Proxmox'
    )

    basic_status_embed.add_field(
        name='Node',
        value=node_field(pvei_data[list(pvei_data)[0]]),
        inline=False
    )
    basic_status_embed.add_field(
        name='Virtual Machines',
        value=vm_lxc_field(pvei_data[list(pvei_data)[1]]),
        inline=False
    )
    basic_status_embed.add_field(
        name='LXCs',
        value=vm_lxc_field(pvei_data[list(pvei_data)[3]]),
        inline=False
    )
    basic_status_embed.add_field(
        name='Disks',
        value=disks_field(pvei_data[list(pvei_data)[2]]),
        inline=True
    )

    return basic_status_embed


def em_node_information(pvei_data: dict):
    def node_information_field(b_info: dict):
        result: str = ''

        for info in b_info:
            result += '- **' + info + ': **'
            if info in ['maxmem', 'maxdisk']:
                result += str(togigabyte(b_info[info])) + '\n'
            else:
                result += str(b_info[info]) + '\n'

        return result

    node_information_embed = InformationalEmbed(
        title='Proxmox Norification',
        url=pvei_url,
        description='Basic Information current node.',
        timestamp=datetime.now()
    )
    node_information_embed.set_author(
        name='XBI1 - Notification Bot',
        url=author_url
    )
    node_information_embed.set_thumbnail()
    node_information_embed.set_footer(
        text='Proxmox'
    )

    node_information_embed.add_field(
        name='Basic Information',
        value=node_information_field(pvei_data),
        inline=False
    )

    return node_information_embed


def em_nodes(pvei_data: dict):
    def nodes_field(n_info: dict):
        result: str = ''

        for nodes in n_info:
            for info in nodes:
                result += '- **' + info + ': **'
                if info in ['maxmem', 'maxdisk']:
                    result += str(togigabyte(nodes[info])) + '\n'
                else:
                    result += str(nodes[info]) + '\n'
            result += '\n'

        return result

    nodes_embed = InformationalEmbed(
        title='Nodes',
        url=pvei_url,
        description='All Nodes.',
        timestamp=datetime.now()
    )

    nodes_embed.set_author(
        name='XBI1 - Notification Bot',
        url=author_url
    )
    nodes_embed.set_thumbnail()
    nodes_embed.set_footer(
        text='Proxmox'
    )

    nodes_embed.add_field(
        name='All nodes in the cluster.',
        value=nodes_field(pvei_data),
        inline=False
    )

    return nodes_embed


def em_all_machines(pvei_data: dict):
    def qemus_field(qemus_dict: dict):
        result: str = ''

        for qemu in qemus_dict:
            result += '- ' + str(qemu['vmid']) + ' **:** '
            result += str(qemu['name']) + ' **:** '
            result += str(qemu['status'])[:1] + ' **:** '
            result += '%' + str(round(qemu['cpu'], 2) * 100) + ' **:** '
            result += str(qemu['cpus']) + ' **:** '
            result += str(sec_to_datetime(qemu['uptime'])) + ' **:** '
            result += '%' + str(round(qemu['memu'], 2) * 100)
            result += '\n'

        return result

    def lxcs_field(lxcs_dict: dict):
        result: str = ''

        for lxc in lxcs_dict:
            result += '- ' + str(lxc['vmid']) + ' **:** '
            result += str(lxc['name']) + ' **:** '
            result += str(lxc['status'])[:1] + ' **:** '
            result += '%' + str(round(lxc['cpu'], 2) * 100) + ' **:** '
            result += str(lxc['cpus']) + ' **:** '
            result += str(sec_to_datetime(lxc['uptime'])) + ' **:** '
            result += '%' + str(round(lxc['memu'], 2) * 100)
            result += '\n'

        return result

    all_machines_embed = InformationalEmbed(
        title='Proxmox Norification',
        url=pvei_url,
        description='All information for Qemus and LXCs.',
        timestamp=datetime.now()
    )
    all_machines_embed.set_author(
        name='XBI1 - Notification Bot',
        url=author_url
    )
    all_machines_embed.set_thumbnail()
    all_machines_embed.set_image()
    all_machines_embed.set_footer(
        text='Proxmox'
    )

    all_machines_embed.add_field(
        name='Qemus',
        value=qemus_field(pvei_data['qemus']),
        inline=False
    )

    all_machines_embed.add_field(
        name='LXCs',
        value=lxcs_field(pvei_data['lxcs']),
        inline=False
    )

    return all_machines_embed


def em_proxmox_version(pvei_data: dict):
    def desc_version(pvei_data: dict):
        return '**' + pvei_data['version'] + '**'

    version_embed = InformationalEmbed(
        title='Proxmox Version',
        description=desc_version(pvei_data),
        timestamp=datetime.now()
    )

    version_embed.set_author()
    version_embed.set_thumbnail()
    version_embed.set_footer(
        text="Proxmox"
    )

    return version_embed


def em_proxmox_versions(pvei_data: list):
    def desc_versions(pvei_data: list):
        result: str = ''

        for node in pvei_data:
            result += '- **' + node[0] + '**: '
            result += node[1] + '\n'

        return result

    version_embed = InformationalEmbed(
        title='Proxmox Version',
        description=desc_versions(pvei_data),
        timestamp=datetime.now()
    )

    version_embed.set_author()
    version_embed.set_thumbnail()
    version_embed.set_footer(
        text="Proxmox"
    )

    return version_embed
