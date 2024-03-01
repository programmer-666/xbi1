# pvei.py

from urllib3 import disable_warnings
from proxmoxer import ProxmoxAPI

from .pvei_logger import log


# SSL support currently not available (Will be tested...)
# All communication works just HTTP
# ProxmoxAPI gets warning beacuse of this
# These warnings are ignored with :
disable_warnings()


class PVEInterface:
    # PVEI is a interface for ProxmoxVE API.
    # Works on Proxmoxer module.
    # Developed for getting information about node.
    @log
    def __init__(self, proxmox_api: ProxmoxAPI):
        # still a beta code on test stage
        # self.node gets random node from ProxmoxVE
        self.__pmox_api = proxmox_api
        self.node = self.__pmox_api.nodes.get()[0]

    @log
    def change_node(self, node_id: int = 0) -> None:
        # changes current node
        self.node = self.__pmox_api.nodes.get()[node_id]
        return self.node

    @log
    def proxmox_version(self) -> dict:
        # Returns ProxmoxVE version, repoid and release.
        return self.__pmox_api.version.get()

    @log
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

    @log
    def basic_all_status(self) -> dict:
        # Returns all basic data of node.
        node = self.node['node']

        disks = [
            disk
            for disk in self.__pmox_api.nodes(node).disks.list.get()
        ]

        qemus = [
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

    @log
    def all_machines(self) -> dict:
        return {
            'qemus': [
                {
                    'vmid': qemu['vmid'],
                    'name': qemu['name'],
                    'status': qemu['status'],
                    'cpu': round(qemu['cpu'], 2),
                    'cpus': qemu['cpus'],
                    'uptime': qemu['uptime'],
                    'memu': round(qemu['mem'] / qemu['maxmem'], 2)
                }
                for qemu in self.__pmox_api.nodes(self.node['node']).qemu.get()
            ],
            'lxcs': [
                {
                    'vmid': lxc['vmid'],
                    'name': lxc['name'],
                    'status': lxc['status'],
                    'cpu': round(lxc['cpu'], 2),
                    'cpus': lxc['cpus'],
                    'uptime': lxc['uptime'],
                    'memu': round(lxc['mem'] / lxc['maxmem'], 2)
                }
                for lxc in self.__pmox_api.nodes(self.node['node']).lxc.get()
            ]
        }

    @log
    def all_nodes(self):
        nodes = self.__pmox_api.nodes.get()
