import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_dependant_data(data, create_client, post_dependant_data, get_dependant_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_dependant = post_dependant_data(customer_id, None,'dependants', True)
    post_dependant_response = post_dependant.json()
    common.check_reponse_message(post_dependant_response, constants.dependant_add_success_message)
    logger.info("Dependant Details Added Successfully")

    dependant_details = get_dependant_data_with_customer_id(customer_id)
    dependant_response = dependant_details.json()
    common.check_reponse_message(dependant_response, constants.get_dependant_success_message)
    logger.info("Dependant Details cFetched Successfully")
    logger.info(dependant_response)
    logger.info("Fetch Dependant Data Of One Customer Test Passed!")


def test_fetch_details_with_invalid_customer_id(get_dependant_data_with_customer_id):
    get_client_data = get_dependant_data_with_customer_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.registration_failed_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Dependant Data With Invalid Customer ID Test Passed!")
