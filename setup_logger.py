# setup_logger.py
import logging

def get_logger(name):
    """Returns a logger object with file and console handlers"""
    format="%(asctime)s %(levelname)s:-:%(name)s:-:%(message)s"
    # logging.basicConfig(format=format)
    file_handler = logging.FileHandler("logfile.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(format))
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter(format))


    ## Create the format
    logging.basicConfig(level=logging.DEBUG,format=format,handlers=[file_handler,console_handler])
    logger = logging.getLogger(name)

    ## Create a logger
    # logger = logging.getLogger(__name__)
    # logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    return logger

# init logger
if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.debug("Hello World!")
    logger.info("Hello World!")
    logger.warning("Hello World!")
    logger.error("Hello World!")
    logger.critical("Hello World!")
