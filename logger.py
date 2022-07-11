import logging

logging.basicConfig(
	level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
    	logging.FileHandler("motion_sensor.log", mode='w'),
    	logging.StreamHandler()
    ]
)

def debug(log_tag, message):
	log_prefix = log_tag + ": "
	logging.debug(log_prefix + message)

def error(log_tag, message):
	log_prefix = log_tag + ": "
	logging.error(log_prefix + message)