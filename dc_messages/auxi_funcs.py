# auxi_funcs.py
# auxiliary functions for messages

from datetime import timedelta


def togigabyte(memory: int) -> float:
    return round(memory / 1024 / 1024 / 1024, 2)


def avg_mem(mem: int, maxmem: int):
    return round((mem / maxmem) * 100, 2)


def sec_to_datetime(seconds):
    return str(timedelta(seconds=seconds))


def code_mark(desc: str):
    return '```' + str(desc) + '```'
