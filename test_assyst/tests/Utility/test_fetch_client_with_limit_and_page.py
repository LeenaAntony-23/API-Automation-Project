import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


def test_fetch_all_client(get_client_data):

    get_client_info = get_client_data()
    get_client_response = get_client_info.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info(get_client_response)
    logger.info("All Client Details Fetched Successfully")

def test_fetch_all_client_invalid_url(get_client_data_with_invalid_url):

    get_client_info = get_client_data_with_invalid_url()
    get_client_response = get_client_info.json()
    logger.info(get_client_response)

    logger.info("Invalid URL Test Passed")