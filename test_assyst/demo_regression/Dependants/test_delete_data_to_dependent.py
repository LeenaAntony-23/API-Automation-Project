import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
def test_delete_all_data_to_dependent(data,create_client,post_dependant_data,delete_client_details,get_dependant_data_with_customer_id):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    dependent_data = common.read_json("./jsons/create_new_dependant.json")
    post_dependant = post_dependant_data(customer_id, dependent_data, 'dependants', True)
    post_dependant_response = post_dependant.json()
    logger.info(post_dependant_response)
    common.check_reponse_message(post_dependant_response, constants.dependant_add_success_message)
    logger.info("Dependant Details Added Successfully")
    dependant_id = post_dependant_response['data']['dependant']['dependant_id']


    dependant_details = get_dependant_data_with_customer_id(customer_id)
    get_client_response_before = dependant_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_dependant_success_message)
    logger.info("Dependant Details Fetched Successfully Before Deletion")

    delete_client_data = delete_client_details('dependent',dependant_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_dependent_success_message)
    logger.info("Dependent Details Deleted Successfully")

    dependant_details = get_dependant_data_with_customer_id(customer_id)
    get_client_response_after = dependant_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.dependant_invalid_message)
    logger.info("Dependent Details Fetched Successfully After Deletion")

    dependent_after = get_client_response_after['data']

    assert dependant_id not in [['dependant_id'] for data in
                                 dependent_after], "Dependent ID should be deleted from the response"

    logger.info("Confirmed that dependent data has been deleted successfully.")

