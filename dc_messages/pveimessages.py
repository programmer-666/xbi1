# pveimessages.py

from table2ascii import table2ascii

from .auxi_funcs import code_mark


def machines_table(pvei_data: dict):
    lxcs: list = pvei_data['lxcs']
    qemus: list = pvei_data['qemus']

    lxc_table = ''
    qemu_table = ''

    if len(lxcs) > 0:
        lxc_table = table2ascii(
            header=list(lxcs[0].keys()),
            body=[list(lxc.values()) for lxc in lxcs]
        )

    if len(qemus) > 0:
        qemu_table = table2ascii(
            header=list(qemus[0].keys()),
            body=[list(qemu.values()) for qemu in qemus]
        )

    return code_mark(':LXC MACHINES:\n' + lxc_table) \
        + code_mark(':QEMU MACHINES:\n' + qemu_table)
