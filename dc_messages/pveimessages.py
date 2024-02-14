from table2ascii import table2ascii
from datetime import datetime, timedelta


def all_machines_table(pvei_data: dict):
    lxcs: list = pvei_data['lxcs']

    lxc_table = table2ascii(
        header=list(lxcs[0].keys()),
        body=lxcs
    )
    print(lxc_table)
    return list(lxcs[0])
