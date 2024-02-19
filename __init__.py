# xbi1.__init__.py

import configparser
from proxmoxer import ProxmoxAPI

from xbi1_pvei import pvei_logger
from xbi1_pvei.pvei import PVEInterface


config = configparser.ConfigParser()
config.read('ini.conf')

# pvei_api_state checks interface
# if proxmox connection established
# then changes state to True
pvei_api_state: bool = False

try:
    # pvei is ProxmoxVE's interface
    # should be exported and used
    pvei = PVEInterface(
        ProxmoxAPI(
            config['PROXMOX']['host'],
            user=config['PROXMOX']['user'],
            password=config['PROXMOX']['password'],
            verify_ssl=False
        )
    )

    if pvei:
        # if connection established without problem
        pvei_api_state = True

except Exception as exception:
    # for any exceptions
    pvei_logger.logger.exception(exception.args[0])

finally:
    if not pvei_api_state:
        pvei_logger.logger.warning('PVEInterface cant created')
