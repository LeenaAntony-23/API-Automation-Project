import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_outgoing_data_with_valid_cutomer_id(data, create_client, post_outgoing_data,
                                                   get_outgoing_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_outgoing = post_outgoing_data(customer_id, None, 'outgoings', True)
    post_outgoing_response = post_outgoing.json()
    logger.info(post_outgoing_response)
    common.check_reponse_message(post_outgoing_response, constants.outgoing_add_success_message)
    logger.info("Outgoing Details Added Successfully")

    get_client_data = get_outgoing_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.outgoing_fetch_success_message)
    assert get_client_response["isError"] is False
    logger.info("Outgoing Details Fetched Successfully")
    logger.info("Fetch Outgoing Data Of One Customer Test Passed!")


def test_fetch_outgoing_data_with_invalid_customer_id(get_outgoing_data_with_customer_id):
    get_client_data = get_outgoing_data_with_customer_id('d37fcd87-1881-4798-af93-802fea5027b9')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Outgoing Data With Invalid Customer ID Test Passed!")
