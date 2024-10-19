import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_customer_data_with_valid_customer_id(customer_id,data, create_client, get_client_data_with_customer_id):


    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
    logger.info(get_client_response)
    #common.compare_dicts(create_client_response['data'], get_client_response['data']['NameAndAddress'])
    logger.info("Fetch One Customer Data Test Passed!")


def test_fetch_one_customer_data_with_invalid_customer_id(get_client_data_with_customer_id):
    get_client_data = get_client_data_with_customer_id('e34960f1-ce23-4985-a5df-d497193be3ab')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Customer ID Test Passed!")
