import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


def test_fetch_all_client_data(get_client_details):

    get_client_data = get_client_details()
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info(get_client_response)
    logger.info("All Client Details Fetched Successfully")