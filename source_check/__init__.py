#!/usr/bin/python3
import os
from hashlib import sha1


sc_hashes: list = []
for root, dir, files in os.walk('../'):
    for file in files:
        if file[-3:] == '.py':
            sc_hashes.append(
                sha1(
                    open("".join([root, '/', file]), 'rb').read()
                ).hexdigest()
            )
