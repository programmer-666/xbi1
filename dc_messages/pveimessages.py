from table2ascii import table2ascii
from .pveiembeds import code_mark


def all_machines_table(pvei_data: dict):
    lxcs: list = pvei_data['lxcs']
    qemus: list = pvei_data['qemus']

    lxc_table = table2ascii(
        header=list(lxcs[0].keys()),
        body=[list(lxc.values()) for lxc in lxcs]
    )

    qemu_table = table2ascii(
        header=list(qemus[0].keys()),
        body=[list(qemu.values()) for qemu in qemus]
    )

    return code_mark(lxc_table) + code_mark(qemu_table)
