import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("datas", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contacts_notes.csv"))
def test_add_contacts_notes_data(customer_id,get_notes_data_with_customer_id,datas,field_values, create_client, post_client_note_data, patch_note_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_contact_action = post_client_note_data(customer_id,values,False)
    client_contact_action_data = client_contact_action.json()
    common.check_reponse_message(client_contact_action_data,expected_message )
    logger.info("Client Details For Contact Notes Added Successfully")
    get_client_data = get_notes_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)

    common.check_reponse_message(get_client_response, constants.customer_success_message)
    assert get_client_response["isError"] is False
    logger.info("Contact Note Details Fetched Successfully")



