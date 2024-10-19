import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_data_to_user_defined(get_userdefined_value_data_with_customer_id, post_system_manager_data,create_client,data,dataa,post_userdefined_value):
    post_user = post_system_manager_data(dataa, 'user_defined_field', True)
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_success)
    logger.info("User defined Details Added Successfully")

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    category_id = post_user_response['data']['id']

    post_user = post_userdefined_value(customer_id,category_id,"user_defined_values")
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_value_success)
    logger.info("User defined Details Added Successfully")

    get_userdefined_value_data = get_userdefined_value_data_with_customer_id(customer_id)
    get_userdefined_value_response = get_userdefined_value_data.json()
    logger.info(get_userdefined_value_response)
    common.check_reponse_message(get_userdefined_value_response, constants.customer_success_message)
    assert get_userdefined_value_response["isError"] is False
    logger.info("UserDefined value Details Fetched Successfully")


def test_fetch_userdefined_value_with_invalid_customer_id(get_userdefined_value_data_with_customer_id):
    get_client_data = get_userdefined_value_data_with_customer_id('0006f028-ea52-4eec-94d8-e995e1c80ffc')
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.get_userdefined_value_invalid_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Notes Data With Invalid Customer ID Test Passed!")

