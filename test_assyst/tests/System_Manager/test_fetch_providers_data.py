import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_providers_data(get_providers_details):

    get_provider_data = get_providers_details()
    get_provider_data_response = get_provider_data.json()
    common.check_reponse_message(get_provider_data_response, constants.get_providers_success_message)
    logger.info(get_provider_data_response)
    logger.info("Provider details listed successfully")