# import pytest
# import logging
# from test_assyst.utils import common
# from test_assyst import constants
#
# logger = logging.getLogger('my_logger')
#
#
# @pytest.mark.parametrize("data",["./jsons/create_client.json"])
# @pytest.mark.parametrize("field_values1", common.read_csv("./test_data_regression/Income/test_data_income.csv"))
# @pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_employment.csv"))
# def test_add_client_and_sub_records(field_values1,post_income_superadmin,patch_income_superadmin,create_client_superadmin,get_client_data_superadmin_customer_id,data,field_values,post_client_data_superadmin,patch_employment_data_superadmin,get_client_details_superadmin):
#
#     # add client,post employment, patch employment,view employment
#
#
#     create_client = create_client_superadmin(data, None, True)
#     create_client_response = create_client.json()
#     logger.info(create_client_response)
#     common.check_reponse_message(create_client_response, constants.add_client_success_message)
#     logger.info("Client Details Added Successfully")
#
#     customer_id = create_client_response['data']['customer_id']
#     employment_data = common.read_json("./jsons/create_client_employment.json")
#
#     client_employment = post_client_data_superadmin(customer_id, employment_data, 'employment', True)
#     client_employment_data = client_employment.json()
#     logger.info(client_employment_data)
#     common.check_reponse_message(client_employment_data, constants.add_client_success_message)
#     logger.info("Client employment Added Successfully")
#
#     employment_id = client_employment_data['data']['employment']['employment_id']
#
#     data = {field: field_values.get(field) for field in field_values.keys() if
#             field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     data.popitem()
#     patch_client_data = patch_employment_data_superadmin(customer_id, employment_id, data, 'employment', False)
#     patch_client_data_response = patch_client_data.json()
#     logger.info(patch_client_data_response)
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Employment Updated Successfully")
#
#     get_client_data = get_client_data_superadmin_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
#   #view all clients
#
#
#     get_client_data = get_client_details_superadmin()
#     get_client_response = get_client_data.json()
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info(get_client_response)
#     logger.info("All Client Details Fetched Successfully")
#
# # post, patch ,get income
#
#     post_income = post_income_superadmin(customer_id, data, 'income', True)
#     post_income_response = post_income.json()
#     logger.info(post_income_response)
#     common.check_reponse_message(post_income_response, constants.add_income_success_message)
#     logger.info("Income Details Added Successfully")
#
#     income_id = post_income_response['data']['income_id']
#     values = {field: int(field_values1.get(field)) if (field_values1.get(field).isdigit() and field != 'case_type') else
#     field_values1.get(field) for field in field_values1.keys() if field_values1.get(field) is not None and
#               field_values1.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     values.popitem()
#     update_income_data = patch_income_superadmin(customer_id, income_id, values, 'income', False)
#     update_income_data_response = update_income_data.json()
#     logger.info(update_income_data_response)
#     common.check_reponse_message(update_income_data_response, expected_message)
#     logger.info("Income details Updated Successfully")