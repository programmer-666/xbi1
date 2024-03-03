# xbi1_pvei.pvei_logger.py
# :scc:1:1002:
import logging.config
from time import time
from typing import Callable
from logging import getLogger


logging.config.fileConfig('../xbi1/log_conf.ini')
logger = getLogger(__name__)


# total_work_time: float = 0
# this variable for metric
# not necessary, but if you want to use
# you need to activate relating operation

def log(function) -> Callable:
    # this function creates a log output to logs/xbi1.log
    # n these logs you can see which classes and methods were called
    def dec_f(*args) -> Callable:
        # global total_work_time

        decf_start_time: float = time()
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
        # total_work_time += work_time

        return f_var
    return dec_f
