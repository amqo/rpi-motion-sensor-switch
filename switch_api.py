import requests
import constants
import logger
from requests.exceptions import HTTPError
import json

LOG_TAG = 'SWITCH API'

# Requests data
url_get = constants.SERVER_URL + '/api/states/' + constants.SWITCH_ID
body_get = {}

url_post = constants.SERVER_URL + '/api/services/switch/turn_on'
body_post = {
    'entity_id': constants.SWITCH_ID
}

headers_call = {
    'Authorization':'Bearer ' + constants.TOKEN,
    'Content-Type':'application/json'
}

def is_switch_off():
    try:
        response = requests.get(url_get, data=json.dumps(body_get), headers=headers_call)
        state = response.json().get('state')
        logger.debug(LOG_TAG, 'switch state: ' + state)
        return state == 'off'
    except HTTPError as http_err:
        logger.error(LOG_TAG, 'HTTP error occurred: ' + http_err)
    except Exception as err:
        logger.error(LOG_TAG, 'Other error occurred: ' + err)

def turn_on_switch():
    try:
        response = requests.post(url_post, data=json.dumps(body_post), headers=headers_call)
        logger.debug(LOG_TAG, 'turn_on_swith result: ' + str(response.content))
    except HTTPError as http_err:
        logger.error(LOG_TAG, 'HTTP error occurred: ' + http_err)
    except Exception as err:
        logger.error(LOG_TAG, 'Other error occurred: ' + err)