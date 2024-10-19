import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')





@pytest.mark.parametrize("datas", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_fact_find_notes.csv"))
def test_add_Fact_find_notes_data(post_client_fact_note_data,datas,field_values, create_client, post_client_note_data, patch_note_data):
    create_client = create_client(datas, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_contact_action = post_client_fact_note_data(customer_id,values,False)
    client_contact_action_data = client_contact_action.json()
    common.check_reponse_message(client_contact_action_data,expected_message )
    logger.info("Client Details For Fact Find Notes Added Successfully")
