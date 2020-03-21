import logging


class A:
    def __init__(self):
        self.logger = logging.getLogger(self.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("initialized")
    def hello_world(self):
        self.logger.info("hello world")


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
        "%(asctime)-15s - %(name)s - %(levelname)s - %(message)s")

#add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

a = A()
logger.debug("debug message")
logger.info("info message")
logger.info("warn message")
logger.error("error message")
logger.critical("critical message")

a.hello_world()





