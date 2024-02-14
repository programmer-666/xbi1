# xbi1_pvei.__init__.py
# :scc:2:1003:
from urllib3 import disable_warnings
from .pvei_logger import get_log


# SSL support currently not available (Will be tested...)
# All communication works just HTTP
# ProxmoxAPI gets warning beacuse of this
# These warnings are ignored with :
disable_warnings()


class PVEInterface:
    # PVEI is a interface for ProxmoxVE API.
    # Developed for getting node informations.
    @get_log
    def __init__(self, proxmox_api: 'ProxmoxAPI'):
        # still a beta code on test stage
        # self.node gets first node from ProxmoxVE
        self.__pmox_api = proxmox_api
        self.node = self.__pmox_api.nodes.get()[0]

    @get_log
    def change_node(self, node_id: int = 0) -> None:
        self.__pmox_api.nodes.get()[node_id]

    @get_log
    def proxmox_version(self):
        # Returns ProxmoxVE version.
        return self.__pmox_api.version.get()

    @get_log
    def basic_information(self) -> dict:
        # this function returns selected node's
        # maximum cpu, memory and disk usage
        basic_info = self.node  # self.__pmox_api.nodes.get()[0]
        return {
            'id': basic_info['id'],
            'maxcpu': basic_info['maxcpu'],
            'maxmem': basic_info['maxmem'],
            'maxdisk': basic_info['maxdisk'],
        }

    @get_log
    def basic_all_status(self) -> dict:
        # Returns status of node.
        node = self.node['node']
        disks = [
            # {
            #     'model': disk['model'],
            #     'size': disk['size'],
            #     'type': disk['type']
            # }
            disk
            for disk in self.__pmox_api.nodes(node).disks.list.get()
        ]

        qemus = [
            # {
            #     'vmid': qemu['vmid'],
            #     'name': qemu['name'],
            #     'status': qemu['status'],
            #     'uptime': qemu['uptime'],
            #     'cpu': qemu['cpu'],
            #     'mem': qemu['mem'],
            #     'maxmem': qemu['maxmem'],
            #     'cpus': qemu['cpus'],
            #     'maxdisk': qemu['maxdisk'],
            # }
            qemu
            for qemu in self.__pmox_api.nodes(node).qemu.get()
        ]

        lxcs = [
            lxc
            for lxc in self.__pmox_api.nodes(node).lxc.get()
        ]

        temp = self.__pmox_api.nodes(node).status.get()
        cpu_info = dict(temp['cpuinfo'])
        cpu_info.pop('flags', None)
        node = {
            'cpuinfo': cpu_info,
            'rootfs': temp['rootfs'],
            'memory': temp['memory']
        }
        del temp, cpu_info

        return {
            self.node['node']: node,
            'VMs': qemus,
            'disks': disks,
            'lxcs': lxcs
        }

    @get_log
    def all_machines(self):
        return {
            'qemus': [
                {
                    'vmid': qemu['vmid'],
                    'name': qemu['name'],
                    'status': qemu['status'],
                    'cpu': qemu['cpu'],
                    'cpus': qemu['cpus'],
                    'uptime': qemu['uptime'],
                    'memu': qemu['mem']/qemu['maxmem']
                }
                for qemu in self.__pmox_api.nodes(self.node['node']).qemu.get()
            ],
            'lxcs': [
                {
                    'vmid': lxc['vmid'],
                    'name': lxc['name'],
                    'status': lxc['status'],
                    'cpu': lxc['cpu'],
                    'cpus': lxc['cpus'],
                    'uptime': lxc['uptime'],
                    'memu': lxc['mem']/lxc['maxmem']
                }
                for lxc in self.__pmox_api.nodes(self.node['node']).lxc.get()
            ]
        }
