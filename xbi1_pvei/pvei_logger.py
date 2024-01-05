# pvei_logger
import logging.config
from logging import getLogger


logging.config.fileConfig('../xbi1/log_conf.ini')
logger = getLogger(__name__)


def pvei_log(function):
    # checks out if class called
    def dec_f(slf, pve):
        try:
            if pve:
                function(slf, pve)
        except 'proxmoxer.core.AuthenticationError' as e:
            logger.exception(e)
    return dec_f


def version_log(function):
    # gets pve's version
    def dec_f(slf):
        try:
            function(slf)
        except Exception as e:
            logger.exception(e)
        finally:
            logger.info(function.__name__)

    return dec_f


def basic_information_log(function):
    # gets pve's version
    def dec_f(slf):
        function(slf)
        logger.info(function.__name__)
    return dec_f
