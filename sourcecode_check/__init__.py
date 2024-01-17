#!/usr/bin/python3
from os import walk
from hashlib import sha1


sc_hashes: list = []
for root, dir, files in walk('../'):
    for file in files:
        if file[-3:] == '.py':
            sc_hashes.append(
                sha1(
                    open("".join([root, '/', file]), 'rb').read()
                ).hexdigest()
            )
