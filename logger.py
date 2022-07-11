import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def debug(log_tag, message):
	log_prefix = log_tag + ": "
	logging.debug(log_prefix + message)

def error(log_tag, message):
	log_prefix = log_tag + ": "
	logging.debug(log_prefix + message)