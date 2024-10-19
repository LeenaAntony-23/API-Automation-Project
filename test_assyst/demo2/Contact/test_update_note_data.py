import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("datas", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contacts_notes.csv"))
def test_update_contacts_notes_data(customer_id,get_notes_data_with_customer_id,datas,field_values, create_client, post_client_note_data, patch_note_data):

    create_notes = post_client_note_data(customer_id, None, True)
    post_factnotes_response = create_notes.json()
    #logger.info(post_factnotes_response)
    common.check_reponse_message(post_factnotes_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")

    note_id = post_factnotes_response['data']['notes']['note_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_client_data = patch_note_data(customer_id,note_id, data, False)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Contact Notes Updated Successfully")

    logger.info("Update Data To Contact Notes Test Passed!")
    get_client_data = get_notes_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)

    common.check_reponse_message(get_client_response, constants.customer_success_message)
    assert get_client_response["isError"] is False
    logger.info("Contact Note Details Fetched Successfully")

