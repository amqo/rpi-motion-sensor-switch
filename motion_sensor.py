from gpiozero import MotionSensor

import time_api
import switch_api
import logger
import datetime

LOG_TAG = 'MOTION SENSOR'

# Raspberry Pi GPIO pin config
sensor = MotionSensor(14)

# Time limits
start = datetime.time(7, 0, 0)
end = datetime.time(22, 0, 0)

def on_motion():
    logger.debug(LOG_TAG, 'Motion detected!')
    if time_api.time_in_range(start, end):
        if switch_api.is_switch_off(): 
            switch_api.turn_on_switch()
    else:
        logger.debug(LOG_TAG, 'Ignoring motion, out of time')

def no_motion():
    logger.debug(LOG_TAG, 'NO Motion detected!')

logger.debug(LOG_TAG, 'Setting up the PIR sensor...')
sensor.wait_for_no_motion()

logger.debug(LOG_TAG, '* Device ready! *')

while True:
    sensor.when_motion = on_motion
    sensor.when_no_motion = no_motion

