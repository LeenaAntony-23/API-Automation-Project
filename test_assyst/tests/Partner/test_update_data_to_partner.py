import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_name_and_address.csv"))
def test_update_partner_name_address_data(data, field_values, create_client, patch_client_data, post_partner_data):
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
    expected_message = values.get(list(values)[-1])
    values.popitem()
    patch_client_data = patch_client_data(partner_cust_id, values, 'name_and_address', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Partner Details For Name And Address Updated Successfully")

    logger.info("Update Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_contact.csv"))
def test_update_partner_contact_data(data, field_values, create_client, patch_client_data, post_partner_data):
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
    expected_message = values.get(list(values)[-1])
    values.popitem()
    partner_contact = patch_client_data(partner_cust_id, values, 'contact', False)
    partner_contact_data = partner_contact.json()
    logger.info(partner_contact_data)
    common.check_reponse_message(partner_contact_data, expected_message)
    logger.info("Partner Details For Contact Added Successfully")

    logger.info("Update Contact Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_nationality.csv"))
def test_update_partner_nationality_data(data, field_values, create_client, post_partner_data, patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    # values.popitem()
    logger.info(values)
    partner_nationality = patch_client_data(partner_cust_id, values, 'nationality', False)
    partner_nationality_data = partner_nationality.json()
    logger.info(partner_nationality_data)
    common.check_reponse_message(partner_nationality_data, expected_message)
    logger.info("Partner Details For Nationality Added Successfully")

    logger.info("Update Nationality Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_personal.csv"))
def test_update_partner_personal_data(data, field_values, create_client, patch_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    partner_personal = patch_client_data(partner_cust_id, values, 'personal', False)
    partner_personal_data = partner_personal.json()
    common.check_reponse_message(partner_personal_data, expected_message)
    logger.info("Partner Details For Personal Added Successfully")

    logger.info("Update Personal Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_health_note.csv"))
def test_update_partner_health_note_data(data, field_values, create_client, patch_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    partner_health = patch_client_data(partner_cust_id, values, 'health_note', False)
    partner_health_data = partner_health.json()
    logger.info(partner_health_data)
    common.check_reponse_message(partner_health_data, expected_message)
    logger.info("Partner Details For Health Note Added Successfully")

    logger.info("Update Health Note Data To Partner Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_employment.csv"))
def test_update_partner_employment_data(patch_employment_data,post_client_data,data, field_values, create_client, patch_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    employment_data = common.read_json("./jsons/create_client_employment.json")

    client_employment = post_client_data(partner_cust_id, employment_data, 'employment', True)
    client_employment_data = client_employment.json()
    logger.info(client_employment_data)
    common.check_reponse_message(client_employment_data, constants.add_partner_success_message)
    logger.info("Partner employment Added Successfully")

    employment_id = client_employment_data['data']['employment']['employment_id']

    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_client_data = patch_employment_data(partner_cust_id, employment_id, data, 'employment', False)
    patch_client_data_response = patch_client_data.json()
    logger.info(patch_client_data_response)
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Partner Employment Updated Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_objectives.csv"))
def test_update_partner_objective_data(patch_clientobjectives_data,post_client_data,data, field_values, create_client, patch_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    objectives_data = common.read_json("./jsons/create_new_objectives.json")
    client_objectives = post_client_data(partner_cust_id, objectives_data, 'objectives', True)
    client_objectives_data = client_objectives.json()
    logger.info(client_objectives_data)
    common.check_reponse_message(client_objectives_data, constants.add_partner_success_message)
    logger.info("Partner Details For Objectives Added Successfully")


    objective_id = client_objectives_data['data']['objectives']['objective_id']
    logger.info(customer_id)
    logger.info(objective_id)

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_objectives_data = patch_clientobjectives_data(partner_cust_id, objective_id, values, 'objectives', None)
    patch_identity_data_response = patch_objectives_data.json()
    logger.info(patch_identity_data_response)
    common.check_reponse_message(patch_identity_data_response, expected_message)
    logger.info("Partner Details For Outgoings Updated Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_service_type.csv"))
def test_update_partner_servicetype_data(patch_clientservicetype_data,post_client_data,data, field_values, create_client, patch_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    servicetype_data = common.read_json("./jsons/create_new_servicetype.json")
    client_servicetype = post_client_data(partner_cust_id, servicetype_data, 'service_type', True)
    client_servicetype_data = client_servicetype.json()
    logger.info(client_servicetype_data)
    common.check_reponse_message(client_servicetype_data, constants.add_partner_success_message)
    logger.info("Partner Details For Service Type Added Successfully")


    servicetype_id = client_servicetype_data['data']['servicetype']['servicetype_id']

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_client_data = patch_clientservicetype_data(partner_cust_id, servicetype_id, values, 'service_type', None)
    patch_client_data_response = patch_client_data.json()
    logger.info(expected_message)
    logger.info(patch_client_data_response)
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Partner Details For Service Type Updated Successfully")
    logger.info("Update Service Type Data To Client Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Partner/test_data_identity.csv"))
def test_update_partner_identity_data(patch_clientidentity_data,post_client_data,data, field_values, create_client, patch_client_data, post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    identity_data = common.read_json("./jsons/create_new_identity.json")
    client_identity = post_client_data(partner_cust_id, identity_data, 'identity', True)
    client_identity_data = client_identity.json()
    logger.info(client_identity_data)
    common.check_reponse_message(client_identity_data, constants.add_partner_success_message)
    logger.info("Partner Details For identity Added Successfully")


    identity_id = client_identity_data['data']['identity']['identity_id']

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_identity_data = patch_clientidentity_data(partner_cust_id, identity_id, values, 'identity', None)
    patch_identity_data_response = patch_identity_data.json()
    logger.info(patch_identity_data_response)
    common.check_reponse_message(patch_identity_data_response, expected_message)
    logger.info("Partner Details For Identity Updated Successfully")
    logger.info("Update Identity Data To Client Test Passed!")
