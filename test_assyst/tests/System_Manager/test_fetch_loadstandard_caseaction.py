import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_all_loard_standard_caseaction_data(get_load_standard_caseaction_details):

    get_loard_standard_caseaction_data = get_load_standard_caseaction_details()
    get_loard_standard_caseaction_response = get_loard_standard_caseaction_data.json()
    common.check_reponse_message(get_loard_standard_caseaction_response, constants.get_load_standard_case_action_success_message)
    logger.info(get_loard_standard_caseaction_response)
    logger.info("Load standard action for case listed successfully")