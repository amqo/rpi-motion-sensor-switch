import datetime
import logger
import sys


LOG_TAG = 'TIME API'

def time_in_range(start, end):
    now = datetime.datetime.now()
    logger.debug(LOG_TAG, 'Current datetime: ' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    now_time = datetime.time(now.hour, now.minute, now.second)
    
    if start <= end:
        return start <= now_time <= end
    else:
        return start <= now_time or now_time <= end