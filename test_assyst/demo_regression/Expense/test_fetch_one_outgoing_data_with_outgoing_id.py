import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_outgoing_data_with_outgoing_id(customer_id,data, create_client, post_outgoing_data,
                                                  get_outgoing_data_with_outgoing_id):

    create_outgoing = post_outgoing_data(customer_id, None, 'outgoings', True)
    post_outgoing_response = create_outgoing.json()
    logger.info(post_outgoing_response)
    common.check_reponse_message(post_outgoing_response, constants.outgoing_add_success_message)
    logger.info("Outgoing Details Added Successfully")

    expense_id = post_outgoing_response['data']['expense_id']
    get_outgoing = get_outgoing_data_with_outgoing_id(expense_id,customer_id)
    get_outgoing_response = get_outgoing.json()
    logger.info(get_outgoing_response)
    common.check_reponse_message(get_outgoing_response, constants.get_outgoing_success_message)
    logger.info("Outgoing Details Fetched Successfully")

    logger.info("Fetch Outgoing Data Of One Customer Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_outgoing_data_with_invalid_id(customer_id,data,create_client,get_outgoing_data_with_outgoing_id):

    get_outgoing_data = get_outgoing_data_with_outgoing_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0',customer_id)
    get_outgoing_response = get_outgoing_data.json()
    common.check_reponse_message(get_outgoing_response, constants.get_outgoing_invalid_message)
    assert get_outgoing_response["isError"] is False
    logger.info("Fetch Outgoing Data With Invalid ID Test Passed!")
