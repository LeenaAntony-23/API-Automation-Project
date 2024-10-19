import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_income_data(customer_id,data, create_client, post_income_data, get_income_with_income_id):

    post_income = post_income_data(customer_id, data, 'income', True)
    post_income_response = post_income.json()
    common.check_reponse_message(post_income_response, constants.add_income_success_message)
    logger.info(post_income_response)
    logger.info(data)
    logger.info("Income Details Added Successfully")

    income_id = post_income_response['data']['income_id']
    get_income = get_income_with_income_id(income_id, customer_id)
    get_income_response = get_income.json()
    common.check_reponse_message(get_income_response, constants.get_income_success_message)
    assert get_income_response["isError"] is False
    logger.info(get_income_response)
    logger.info("Income Details Fetched Successfully")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_income_data_with_invalid_id(customer_id,data, create_client, get_income_with_income_id):

    get_income = get_income_with_income_id('d37fcd87-1881-4798-af93-802fea5027b9', customer_id)
    get_income_response = get_income.json()
    common.check_reponse_message(get_income_response, constants.income_invlaid_message)
    assert get_income_response["isError"] is False
    logger.info("Fetch income Data With Invalid income ID Test Passed!")