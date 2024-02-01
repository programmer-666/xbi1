#!.venv/bin/python
# app.py
# :scc:1:1001:

from __init__ import pvei
from threading import Thread
from sourcecode_check import scc


scc_thread = Thread(target=scc.activate_scc, name='SCC Thread')
scc_thread.start()

# pvei.proxmox_version()
# pvei.basic_information()
print(pvei.basic_status())
