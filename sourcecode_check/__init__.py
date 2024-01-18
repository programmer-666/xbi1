#!/usr/bin/python3
# sourcecode_check
# :scc:3:1004:
from os import walk
from hashlib import sha1
from configparser import ConfigParser


config = ConfigParser()
config.read('scc.conf')

# find all python source code files
# read first line for scMark
# if sc file has scMark then create hashes
# compress all logs and store
# works with terminal, can takes args...

# PSUEDO CODE
"""
sc_hashes: list = []
for root, dir, files in walk('../'):
    for file in files:
        if file[-3:] == '.py':
            sc_hashes.append(
                sha1(
                    open("".join([root, '/', file]), 'rb').read()
                ).hexdigest()
            )
"""
