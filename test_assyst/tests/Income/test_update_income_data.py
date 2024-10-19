import pytest
import logging
from test_assyst import constants
from test_assyst.conftest import patch_income_data
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Income/test_data_income.csv"))
def test_create_and_fetch_income_data(data, create_client,field_values, post_income_data,patch_income_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_income = post_income_data(customer_id, data, 'income', True)
    post_income_response = post_income.json()
    logger.info(post_income_response)
    common.check_reponse_message(post_income_response, constants.add_income_success_message)
    logger.info("Income Details Added Successfully")

    income_id = post_income_response['data']['income_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_income_data = patch_income_data(customer_id, income_id, values, 'income', False)
    update_income_data_response = update_income_data.json()
    logger.info(update_income_data_response)
    common.check_reponse_message(update_income_data_response, expected_message)
    logger.info("Income details Updated Successfully")

    logger.info("Update Income details Test Passed!")