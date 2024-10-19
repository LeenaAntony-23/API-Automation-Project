import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Expense/test_data_expense.csv"))
def test_update_data_to_outgoing(data, field_values, create_client, post_outgoing_data,patch_outgoing_data,get_outgoing_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_outgoing = post_outgoing_data(customer_id, None, 'outgoings', True)
    post_outgoing_response = post_outgoing.json()
    logger.info(post_outgoing_response)
    common.check_reponse_message(post_outgoing_response, constants.outgoing_add_success_message)
    logger.info("Outgoing Details Added Successfully")

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}

    patch_expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()

    expense_id = post_outgoing_response['data']['expense_id']

    patch_outgoing_data = patch_outgoing_data(customer_id, expense_id, data, 'outgoings', False)
    patch_outgoing_data_response = patch_outgoing_data.json()
    logger.info(patch_outgoing_data_response)
    common.check_reponse_message(patch_outgoing_data_response, patch_expected_message)
    logger.info("Client Details For Outgoings Updated Successfully")
    logger.info("Update Outgoing Data To Client Test Passed!")

    get_client_data = get_outgoing_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.outgoing_fetch_success_message)
    assert get_client_response["isError"] is False
    logger.info("Outgoing Details Fetched Successfully")