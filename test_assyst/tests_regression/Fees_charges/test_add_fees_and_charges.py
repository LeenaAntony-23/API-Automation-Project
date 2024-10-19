import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_fees_charges.csv"))
def test_add_all_data_to_fees_charges(data, field_values, create_client, post_client_data,
                                     get_client_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_contact_fee = post_client_data(customer_id, values, 'fees_charges', False)
    client_contact_fee_data = client_contact_fee.json()
    logger.info(client_contact_fee_data)
    common.check_reponse_message(client_contact_fee_data, expected_message)
    logger.info("Client Details For Fees And Charged Added Successfully")


    logger.info("Add Fees Charges Data Test Passed!")

