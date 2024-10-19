import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_name_and_address_partner_trail.csv"))
def test_add_all_data_to_name_address(data, field_values, create_client, post_partner_data):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info(create_client_response)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    partner_name_addres = post_partner_data(customer_id, values, 'name_and_address', False)
    partner_name_addres_data = partner_name_addres.json()
    common.check_reponse_message(partner_name_addres_data, expected_message)
    logger.info("Partner Details For Name And Address Added Successfully")

    logger.info("Add NameAndAddress Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_employment.csv"))
def test_add_all_data_to_employment(data, field_values, create_client, post_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    logger.info(customer_id)
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    partner_employment = post_client_data(partner_cust_id, values, 'employment', False)
    partner_employment_data = partner_employment.json()
    logger.info(partner_employment_data)
    common.check_reponse_message(partner_employment_data, expected_message)
    logger.info("Partner Details For Employment Added Successfully")

    logger.info("Add Employment Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_identity.csv"))
def test_add_all_data_to_identity(data, field_values, create_client, post_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    partner_identity = post_client_data(partner_cust_id, values, 'identity', False)
    partner_identity_data = partner_identity.json()
    common.check_reponse_message(partner_identity_data, expected_message)
    logger.info("Partner Details For Identity Added Successfully")

    logger.info("Add Identity Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_objectives.csv"))
def test_add_all_data_to_objectives(data, field_values, create_client, post_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    partner_objectives = post_client_data(partner_cust_id, values, 'objectives', False)
    partner_objectives_data = partner_objectives.json()
    common.check_reponse_message(partner_objectives_data, expected_message)
    logger.info("Partner Details For Objectives Added Successfully")

    logger.info("Add Objectives Data Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_service_type.csv"))
def test_add_all_data_to_servicetype(data, field_values, create_client, post_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_servicetype = post_client_data(partner_cust_id, values, 'service_type', False)
    client_servicetype_data = client_servicetype.json()
    common.check_reponse_message(client_servicetype_data, expected_message)
    logger.info("Partner Details For Service Type Added Successfully")

    logger.info("Add Servicetype Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_vulnerability.csv"))
def test_add_all_data_to_vulnerability(data, field_values, create_client,post_vulnerability_data, post_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()

    client_vulnarability = post_vulnerability_data(partner_cust_id, values, 'vulnerability', False)
    client_vulnarability_data = client_vulnarability.json()
    # logger.info(client_vulnarability_data)
    common.check_reponse_message(client_vulnarability_data, expected_message)
    logger.info("Client Details For Vulnerability Added Successfully")