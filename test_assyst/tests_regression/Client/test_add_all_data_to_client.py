import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

#
# @pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_name_and_address.csv"))
# #@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
# def test_add_all_data_to_name_address(field_values, create_client, get_client_data_with_customer_id):
#
#     data = {field: field_values.get(field) for field in field_values.keys() if
#             field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = data.get(list(data)[-2])
#     data.popitem()
#     data.popitem()
#     client_name_addres = create_client(data, 'name_and_address', False)
#     client_name_addres_data = client_name_addres.json()
#     #common.check_reponse_message(client_name_addres_data, constants.add_client_success_message)
#     common.check_reponse_message(client_name_addres_data,expected_message )
#     logger.info("Client Details For Name And Address Added Successfully")
#     logger.info(client_name_addres_data)
#     logger.info("Add NameAndAddress With Valid Data Test Passed!")
#
#
# @pytest.mark.parametrize("data", ["./jsons/create_client.json"])
# @pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_employment.csv"))
# def test_add_all_data_to_employment(data, field_values, create_client, post_client_data,
#                                      get_client_data_with_customer_id):
#     create_client = create_client(data, None, True)
#     create_client_response = create_client.json()
#     logger.info(create_client_response)
#     common.check_reponse_message(create_client_response, constants.add_client_success_message)
#     logger.info("Client Details Added Successfully")
#
#     customer_id = create_client_response['data']['customer_id']
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-2])
#     values.popitem()
#     values.popitem()
#     client_employment = post_client_data(customer_id, values, 'employment', False)
#     client_employment_data = client_employment.json()
#     logger.info(client_employment_data)
#     common.check_reponse_message(client_employment_data, expected_message)
#     logger.info("Client Details For Employment Added Successfully")
#
#
#     logger.info("Add Employment Data Test Passed!")
#
#
# @pytest.mark.parametrize("data", ["./jsons/create_client.json"])
# @pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_identity.csv"))
# def test_add_all_data_to_identity(data, field_values, create_client, post_client_data,
#                                      get_client_data_with_customer_id):
#     create_client = create_client(data, None, True)
#     create_client_response = create_client.json()
#     logger.info(create_client_response)
#     common.check_reponse_message(create_client_response, constants.add_client_success_message)
#     logger.info("Client Details Added Successfully")
#
#     customer_id = create_client_response['data']['customer_id']
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-2])
#     values.popitem()
#     values.popitem()
#     client_identity = post_client_data(customer_id, values, 'identity', False)
#     client_identity_data = client_identity.json()
#     logger.info(client_identity_data)
#     common.check_reponse_message(client_identity_data, expected_message)
#     logger.info("Client Details For Identity Added Successfully")
#
#
#
#
# @pytest.mark.parametrize("data", ["./jsons/create_client.json"])
# @pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_objectives.csv"))
# def test_add_all_data_to_objectives(data, field_values, create_client, post_client_data,
#                                      get_client_data_with_customer_id):
#     create_client = create_client(data, None, True)
#     create_client_response = create_client.json()
#     logger.info(create_client_response)
#     common.check_reponse_message(create_client_response, constants.add_client_success_message)
#     logger.info("Client Details Added Successfully")
#
#     customer_id = create_client_response['data']['customer_id']
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-2])
#     values.popitem()
#     values.popitem()
#     client_objectives = post_client_data(customer_id, values, 'objectives', False)
#     client_objectives_data = client_objectives.json()
#     logger.info(client_objectives_data)
#     common.check_reponse_message(client_objectives_data, expected_message)
#
#     logger.info("Client Details For Objectives Added Successfully")
#
#
#     logger.info("Add Objectives Data Test Passed!")
#
#
# @pytest.mark.parametrize("data", ["./jsons/create_client.json"])
# @pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_service_type.csv"))
# def test_add_all_data_to_servicetype(data, field_values, create_client, post_client_data,
#                                      get_client_data_with_customer_id):
#     create_client = create_client(data, None, True)
#     create_client_response = create_client.json()
#     logger.info(create_client_response)
#     common.check_reponse_message(create_client_response, constants.add_client_success_message)
#     logger.info("Client Details Added Successfully")
#
#     customer_id = create_client_response['data']['customer_id']
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-2])
#     values.popitem()
#     values.popitem()
#     client_servicetype = post_client_data(customer_id, values, 'service_type', False)
#     client_servicetype_data = client_servicetype.json()
#     logger.info(client_servicetype_data)
#     common.check_reponse_message(client_servicetype_data, expected_message)
#     logger.info("Client Details For Service Type Added Successfully")
#
#
#     logger.info("Add Servicetype Data Test Passed!")



@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_vulnerability.csv"))
def test_add_all_data_to_vulnerability(data, field_values, create_client, post_vulnerability_data,
                                      get_client_data_with_customer_id,get_vulnerability_using_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_vulnarability = post_vulnerability_data(customer_id, values, 'vulnerability', False)
    client_vulnarability_data = client_vulnarability.json()
    logger.info(client_vulnarability_data)
    common.check_reponse_message(client_vulnarability_data, expected_message)
    logger.info("Client Details For Vulnerability Added Successfully")


#get corresponding driver details


    get_vulnerability_customer_id = get_vulnerability_using_customer_id(customer_id)
    get_vulnerability_customer_id_response = get_vulnerability_customer_id.json()
    common.check_reponse_message(get_vulnerability_customer_id_response, constants.get_vulnerability_success_message)
    logger.info(get_vulnerability_customer_id_response)
    logger.info("Vulnerability using customer id for Driver Details Fetched Successfully")

    logger.info("Add vulnerability Data Test Passed!")

