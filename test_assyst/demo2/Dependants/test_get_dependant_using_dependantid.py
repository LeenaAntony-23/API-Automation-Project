import pytest
import logging
from test_assyst.conftest import post_notes_data_with_customer_id
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_dependant_data_with_valid_customer_id(customer_id,data, create_client, post_dependant_data,get_dependant_data_with_dependant_id):


    create_dependant = post_dependant_data(customer_id, None, 'dependants', True)
    post_dependant_response = create_dependant.json()
    logger.info(post_dependant_response)
    common.check_reponse_message(post_dependant_response, constants.dependant_add_success_message)
    logger.info("Dependant Details Added Successfully")

    dependant_id = post_dependant_response['data']['dependant']['dependant_id']
    get_dependant = get_dependant_data_with_dependant_id(dependant_id, customer_id)
    get_dependant_response = get_dependant.json()
    common.check_reponse_message(get_dependant_response, constants.dependant_fetched_success_message)
    #assert get_dependant_response["isError"] is False
    logger.info("Dependant Details Fetched Successfully")



@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_dependant_data_with_invalidvalid_dependent_id(customer_id,data, create_client, post_dependant_data,get_dependant_data_with_dependant_id):


    get_dependant_data = get_dependant_data_with_dependant_id('d37fcd87-1881-4798-af93-802fea5027b9', customer_id)
    get_dependant_response = get_dependant_data.json()
    common.check_reponse_message(get_dependant_response, constants.dependant_invalid_message)
    assert get_dependant_response["isError"] is False
    logger.info("Fetch AddressBook Data With Invalid Customer ID Test Passed!")