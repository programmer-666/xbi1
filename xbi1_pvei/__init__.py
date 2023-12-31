# xbi1_pvei.__init__.py
from urllib3 import disable_warnings
from .pvei_logger import version_log, pvei_log


# SSL support currently not available (Will be tested...)
# All communication works just HTTP
# ProxmoxAPI gets warning beacuse of this
# These warnings are ignored with disable_warnings()
disable_warnings()


class PVEInterface:
    # PVEI is a interface for ProxmoxVE API.
    # Developed for discord channels.
    @pvei_log
    def __init__(self, proxmox_api: 'ProxmoxAPI'):
        self.__pmox_api = proxmox_api
        self.node = self.__pmox_api.nodes.get()[0]['node']  # for first node

    @version_log
    def proxmox_version(self):
        # Returns proxmox version.
        return self.__pmox_api.version.get()

    def basic_information(self):
        # Returns
        #     id,
        #     maxcpu,
        #     maxmem,
        #     maxdisk
        # information used on selected node.
        basic_info = self.__pmox_api.nodes.get()[0]
        return {
            'id': basic_info['id'],
            'maxcpu': basic_info['maxcpu'],
            'maxmem': basic_info['maxmem'],
            'maxdisk': basic_info['maxdisk'],
        }

    def basic_status(self):
        # Returns status of node.
        disks = [
            {
                'model': disk['model'],
                'size': disk['size'],
                'type': disk['type']
            }
            for disk in self.__pmox_api.nodes(self.node).disks.list.get()
        ]

        qemus = [
            {
                'vmid': qemu['vmid'],
                'name': qemu['name'],
                'status': qemu['status'],
                'uptime': qemu['uptime'],
                'cpu': qemu['cpu'],
                'mem': qemu['mem'],
                'maxmem': qemu['maxmem'],
                'cpus': qemu['cpus'],
                'maxdisk': qemu['maxdisk'],
            }
            for qemu in self.__pmox_api.nodes(self.node).qemu.get()
        ]

        temp = self.__pmox_api.nodes(self.node).status.get()
        cpu_info = dict(temp['cpuinfo'])
        cpu_info.pop('flags', None)
        node = {
            'cpuinfo': cpu_info,
            'rootfs': temp['rootfs'],
            'memory': temp['memory']
        }
        del temp, cpu_info

        return {
            'node': node,
            'VMs': qemus,
            'disks': disks
        }
