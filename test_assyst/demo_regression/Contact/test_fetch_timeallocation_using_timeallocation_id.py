import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_customer_data_with_valid_customer_id(customer_id,data, create_client, post_client_data,get_timeallocation_data_with_timeallocation_id ):


    timeallocation_data = common.read_json("./jsons/create_new_timeallocation.json")
    client_timeallocation = post_client_data(customer_id, timeallocation_data, 'contacts_time_allocation', True)
    client_timeallocation_data = client_timeallocation.json()
    logger.info(client_timeallocation_data)
    common.check_reponse_message(client_timeallocation_data, constants.add_timeallocation_success_message)
    logger.info("Client Details For Time Allocation Added Successfully")

    customer_id = client_timeallocation_data['data']['timeallocation']['customer_id']
    timeallocation_id = client_timeallocation_data['data']['timeallocation']['timeallocation_id']
    logger.info(customer_id)
    logger.info(timeallocation_id)

    get_timeallocation_data = get_timeallocation_data_with_timeallocation_id(customer_id,timeallocation_id)
    get_timeallocation_response = get_timeallocation_data.json()
    logger.info(get_timeallocation_response)
    common.check_reponse_message(get_timeallocation_response,constants.get_client_success_message)
    assert get_timeallocation_response["isError"] is False
    logger.info("Time Allocation Details Fetched Successfully")

    #common.compare_dicts(client_timeallocation_data['data']['timeallocation'], get_timeallocation_response['data'])
    logger.info("Fetch One Time Allocation Data Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test__fetch_one_customer_data_with_invalid_timeallocation_id(customer_id,data, create_client, get_timeallocation_data_with_timeallocation_id):

    get_client_data = get_timeallocation_data_with_timeallocation_id(customer_id,'bddfd833-0bee-4c40-94e0-8cad8feb295c')
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response,constants.invalid_Timeallocation_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Time Allocation Test Passed!")