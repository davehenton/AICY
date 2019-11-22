from pathlib import Path
import os
import logging
import datetime

def init_logging():
    #Creates a global logger
    logger = logging.getLogger("aicy_logger")
    logger.setLevel(logging.DEBUG)

    #Generate a logfile
    dirname = os.path.dirname(os.path.abspath(__file__))
    time = str(datetime.datetime.now()).replace(":", ".")
    logfilename = os.path.join(dirname , '_logs_' ,"log "+time+" .log")
    logfile = open(logfilename, "w")
    logfile.close()

    #Formater
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s') #A default one

    #Create Handler
    logfile_handler = logging.FileHandler(filename = logfilename)
    logfile_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(logfile_handler)
    logger.addHandler(stream_handler)
    logger.debug("I'm a test messages! If you see me, the logger is running!")

if __name__ == "__main__":
    init_logging()
