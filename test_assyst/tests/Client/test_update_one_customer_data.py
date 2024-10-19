import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_name_and_address.csv"))
def test_update_client_name_address_data(get_client_data_with_customer_id,data, field_values, create_client, patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_client_data = patch_client_data(customer_id, data, 'name_and_address', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Name And Address Updated Successfully")

    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
    logger.info("Update Data To Client Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_contact.csv"))
def test_update_client_contact_data(get_client_data_with_customer_id,data, field_values, create_client, patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    #data.popitem()
    patch_client_data = patch_client_data(customer_id, data, 'contact', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Contact Updated Successfully")
    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
    logger.info("Update Contact Data To Client Test Passed!")

#
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_nationality.csv"))
def test_update_client_nationality_data(get_client_data_with_customer_id,data, field_values, create_client, patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    #data.popitem()
    patch_client_datas = patch_client_data(customer_id, data, 'nationality', None)
    patch_client_data_response = patch_client_datas.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Nationality Updated Successfully")
    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
    logger.info("Update Nationality Data To Client Test Passed!")

#
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_personal.csv"))
def test_update_client_personal_data(get_client_data_with_customer_id,data, field_values, create_client, patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    #data.popitem()
    patch_client_data = patch_client_data(customer_id, data, 'personal', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Personal Updated Successfully")
    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
    logger.info("Update Personal Data To Client Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_health_note.csv"))
def test_update_client_health_note_data(get_client_data_with_customer_id,data, field_values, create_client, patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    #data.popitem()
    patch_client_data = patch_client_data(customer_id, data, 'health_note', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Health Note Updated Successfully")
    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
    logger.info("Update Health Note Data To Client Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_administration.csv"))
def test_update_client_administration_data(get_client_data_with_customer_id,data, field_values, create_client, patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    #data.popitem()
    patch_client_data = patch_client_data(customer_id, data, 'administration', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Administration Updated Successfully")
    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
    logger.info("Update Administration Data To Client Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_compliance.csv"))
def test_update_client_compliance_data(get_client_data_with_customer_id,data, field_values, create_client, patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    #data.popitem()
    patch_client_data = patch_client_data(customer_id, data, 'compliance', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Compliance Updated Successfully")
    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
    logger.info("Update Compliance Data To Client Test Passed!")
