import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_customer_data_with_valid_customer_id(data, create_client,post_partner_data, get_client_data_with_partner_customer_id):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    # logger.info("customer id")
    # logger.info(customer_id)
    # logger.info("partner id")
    # logger.info(partner_cust_id)

    get_client_data = get_client_data_with_partner_customer_id(partner_cust_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Partner Details Fetched Successfully")
    logger.info(get_client_response)
    logger.info("Fetch One Partner Data Test Passed!")


def test_fetch_one_customer_data_with_invalid_customer_id(get_client_data_with_partner_customer_id):
    get_client_data = get_client_data_with_partner_customer_id('e34960f1-ce23-4985-a5df-d497193be3ab')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_partner_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Partner customer ID Test Passed!")
