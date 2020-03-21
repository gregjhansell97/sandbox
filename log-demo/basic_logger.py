import logging

#logging.basicConfig(filename="example.log", level=logging.DEBUG)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

logging.debug("this message should go to the log file")
logging.warning("Watch out!")
logging.info("I told you so")




