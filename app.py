#!.venv/bin/python
# app.py
# :scc:1:1001:
from __init__ import pvei
from threading import Thread
from sourcecode_check import scc


scc.activate_scc()


def main_t():
    pvei.proxmox_version()
    pvei.basic_information()
    pvei.basic_status()


thread = Thread(target=main_t, name="main function", )
thread.start()
thread.join()
