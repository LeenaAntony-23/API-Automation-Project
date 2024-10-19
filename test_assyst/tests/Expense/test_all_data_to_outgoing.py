import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Expense/test_data_expense.csv"))
def test_add_data_to_outgoing(data, field_values, create_client, post_outgoing_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    # data = {field: field_values.get(field) for field in field_values.keys() if
    #         field_values.get(field) is not None and field_values.get(field) != ''}
    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_outgoing = post_outgoing_data(customer_id, data, 'outgoings', False)
    post_outgoing_response = post_outgoing.json()
    common.check_reponse_message(post_outgoing_response, expected_message)
    logger.info("Outgoing Details Added Successfully")

    logger.info("Add Data To Outgoing Test Passed!")
