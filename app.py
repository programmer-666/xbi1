#!.venv/bin/python
# app.py
from __init__ import pvei
from threading import Thread


def main_t():
    pvei.proxmox_version()


thread = Thread(target=main_t)
thread.start()
thread.join()
