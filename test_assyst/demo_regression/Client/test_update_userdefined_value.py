import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_user_defined_valid_customer_id(customer_id,get_client_data_with_customer_id,post_system_manager_data,create_client,data,dataa,post_userdefined_value, patch_user_defined_value_data):
    # system manager user defined post
    post_user = post_system_manager_data(dataa, 'user_defined_field', True)
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_success)
    logger.info("User defined Details Added Successfully")

    # create client

    category_id = post_user_response['data']['id']

    post_user = post_userdefined_value(customer_id,category_id,"user_defined_values")
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_value_success)
    logger.info("User defined Details Added Successfully")

    value_id=post_user_response['data'][0]['data']['user_defined_value_id']

    # client user defined value patch
    patch_userdefined_value_data = patch_user_defined_value_data(customer_id,value_id,category_id,
                                                          'user_defined_values')
    patch_userdefined_value_response = patch_userdefined_value_data.json()
    logger.info(patch_userdefined_value_response)
    common.check_reponse_message(patch_userdefined_value_response, constants.patch_client_success_message)
    logger.info("Client Details For User Defined Updated Successfully")
    logger.info("Update User Defined Data To Client Test Passed!")

    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_user_defined_invalid_customer_id(customer_id,post_system_manager_data,create_client,data,dataa,post_userdefined_value, patch_user_defined_value_data):
    # system manager user defined post
    post_user = post_system_manager_data(dataa, 'user_defined_field', True)
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_success)
    logger.info("User defined Details Added Successfully")

    # create client

    category_id = post_user_response['data']['id']

    post_user = post_userdefined_value(customer_id, category_id, "user_defined_values")
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_value_success)
    logger.info("User defined Details Added Successfully")

    value_id = post_user_response['data'][0]['data']['user_defined_value_id']

    # client user defined value patch
    patch_userdefined_value_data = patch_user_defined_value_data("d3bc8293-cc58-4431-aaea-15c251a5a2f3",value_id,category_id,
                                                          'user_defined_values')
    patch_userdefined_value_response = patch_userdefined_value_data.json()
    logger.info(patch_userdefined_value_response)
    message = patch_userdefined_value_response["message"]
    logger.info(message)
    expected_message = constants.invalid_customer_id_message
    logger.info(expected_message)
    assert expected_message == message, f"expected {expected_message}, but actual {message}"
    assert post_user_response[
               'statusCode'] == 200, f"API call failed with StatusCode: {post_user_response['statusCode']}"
    assert post_user_response["isError"] is False, "API call failed ['isError'] should be False"
    logger.info("Customer not found")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_user_defined_invalid_user_defined_value_id(customer_id,post_system_manager_data,create_client,data,dataa,post_userdefined_value, patch_user_defined_value_data):
    # system manager user defined post
    post_user = post_system_manager_data(dataa, 'user_defined_field', True)
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_success)
    logger.info("User defined Details Added Successfully")

    # create client

    category_id = post_user_response['data']['id']
    # customer_id = "00ea8973-0aaf-4ab6-990f-e1d2a2e93f0f"
    # category_id = "0c8ca9d7-ed54-45f7-9a18-cf671dab96a9"

    # client user defined value post
    post_user = post_userdefined_value(customer_id, category_id, "user_defined_values")
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_value_success)
    logger.info("User defined Details Added Successfully")

    value_id = post_user_response['data'][0]['data']['user_defined_value_id']

    # client user defined value patch
    patch_userdefined_value_data = patch_user_defined_value_data(customer_id,"d3bc8293-cc58-4431-aaea-15c251a5a2f3",category_id,
                                                          'user_defined_values')
    patch_userdefined_value_response = patch_userdefined_value_data.json()
    logger.info(patch_userdefined_value_response)
    message = patch_userdefined_value_response["message"]
    logger.info(message)
    expected_message = constants.invalid_userdefined_id_message
    logger.info(expected_message)
    assert expected_message == message, f"expected {expected_message}, but actual {message}"
    assert post_user_response[
               'statusCode'] == 200, f"API call failed with StatusCode: {post_user_response['statusCode']}"
    assert post_user_response["isError"] is False, "API call failed ['isError'] should be False"
    logger.info("Customer not found")

# @pytest.mark.parametrize("data", ["./jsons/create_client.json"])
# @pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
# def test_update_user_defined_invalid_user_defined_field_id(post_system_manager_data,create_client,data,dataa,post_userdefined_value, patch_user_defined_value_data):
#     # # system manager user defined post
#     # post_user = post_system_manager_data(dataa, 'user_defined_field', True)
#     # post_user_response = post_user.json()
#     # logger.info(post_user_response)
#     # common.check_reponse_message(post_user_response, constants.add_user_defined_success)
#     # logger.info("User defined Details Added Successfully")
#
#     # # create client
#     # create_client = create_client(data, None, True)
#     # create_client_response = create_client.json()
#     # common.check_reponse_message(create_client_response, constants.add_client_success_message)
#     # logger.info("Client Details Added Successfully")
#
#     # customer_id = create_client_response['data']['customer_id']
#     # category_id = post_user_response['data']['id']
#     customer_id = "00ea8973-0aaf-4ab6-990f-e1d2a2e93f0f"
#     category_id = "0c8ca9d7-ed54-45f7-9a18-cf671dab96a9"
#
#
#     # client user defined value post
#     post_user = post_userdefined_value(customer_id, category_id, "user_defined_values")
#     post_user_response = post_user.json()
#     logger.info(post_user_response)
#     common.check_reponse_message(post_user_response, constants.add_user_defined_value_success)
#     logger.info("User defined Details Added Successfully")
#
#     value_id = post_user_response['data'][0]['data']['user_defined_value_id']
#
#     category_id = "00ea8973-0aaf-4ab6-990f-e1d2a2e93f0f"
#
#     # client user defined value patch
#     patch_userdefined_value_data = patch_user_defined_value_data(customer_id,value_id,category_id,
#                                                           'user_defined_values')
# #     patch_userdefined_value_response = patch_userdefined_value_data.json()
# #     logger.info(patch_userdefined_value_response)
# #     message = patch_userdefined_value_response["message"]
# #     logger.info(message)
# #     expected_message = constants.invalid_userdefined_id_message
# #     logger.info(expected_message)
# #     assert expected_message == message, f"expected {expected_message}, but actual {message}"
# #     assert post_user_response[
# #                'statusCode'] == 200, f"API call failed with StatusCode: {post_user_response['statusCode']}"
# #     assert post_user_response["isError"] is False, "API call failed ['isError'] should be False"
# #     logger.info("Customer not found")
#
