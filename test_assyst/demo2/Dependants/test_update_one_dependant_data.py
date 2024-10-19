import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Dependant/test_data_dependant.csv"))
def test_update_dependant_data_with_valid_data(customer_id,data, field_values, create_client, post_dependant_data,
                                               patch_dependant_data,get_dependant_data_with_customer_id):

    post_dependant = post_dependant_data(customer_id, None, 'dependants', True)
    post_dependant_response = post_dependant.json()
    common.check_reponse_message(post_dependant_response, constants.dependant_add_success_message)
    logger.info("Dependant Details Added Successfully")

    dependant_id = post_dependant_response['data']['dependant']['dependant_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_dependant = patch_dependant_data(customer_id,dependant_id, data, 'dependants')
    patch_dependant_response = patch_dependant.json()
    common.check_reponse_message(patch_dependant_response, expected_message)
    logger.info("Dependant Details Updated Successfully")
    logger.info(patch_dependant_response)
    logger.info("Update Data To Dependant Test Passed!")
    dependant_details = get_dependant_data_with_customer_id(customer_id)
    dependant_response = dependant_details.json()
    common.check_reponse_message(dependant_response, constants.get_dependant_success_message)
    logger.info("Dependant Details cFetched Successfully")
