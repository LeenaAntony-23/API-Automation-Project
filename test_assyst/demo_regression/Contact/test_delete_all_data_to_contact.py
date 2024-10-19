import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
def test_delete_all_data_to_single_client_action(data,create_client,post_client_data,delete_client_details,get_appointment_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create client action using json data
    appointment_data = common.read_json("./jsons/create_client_contexts.json")
    client_contact_action = post_client_data(customer_id, appointment_data, 'contacts_client_action', True)
    client_contact_action_data = client_contact_action.json()
    logger.info(client_contact_action_data)
    common.check_reponse_message(client_contact_action_data, constants.add_client_success_message)
    logger.info("Contact Client Action Added Successfully")
    appointment_id = client_contact_action_data['data']['contacts_client_action']['appointment_id']

    #  Fetch client action data before deletion
    get_appointment_data = get_appointment_data_with_customer_id(customer_id)
    get_client_response_after = get_appointment_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_client_appointment_message)
    logger.info("Client Details Appointment Details Fetch Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('client_action',appointment_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_client_action_success_message)
    logger.info("Appointment Details Deleted Successfully")

    #  Fetch client action data after deletion
    get_appointment_data = get_appointment_data_with_customer_id(customer_id)
    get_client_response_after = get_appointment_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_appointment_invalid_message)
    logger.info("Appointment Details Fetch Successfully")

    appointment_after = get_client_response_after['data']
    assert appointment_id not in [['appointment_id'] for data in
                                 appointment_after], "Appointment ID is not deleted from the response"

    logger.info("Confirmed that Appointment data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contacts_client_action.csv"))
def test_delete_all_data_to_multiple_client_action(field_values,data,create_client,post_client_data,delete_client_details,get_appointment_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create client action using json data
    appointment_data = common.read_json("./jsons/create_client_contexts.json")
    client_contact_action = post_client_data(customer_id, appointment_data, 'contacts_client_action', True)
    client_contact_action_data = client_contact_action.json()
    logger.info(client_contact_action_data)
    common.check_reponse_message(client_contact_action_data, constants.add_client_success_message)
    logger.info("First Contact Client Action Added Successfully")
    appointment_id_1 = client_contact_action_data['data']['contacts_client_action']['appointment_id']

    # Create client action using CSV data
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
             for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_contact_action = post_client_data(customer_id, values, 'contacts_client_action', False)
    client_contact_action_data = client_contact_action.json()
    common.check_reponse_message(client_contact_action_data, expected_message)
    logger.info("Second Contact Client Action Added Successfully")
    appointment_id_2 = client_contact_action_data['data']['contacts_client_action']['appointment_id']

    #  Fetch client action data before deletion
    get_appointment_data = get_appointment_data_with_customer_id(customer_id)
    get_client_response_after = get_appointment_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_client_appointment_message)
    logger.info("First and Second Appointment Details Fetch Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('client_action',appointment_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_client_action_success_message)
    logger.info("First Appointment Details Deleted Successfully")

    #  Fetch client action data after deletion
    get_appointment_data = get_appointment_data_with_customer_id(customer_id)
    get_client_response_after = get_appointment_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_client_appointment_message)
    logger.info("Second Appointment Details Fetch Successfully")

    appointment_after = get_client_response_after['data']

    assert appointment_id_1 not in [data['appointment_id'] for data in
                                 appointment_after], "First Appointment ID is not deleted from the response"

    logger.info("Confirmed that Appointment data has been deleted successfully.")


@pytest.mark.parametrize("data",["./jsons/create_client.json"])
def test_delete_all_data_to_single_contact_note(data,create_client,post_client_note_data,delete_client_details,get_notes_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create note using json data
    contact_note_data = common.read_json("./jsons/create_client_notes.json")
    create_notes = post_client_note_data(customer_id, contact_note_data, True)
    post_factnotes_response = create_notes.json()
    logger.info(post_factnotes_response)
    common.check_reponse_message(post_factnotes_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")
    note_id = post_factnotes_response['data']['notes']['note_id']

    #  Fetch note data before deletion
    get_client_data = get_notes_data_with_customer_id(customer_id)
    get_client_response_before = get_client_data.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.customer_success_message)
    logger.info("Contact Note Details Fetched Successfully")

    #  Delete first note file details
    delete_client_file_data = delete_client_details('contact_note_file', note_id)
    delete_client_file_data_response = delete_client_file_data.json()
    logger.info(delete_client_file_data_response)
    common.check_reponse_message(delete_client_file_data_response, constants.delete_contact_note_file_success_message)
    logger.info("Contact Note File Details Deleted Successfully")

    #  Delete first note details
    delete_client_data = delete_client_details('contact_note',note_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_contact_note_success_message)
    logger.info("Contact Note Details Deleted Successfully")

    #  Fetch note data after deletion
    get_client_data = get_notes_data_with_customer_id(customer_id)
    get_client_response_after = get_client_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.customer_success_message)
    logger.info("Contact Note Details Fetched Successfully")

    contact_note_after = get_client_response_after['data']

    assert note_id not in [data['note_id'] for data in
                                 contact_note_after], "Contact note is not deleted from the response"
    logger.info("Confirmed that Contact Note data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contacts_notes.csv"))
def test_delete_all_data_to_multiple_contact_note(field_values,data,create_client,post_client_note_data,delete_client_details,get_notes_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create note using JSON data
    contact_note_data = common.read_json("./jsons/create_client_notes.json")
    create_notes = post_client_note_data(customer_id, contact_note_data, True)
    post_factnotes_response = create_notes.json()
    logger.info(post_factnotes_response)
    common.check_reponse_message(post_factnotes_response, constants.add_fact_find_success_message)
    logger.info("First Note Details Added Successfully")
    note_id_1 = post_factnotes_response['data']['notes']['note_id']

    # Create note using CSV data
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_contact_action = post_client_note_data(customer_id, values, False)
    client_contact_action_data = client_contact_action.json()
    common.check_reponse_message(client_contact_action_data, expected_message)
    logger.info("Second Note Details Added Successfully")
    note_id_2 = post_factnotes_response['data']['notes']['note_id']

    #  Fetch note data before deletion
    get_client_data = get_notes_data_with_customer_id(customer_id)
    get_client_response_before = get_client_data.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.customer_success_message)
    logger.info("First and Second Contact Note Details Fetched Successfully")

    #  Delete first note file details
    delete_client_file_data = delete_client_details('contact_note_file', note_id_1)
    delete_client_file_data_response = delete_client_file_data.json()
    logger.info(delete_client_file_data_response)
    common.check_reponse_message(delete_client_file_data_response, constants.delete_contact_note_file_success_message)
    logger.info("Contact Note File Details Deleted Successfully")

    #  Delete first note details
    delete_client_data = delete_client_details('contact_note',note_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_contact_note_success_message)
    logger.info("First Contact Note Details Deleted Successfully")

    #  Fetch note data after deletion
    get_client_data = get_notes_data_with_customer_id(customer_id)
    get_client_response_after = get_client_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.customer_success_message)
    logger.info("Second Contact Note Details Fetched Successfully")

    contact_note_after = get_client_response_after['data']
    assert note_id_1 not in [['note_id'] for data in
                                 contact_note_after], "First Contact note is not deleted from the response"

    logger.info("Confirmed that Contact Note data has been deleted successfully.")

