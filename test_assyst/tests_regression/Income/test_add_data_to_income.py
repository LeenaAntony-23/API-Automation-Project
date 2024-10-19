import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Income/test_data_income.csv"))
def test_add_all_data_to_income(data, field_values, create_client, post_income_data,get_income_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_income = post_income_data(customer_id, data, 'income', False)
    post_income_response = post_income.json()
    common.check_reponse_message(post_income_response, expected_message)
    logger.info("Income Details Added Successfully")
    logger.info(post_income_response)
    logger.info("Add Data To Income Test Passed!")

    get_income_details = get_income_data_with_customer_id(customer_id)
    get_income_response = get_income_details.json()
    common.check_reponse_message(get_income_response, constants.get_income_success_message)
    assert get_income_response["isError"] is False
    logger.info("Income Details Fetched Successfully")
