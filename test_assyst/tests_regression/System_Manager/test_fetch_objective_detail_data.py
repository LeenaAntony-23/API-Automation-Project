import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_objective_detail_data(get_objective_details):

    get_objective_details_data = get_objective_details()
    get_objective_details_response = get_objective_details_data.json()
    common.check_reponse_message(get_objective_details_response, constants.get_objective_detail_success_message)
    logger.info(get_objective_details_response)
    logger.info("Objective details listed successfully")