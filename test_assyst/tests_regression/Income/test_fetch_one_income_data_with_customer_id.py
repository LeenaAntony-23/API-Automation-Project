import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_income_data(data, create_client, post_income_data, get_income_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_income = post_income_data(customer_id, data, 'income', True)
    post_income_response = post_income.json()
    common.check_reponse_message(post_income_response, constants.add_income_success_message)
    logger.info("Income Details Added Successfully")

    get_income_details = get_income_data_with_customer_id(customer_id)
    get_income_response = get_income_details.json()
    common.check_reponse_message(get_income_response, constants.get_income_success_message)
    assert get_income_response["isError"] is False
    logger.info("Income Details Fetched Successfully")

    logger.info("Fetch Income Data Of One Customer Test Passed!")


def test_fetch_details_with_invalid_customer_id(get_income_data_with_customer_id):
    get_client_data = get_income_data_with_customer_id('d37fcd87-1881-4798-af93-802fea5027b9')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Income Data With Invalid Customer ID Test Passed!")
