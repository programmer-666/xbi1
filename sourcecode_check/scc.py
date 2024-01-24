# scc.py
# :scc:1:1005

import sqlite3
from os import stat
from pathlib import Path
from json import load as jload
from configparser import ConfigParser

SCC_CONFIG_FILE: str = 'scc.conf'  # argv[1]
SCC_PATHS_FILE: str = 'scc_paths.json'  # argv[2]
SCC_MAX_LINE: int = 10
# SCC_MAX_LINE is checks files first 10 lines for scc code

scc_paths: dict = None
scc_sc_data: list = []


config = ConfigParser()
config.read(SCC_CONFIG_FILE)
# Read config data


with open(SCC_PATHS_FILE, 'r', encoding='utf-8') as paths_file:
    # read source code paths from json file
    # paths can be relative or absolute
    scc_paths = jload(paths_file)


def sourcecode_control() -> None:
    # sourcecode_control function takes paths and reads source codes
    # opens every file and reads first 10 (scc_max_line) lines
    # gets scc_codes, absolute paths and source code file name
    # all data goest to the scc_sc_data variable
    # returns None
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


def sourcecode_sc_inofs():
    print([s for s in stat('../app.py')])


class SCQlite(sqlite3.Connection):
    def cursor(self):
        return super(SCQlite, self).cursor(SCQCursor)


class SCQCursor(sqlite3.Cursor):
    def create_db(self):
        self.execute('CREATE TABLE IF NOT EXISTS "source_codes" \
                ("sc_id" integer NOT NULL, "sc_path" \
                text NOT NULL, "sc_name" varchar NOT NULL DEFAULT NULL, \
                "sc_code" varchar NOT NULL, PRIMARY KEY (sc_id));')
        # creating source_codes tables
        self.execute('CREATE UNIQUE INDEX IF NOT EXISTS \
            sc_path_ix ON source_codes (sc_path);')
        # indexes

    def insert_paths(self, sc_data: list):
        self.executemany('INSERT OR IGNORE INTO source_codes \
            (sc_code, sc_path, sc_name) VALUES (?, ?, ?);', sc_data)


if __name__ == '__main__':
    db_connection: SCQlite = sqlite3.connect('scc.db', factory=SCQlite)
    cursor = db_connection.cursor()
    cursor.create_db()

    sourcecode_control()
    # get data scc_sc_data

    cursor.insert_paths(scc_sc_data)
    db_connection.commit()
    # commit changes to database

    print(sourcecode_sc_inofs())
