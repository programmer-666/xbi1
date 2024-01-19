# scc.py
# :scc:1:1005

import sqlite3
from sys import argv
from pathlib import Path
from json import load as jload
from configparser import ConfigParser

SCC_CONFIG_FILE: str = argv[1]
SCC_PATHS_FILE: str = argv[2]
SCC_MAX_LINE: int = 10

scc_paths: dict = None
scc_sc_data: list = []

# Read config data
config = ConfigParser()
config.read(SCC_CONFIG_FILE)

# Reading source code paths
with open(SCC_PATHS_FILE, 'r', encoding='utf-8') as paths_file:
    scc_paths = jload(paths_file)


def sourcecode_control():
    for source_code in scc_paths['source_code_paths']:
        with open(source_code, 'r') as src:
            scc_sc_data.append([(scc_code[2:-1],
                                Path(source_code).resolve()._str,
                                Path(source_code).name)
                                for scc_code in [next(src)
                                for _ in range(SCC_MAX_LINE)]
                                if ':{c_header}:'.format
                                (c_header=config.get('SCC', 'code_header'))
                                in scc_code][0])


class SccSQLite3:
    def __init__(self):
        with sqlite3.connect('scc.db') as tmp_db_connection:
            tdbc_cursor = tmp_db_connection.cursor()
            tdbc_cursor.execute('CREATE TABLE IF NOT EXISTS "source_codes" \
                ("id_sc" integer NOT NULL,"path_sc" text NOT NULL, "name_sc" \
                varchar NOT NULL DEFAULT NULL, "code_sc" varchar NOT NULL, \
                PRIMARY KEY (id_sc))')


if __name__ == '__main__':
    #SccSQLite3()
    sourcecode_control()
    print(scc_sc_data)
