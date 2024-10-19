import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contacts_time_allocation.csv"))
def test_update_all_data_to_timeallocation(customer_id,get_timeallocation_data_with_customer_id,data, field_values, create_client, post_client_data,patch_timeallocation_data ):


    timeallocation_data = common.read_json("./jsons/create_new_timeallocation.json")
    client_timeallocation = post_client_data(customer_id, timeallocation_data, 'contacts_time_allocation', True)
    client_timeallocation_data = client_timeallocation.json()
    logger.info(client_timeallocation_data)
    common.check_reponse_message(client_timeallocation_data, constants.add_servicetype_success_message)
    logger.info("Client Details For Time Allocation Added Successfully")

    customer_id = client_timeallocation_data['data']['timeallocation']['customer_id']
    timeallocation_id = client_timeallocation_data['data']['timeallocation']['timeallocation_id']
    logger.info(customer_id)
    logger.info(timeallocation_id)

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_timeallocation_data = patch_timeallocation_data(customer_id, timeallocation_id, values, 'contacts_time_allocation', None)
    patch_timeallocation_response = patch_timeallocation_data.json()
    logger.info(expected_message)
    logger.info(patch_timeallocation_response)
    common.check_reponse_message(patch_timeallocation_response, expected_message)
    logger.info("Client Details For Time Allocation Updated Successfully")
    logger.info("Update Time Allocation Data To Client Test Passed!")

    get_timeallocation_data = get_timeallocation_data_with_customer_id(customer_id)
    get_timeallocation_response = get_timeallocation_data.json()
    logger.info(get_timeallocation_response)
    common.check_reponse_message(get_timeallocation_response, constants.get_client_success_message)
    assert get_timeallocation_response["isError"] is False
    logger.info("Time Allocation Details Fetched Successfully")