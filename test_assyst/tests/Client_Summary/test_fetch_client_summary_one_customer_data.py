import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_customer_data_with_valid_customer_id(data, post_client_data,create_client, get_client_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']

    data = common.read_json("./jsons/create_client_contexts.json")
    client_employment = post_client_data(customer_id, data, 'employment', True)
    client_employment_data = client_employment.json()
    common.check_reponse_message(client_employment_data, constants.add_client_success_message)
    logger.info("Client Details For Employment Added Successfully")

    client_identity = post_client_data(customer_id, data, 'identity', True)
    client_identity_data = client_identity.json()
    common.check_reponse_message(client_identity_data,constants.add_client_success_message )
    logger.info("Client Details For Identity Added Successfully")

    client_objectives = post_client_data(customer_id, data, 'objectives', True)
    client_objectives_data = client_objectives.json()
    common.check_reponse_message(client_objectives_data,constants.add_client_success_message )
    logger.info("Client Details For Objectives Added Successfully")

    client_servicetype = post_client_data(customer_id, data, 'service_type',True)
    client_servicetype_data = client_servicetype.json()
    common.check_reponse_message(client_servicetype_data,constants.add_client_success_message )
    logger.info("Client Details For Service Type Added Successfully")


    get_client_response = get_client_data_with_customer_id(customer_id)
    get_response_data = get_client_response.json()
    common.check_reponse_message(get_response_data, constants.get_client_success_message)
    logger.info(get_response_data)
    logger.info("Client Details Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_customer_data_with_invalid_customer_id(data, get_client_data_with_customer_id):
    get_client_response = get_client_data_with_customer_id('5f6e7568-f2e2-4fbf-a3d2-a2c246544a08')
    get_response_data = get_client_response.json()
    common.check_reponse_message(get_response_data, constants.invalid_customer_id_message)
    logger.info(get_response_data)
    logger.info("Client Details Fetched Successfully")