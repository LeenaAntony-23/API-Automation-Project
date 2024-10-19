import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_customer_data_with_valid_customer_id(data, create_client, post_client_data, get_commission_data_with_commission_id ):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    logger.info(create_client_response)

    customer_id = create_client_response['data']['customer_id']

    commission_data = common.read_json("./jsons/create_new_commission.json")
    client_commission = post_client_data(customer_id, commission_data, 'fees_charges', True)
    client_commission_data = client_commission.json()
    logger.info(client_commission_data)
    common.check_reponse_message(client_commission_data, constants.add_commission_success_message)
    logger.info("Client Details For Commission Added Successfully")


    commission_id = client_commission_data['data']['fees_charges']['commission_id']
    #logger.info(commission_id)

    get_commission_data = get_commission_data_with_commission_id(customer_id,commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_client_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details Fetched Successfully")

    #common.compare_dicts(client_commission_data['data']['fees_charges'], get_commission_response['data'])
    logger.info("Fetch One Commission Data Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test__fetch_one_customer_data_with_invalid_commission_id(data, create_client, get_commission_data_with_commission_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    get_client_data = get_commission_data_with_commission_id(customer_id,'ad1eef7e-bdcd-4c0c-987a-34268221ff2e')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response,constants.invalid_commisssion_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Commission ID Test Passed!")