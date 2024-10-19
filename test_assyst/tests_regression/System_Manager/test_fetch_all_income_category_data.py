import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_all_income_category_data(get_income_details):

    get_income_data = get_income_details()
    get_income_response = get_income_data.json()
    common.check_reponse_message(get_income_response, constants.get_income_category_success_message)
    logger.info(get_income_response)
    logger.info("All Client Details Fetched Successfully")