import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])

def test_add_data_to_user_defined( customer_id,post_system_manager_data,create_client,data,dataa,post_userdefined_value):
    post_user = post_system_manager_data(dataa, 'user_defined_field', True)
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_success)
    logger.info("User defined Details Added Successfully")


    category_id = post_user_response['data']['id']

    post_user = post_userdefined_value(customer_id,category_id,"user_defined_values")
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_value_success)
    logger.info("User defined Details Added Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_add_data_to_user_defined_invalid_customerid( post_system_manager_data,create_client,data,dataa,post_userdefined_invalid_customer_id):
    post_user = post_system_manager_data(dataa, 'user_defined_field', True)
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_success)
    logger.info("User defined Details Added Successfully")


    category_id = post_user_response['data']['id']

    post_user = post_userdefined_invalid_customer_id("d3bc8293-cc58-4431-aaea-15c251a5a2f3",category_id,"user_defined_values")
    post_user_response = post_user.json()
    message = post_user_response["data"][0]["message"]
    logger.info(message)
    expected_message = constants.invalid_customer_id_message
    logger.info(expected_message)
    assert expected_message == message, f"expected {expected_message}, but actual { message}"
    assert post_user_response['statusCode'] == 200, f"API call failed with StatusCode: {post_user_response['statusCode']}"
    assert post_user_response["isError"] is False, "API call failed ['isError'] should be False"

    logger.info("Customer not found")



@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_add_data_to_user_defined_invalid_userfield_id(customer_id,post_system_manager_data, create_client, data, dataa,
                                                            post_userdefined_invalid_customer_id):





        post_user = post_userdefined_invalid_customer_id(customer_id, "a38aa7e0-2b6f-414e-9cb6-4ab708d20bac",
                                                         "user_defined_values")
        post_user_response = post_user.json()
        logger.info(post_user_response)
        message = post_user_response["data"][0]["message"]
        logger.info(message)
        expected_message = constants.invalid_userdefined_id_message
        logger.info(expected_message)
        assert expected_message == message, f"expected {expected_message}, but actual {message}"
        assert post_user_response[
                   'statusCode'] == 200, f"API call failed with StatusCode: {post_user_response['statusCode']}"
        assert post_user_response["isError"] is False, "API call failed ['isError'] should be False"

        logger.info("Userdefined field  not found")




