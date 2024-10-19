import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_all_attitude_rating_data(get_attitude_rating_details):

    get_attitude_rating_data = get_attitude_rating_details()
    get_attitude_rating_response = get_attitude_rating_data.json()
    common.check_reponse_message(get_attitude_rating_response, constants.get_attitude_rating_success_message)
    logger.info(get_attitude_rating_response)
    logger.info("Attitude rating details listed successfully")