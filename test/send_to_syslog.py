import logging
import logging.handlers
import sys
import socket
import logmatic

logger = logging.getLogger()

sh = logmatic.SysLogJsonHandler('/dev/log')
sh.setFormatter(logmatic.JsonFormatter(extra={"hello": "world","hostname":socket.gethostname()},prefix="appname: "))
logger.addHandler(sh)

logger.setLevel(logging.INFO)

test_logger = logging.getLogger("test")
test_logger.info({"special": "value", "run": 12})
test_logger.info("classic message", extra={"special": "value", "run": 12})

def exception_test():
    try:
        raise Exception('test')
    except Exception:
        test_logger.exception("This is a fake exception")

def unicode_exception_test():
    test_logger.warn("abh\xa0ren")

exception_test()
unicode_exception_test()
