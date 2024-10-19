import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_commission_type(get_commission_type):

    get_provider_data = get_commission_type()
    get_provider_data_response = get_provider_data.json()
    common.check_reponse_message(get_provider_data_response, constants.get_commission_type_success_message)
    logger.info(get_provider_data_response)


def test_fetch_invalid_context_commission_type(get_invali_context_commission_type):

    get_provider_data = get_invali_context_commission_type()
    get_provider_data_response = get_provider_data.json()
    logger.info(get_provider_data_response)
    expected_message = constants.get_commision_type_invalid_context_message
    message = get_provider_data_response['message']
    assert expected_message == message, f"expected {expected_message}, but actual {message}"
    assert get_provider_data_response['statusCode'] == 404, f"API call failed with StatusCode: {get_provider_data_response['statusCode']}"
    logger.info("Cannot GET /masterdata/commission/commissiont")