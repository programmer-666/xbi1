# xbi1.__init__.py
import configparser
from proxmoxer import ProxmoxAPI
from xbi1_pvei import PVEInterface
from xbi1_pvei import pvei_logger

from proxmoxer.core import AuthenticationError
from requests.exceptions import ConnectionError


config = configparser.ConfigParser()
config.read('conf.ini')

# pveiApi_state checks interface
# if proxmox connection established
# then changes state to True
pveiApi_state: bool = False

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
        # connection established without problem
        pveiApi_state = True

except AuthenticationError as exception:
    # In cases such as incorrect password or username
    pvei_logger.logger.exception(exception.args[0])

except ConnectionError as exception:
    pvei_logger.logger.exception(exception.args[0])

except Exception as exception:
    # for any other exceptions
    pvei_logger.logger.exception(exception.args[0])

finally:
    if not pveiApi_state:
        pvei_logger.logger.warning("PVEInterface cant created")
        quit()
