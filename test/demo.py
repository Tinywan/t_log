#!/usr/bin/python3

from t_log import logger

log = logger.logger()

log.critical("这是一个 critical 级别的问题！")
log.error("这是一个 error 级别的问题！")
log.warning("这是一个 warning 级别的问题！")
log.info("这是一个 info 级别的问题！")
log.debug("这是一个 debug 级别的问题！")
