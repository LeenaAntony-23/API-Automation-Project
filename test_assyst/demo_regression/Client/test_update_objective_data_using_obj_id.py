import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_objectives.csv"))
def test_add_all_data_to_objectives(customer_id,get_client_data_with_customer_id,data, field_values, create_client, post_client_data,
                                     patch_clientobjectives_data):


    objectives_data = common.read_json("./jsons/create_new_objectives.json")
    client_objectives = post_client_data(customer_id, objectives_data, 'objectives', True)
    client_objectives_data = client_objectives.json()
    logger.info(client_objectives_data)
    common.check_reponse_message(client_objectives_data,constants.add_objective_success_message)
    logger.info("Client Details For Objectives Added Successfully")

    customer_id  = client_objectives_data['data']['objectives']['customer_id']
    objective_id = client_objectives_data['data']['objectives']['objective_id']
    logger.info(customer_id)
    logger.info(objective_id)


    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_objectives_data = patch_clientobjectives_data(customer_id, objective_id, values, 'objectives', None)
    patch_identity_data_response = patch_objectives_data.json()
    logger.info(patch_identity_data_response)
    common.check_reponse_message(patch_identity_data_response, expected_message)
    logger.info("Client Details For Outgoings Updated Successfully")
    logger.info("Update Outgoing Data To Client Test Passed!")

    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")