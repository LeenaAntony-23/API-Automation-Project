import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_customer_data_with_valid_customer_id(data, create_client, post_client_data, get_timeallocation_data_with_customer_id ):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    logger.info(create_client_response)

    customer_id = create_client_response['data']['customer_id']

    timeallocation_data = common.read_json("./jsons/create_new_timeallocation.json")
    client_timeallocation = post_client_data(customer_id, timeallocation_data, 'contacts_time_allocation', True)
    client_timeallocation_data = client_timeallocation.json()
    logger.info(client_timeallocation_data)
    common.check_reponse_message(client_timeallocation_data, constants.add_timeallocation_success_message)
    logger.info("Client Details For Time Allocation Added Successfully")

    get_timeallocation_data = get_timeallocation_data_with_customer_id(customer_id)
    get_timeallocation_response = get_timeallocation_data.json()
    logger.info(get_timeallocation_response)
    common.check_reponse_message(get_timeallocation_response, constants.get_client_success_message)
    assert get_timeallocation_response["isError"] is False
    logger.info("Time Allocation Details Fetched Successfully")

    #common.compare_dicts(client_timeallocation_data['data']['timeallocation'], get_timeallocation_response['data'])
    logger.info("Fetch One Time Allocation Data Test Passed!")

def test_fetch_one_customer_data_with_invalid_customer_id(get_timeallocation_data_with_customer_id):
        get_client_data = get_timeallocation_data_with_customer_id('e34960f1-ce23-4985-a5df-d497193be3ab')
        get_client_response = get_client_data.json()
        logger.info(get_client_response)
        common.check_reponse_message(get_client_response, constants.invalid_time_customer_id_message)
        assert get_client_response["isError"] is False
        logger.info("Fetch Customer Data With Invalid Customer ID Test Passed!")