import pytest
import logging
import time
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
# @pytest.mark.parametrize("field_values12", common.read_csv("./test_data_regression/Client/test_data_compliance.csv"))
# @pytest.mark.parametrize("field_values11", common.read_csv("./test_data_regression/Client/test_data_administration.csv"))
# @pytest.mark.parametrize("field_values10", common.read_csv("./test_data_regression/Client/test_data_health_note.csv"))
# @pytest.mark.parametrize("field_values9", common.read_csv("./test_data_regression/Client/test_data_contact.csv"))
# @pytest.mark.parametrize("field_values8", common.read_csv("./test_data_regression/Client/test_data_nationality.csv"))
# @pytest.mark.parametrize("field_values7", common.read_csv("./test_data_regression/Client/test_data_personal.csv"))
# @pytest.mark.parametrize("field_values6", common.read_csv("./test_data_regression/Client/test_data_vulnerability.csv"))
# @pytest.mark.parametrize("field_values5", common.read_csv("./test_data_regression/Client/test_data_objectives.csv"))
# @pytest.mark.parametrize("field_values4", common.read_csv("./test_data_regression/Client/test_data_service_type.csv"))
# @pytest.mark.parametrize("field_values2", common.read_csv("./test_data_regression/Client/test_data_employment.csv"))
# @pytest.mark.parametrize("field_values1", common.read_csv("./test_data_regression/Client/test_data_name_and_address.csv"))
# @pytest.mark.parametrize("field_values3", common.read_csv("./test_data_regression/Client/test_data_identity.csv"))
# @pytest.mark.parametrize("run", range(1, 2))  # Run the test 100 times
def test_add_data_to_client( create_client,data):
#NAME AND ADDRESS
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    #customer_id = create_client_response['data']['customer_id']
#
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
#
#     data = {field: field_values1.get(field) for field in field_values1.keys() if
#             field_values1.get(field) is not None and field_values1.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     data.popitem()
#     patch_client_data = patch_client_data(customer_id, data, 'name_and_address', None)
#     patch_client_data_response = patch_client_data.json()
#     logger.info(patch_client_data_response)
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Details For Name And Address Updated Successfully")
#     #time.sleep(5)
#
#
# #EMPLOYMENT
#     employment_data = common.read_json("./jsons/create_client_employment.json")
#     client_employment = post_client_data(customer_id, employment_data, 'employment', True)
#     client_employment_data = client_employment.json()
#     logger.info(client_employment_data)
#     common.check_reponse_message(client_employment_data, constants.add_client_success_message)
#     logger.info("Client employment Added Successfully")
#
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response,constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
#
#     employment_id = client_employment_data['data']['employment']['employment_id']
#     data = {field: field_values2.get(field) for field in field_values2.keys() if
#             field_values2.get(field) is not None and field_values2.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     data.popitem()
#     patch_client_data = patch_employment_data(customer_id, employment_id, data, 'employment', False)
#     patch_client_data_response = patch_client_data.json()
#     logger.info(patch_client_data_response)
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Employment Updated Successfully")
#
#
#
# #IDENTITY
#     identity_data = common.read_json("./jsons/create_new_identity.json")
#     client_identity = post_client_data(customer_id, identity_data, 'identity', True)
#     client_identity_data = client_identity.json()
#     logger.info(client_identity_data)
#     common.check_reponse_message(client_identity_data, constants.add_identity_success_message)
#     logger.info("Client Details For identity Added Successfully")
#
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
#
#     identity_id = client_identity_data['data']['identity']['identity_id']
#
#     values = {field: int(field_values3.get(field)) if field_values3.get(field).isdigit() else field_values3.get(field)
#      for field in field_values3.keys() if field_values3.get(field) is not None and field_values3.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     values.popitem()
#     patch_identity_data = patch_clientidentity_data(customer_id, identity_id, values, 'identity', None)
#     patch_identity_data_response = patch_identity_data.json()
#     logger.info(patch_identity_data_response)
#     common.check_reponse_message(patch_identity_data_response,expected_message)
#     logger.info("Client Details For Identity Updated Successfully")
#
#
#
# #SERVICE TYPE
#     servicetype_data = common.read_json("./jsons/create_new_servicetype.json")
#     client_servicetype = post_client_data(customer_id, servicetype_data, 'service_type', True)
#     client_servicetype_data = client_servicetype.json()
#     logger.info(client_servicetype_data)
#     common.check_reponse_message(client_servicetype_data, constants.add_servicetype_success_message)
#     logger.info("Client Details For Service Type Added Successfully")
#
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
#
#     servicetype_id = client_servicetype_data['data']['servicetype']['servicetype_id']
#
#     values = {field: int(field_values4.get(field)) if field_values4.get(field).isdigit() else field_values4.get(field)
#               for field in field_values4.keys() if field_values4.get(field) is not None and field_values4.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     values.popitem()
#     patch_client_data = patch_clientservicetype_data(customer_id, servicetype_id, values, 'service_type', None)
#     patch_client_data_response = patch_client_data.json()
#     logger.info(expected_message)
#     logger.info(patch_client_data_response)
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Details For Service Type Updated Successfully")
#
# #objective
#     objectives_data = common.read_json("./jsons/create_new_objectives.json")
#     client_objectives = post_client_data(customer_id, objectives_data, 'objectives', True)
#     client_objectives_data = client_objectives.json()
#     logger.info(client_objectives_data)
#     common.check_reponse_message(client_objectives_data,constants.add_objective_success_message)
#     logger.info("Client Details For Objectives Added Successfully")
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
#
#
#     objective_id = client_objectives_data['data']['objectives']['objective_id']
#     values = {field: int(field_values5.get(field)) if field_values5.get(field).isdigit() else field_values5.get(field)
#               for field in field_values5.keys() if field_values5.get(field) is not None and field_values5.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     values.popitem()
#     patch_objectives_data = patch_clientobjectives_data(customer_id, objective_id, values, 'objectives', None)
#     patch_identity_data_response = patch_objectives_data.json()
#     logger.info(patch_identity_data_response)
#     common.check_reponse_message(patch_identity_data_response, expected_message)
#     logger.info("Client Details For Outgoings Updated Successfully")
#
# #vulnerability
#     # vulnerability_data = common.read_json("./jsons/create_client_contexts.json")
#     # #logger.info(vulnerability_data)
#     # client_vulnerability = post_vulnerability_data(customer_id, vulnerability_data, 'vulnerability', True)
#     # client_vulnerability_data = client_vulnerability.json()
#     # logger.info(client_vulnerability_data)
#     # common.check_reponse_message(client_vulnerability_data, constants.add_vulnerability_success_message)
#     # logger.info("Client vulnerability Added Successfully")
#     #
#     # get_vulnerability_customer_id = get_vulnerability_using_customer_id(customer_id)
#     # get_vulnerability_customer_id_response = get_vulnerability_customer_id.json()
#     # common.check_reponse_message(get_vulnerability_customer_id_response, constants.get_vulnerability_success_message)
#     # logger.info(get_vulnerability_customer_id_response)
#     # logger.info("Vulnerability using customer id for Health driver Details Fetched Successfully")
#     #
#     # vulnerability_id = client_vulnerability_data['data'][0]['vulnerability_id']
#     # logger.info(vulnerability_id)
#     # data = {field: field_values6.get(field) for field in field_values6.keys() if
#     #         field_values6.get(field) is not None and field_values6.get(field) != ''}
#     # expected_message = data.get(list(data)[-1])
#     # data.popitem()
#     # data.popitem()
#     # patch_client_data = patch_vulnerability_data(customer_id, vulnerability_id, data, 'vulnerability', False)
#     # patch_client_data_response = patch_client_data.json()
#     # logger.info(patch_client_data_response)
#     # common.check_reponse_message(patch_client_data_response, expected_message)
#     # logger.info("Client Vulnerability Updated Successfully")
#
# #personal
#
#     data = {field: field_values7.get(field) for field in field_values7.keys() if
#             field_values7.get(field) is not None and field_values7.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     #data.popitem()
#     patch_client_data = patch_client_data(customer_id, data, 'personal', None)
#     patch_client_data_response = patch_client_data.json()
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Details For Personal Updated Successfully")
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
# #nationality
#
#     data = {field: field_values8.get(field) for field in field_values8.keys() if
#             field_values8.get(field) is not None and field_values8.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     #data.popitem()
#     patch_client_datas = patch_client_data(customer_id, data, 'nationality', None)
#     patch_client_data_response = patch_client_datas.json()
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Details For Nationality Updated Successfully")
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
# #contact
#     data = {field: field_values9.get(field) for field in field_values9.keys() if
#             field_values9.get(field) is not None and field_values9.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     #data.popitem()
#     patch_client_data = patch_client_data(customer_id, data, 'contact', None)
#     patch_client_data_response = patch_client_data.json()
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Details For Contact Updated Successfully")
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
# #health
#
#     data = {field: field_values10.get(field) for field in field_values10.keys() if
#             field_values10.get(field) is not None and field_values10.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     #data.popitem()
#     patch_client_data = patch_client_data(customer_id, data, 'health_note', None)
#     patch_client_data_response = patch_client_data.json()
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Details For Health Note Updated Successfully")
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
# #admn
#
#     data = {field: field_values11.get(field) for field in field_values11.keys() if
#             field_values11.get(field) is not None and field_values11.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     #data.popitem()
#     patch_client_data = patch_client_data(customer_id, data, 'administration', None)
#     patch_client_data_response = patch_client_data.json()
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Details For Administration Updated Successfully")
#
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
#
# #compliance
#
#     data = {field: field_values12.get(field) for field in field_values12.keys() if
#             field_values12.get(field) is not None and field_values12.get(field) != ''}
#     expected_message = data.get(list(data)[-1])
#     data.popitem()
#     #data.popitem()
#     patch_client_data = patch_client_data(customer_id, data, 'compliance', None)
#     patch_client_data_response = patch_client_data.json()
#     common.check_reponse_message(patch_client_data_response, expected_message)
#     logger.info("Client Details For Compliance Updated Successfully")
#
#     logger.info("Update Compliance Data To Client Test Passed!")
#     get_client_data = get_client_data_with_customer_id(customer_id)
#     get_client_response = get_client_data.json()
#     logger.info(get_client_response)
#     common.check_reponse_message(get_client_response, constants.get_client_success_message)
#     logger.info("Client Details Fetched Successfully")
