import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_standard_caseaction_data(get_standard_caseaction_details):

    get_loard_standard_clientaction_data = get_standard_caseaction_details()
    get_loard_standard_clientaction_response = get_loard_standard_clientaction_data.json()
    common.check_reponse_message(get_loard_standard_clientaction_response, constants.get_standard_case_action_success_message)
    logger.info(get_loard_standard_clientaction_response)
    logger.info("Load standard action for client listed successfully")