import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


def test_fetch_all_user_defined_data(get_userdefined_details):

    get_client_action_details_data = get_userdefined_details()
    get_client_action_details_response = get_client_action_details_data.json()
    common.check_reponse_message(get_client_action_details_response, constants.get_user_defined_success_message)
    logger.info(get_client_action_details_response)
    logger.info("All User defined Field Details Fetched Successfully")