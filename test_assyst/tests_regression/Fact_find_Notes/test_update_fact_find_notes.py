import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_fact_find_notes.csv"))
def test_update_fact_find_data(data, field_values, create_client, post_client_fact_note_data, patch_fact_findnote_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    create_notes = post_client_fact_note_data(customer_id, None, True)
    post_factnotes_response = create_notes.json()
    #logger.info(post_factnotes_response)
    common.check_reponse_message(post_factnotes_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")

    note_id = post_factnotes_response['data']['notes']['note_id']
    file_link = post_factnotes_response['data']['notes']['file_link']
    logger.info(note_id)
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    patch_expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_client_data = patch_fact_findnote_data(customer_id, note_id, data, file_link,False)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, patch_expected_message)
    logger.info("Client Details For Fact Find Notes Updated Successfully")

    logger.info("Update Data To Fact Find Notes Test Passed!")