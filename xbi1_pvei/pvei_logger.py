# xbi1_pvei.pvei_logger.py
import logging.config
from logging import getLogger
from time import time

logging.config.fileConfig('../xbi1/log_conf.ini')
logger = getLogger(__name__)


total_work_time: float = 0

"""
def pvei_log(function):
    # checks out if class called
    def dec_f(*args):
        global total_work_time

        # xbi1.__init__.py:19, first try-catch block
        # that try-catch block checks connection
        # if ProxmoxVE connection control is success
        # then works this method and creates info log
        decf_start_time: time = time()
        f_var = function(*args)

        work_time: float = round(
            (time() - decf_start_time) * 1000.0, 2
        )

        logger.info(
            '{work_time:.2f}::{function_qualname}'.
            format(
                work_time=work_time,
                function_qualname=function.__qualname__
            )
        )
        total_work_time += work_time

        return f_var
    return dec_f


def version_log(function):
    # proxmox version functions log
    def dec_f(*args):
        global total_work_time

        decf_start_time: time = time()
        f_var = function(*args)

        work_time: float = round(
            (time() - decf_start_time) * 1000.0, 2
        )

        logger.info(
            '{work_time:.2f}::{function_qualname}'.
            format(
                work_time=work_time,
                function_qualname=function.__qualname__
            )
        )
        total_work_time += work_time

        return f_var
    return dec_f


def basic_information_log(function):
    # log for basic information function
    def dec_f(*args):
        global total_work_time

        decf_start_time: time = time()
        f_var = function(*args)

        work_time: float = round(
            (time() - decf_start_time) * 1000.0, 2
        )

        del decf_start_time

        logger.info(
            '{work_time:.2f}::{function_qualname}'.
            format(
                work_time=work_time,
                function_qualname=function.__qualname__
            )
        )
        total_work_time += work_time

        return f_var
    return dec_f
"""


def get_log(function):
    # log for basic information function
    def dec_f(*args):
        global total_work_time

        decf_start_time: time = time()
        f_var = function(*args)

        work_time: float = round(
            (time() - decf_start_time) * 1000.0, 2
        )

        del decf_start_time

        logger.info(
            '{work_time:.2f}::{function_qualname}'.
            format(
                work_time=work_time,
                function_qualname=function.__qualname__
            )
        )
        total_work_time += work_time

        return f_var
    return dec_f
