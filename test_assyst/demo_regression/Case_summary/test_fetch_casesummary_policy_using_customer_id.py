import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, get_case_summary_policy_data_with_customer_id ):
    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_details = get_case_summary_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response )
    common.check_reponse_message(policy_response, constants.get_case_summary_policy_success_message)
    logger.info("Case Summary Policy Details Fetched Successfully")

    logger.info("Fetch Case Summary Policy Data Of One Customer Test Passed!")


def test_fetch_policy_data_with_invalid_customer_id(get_case_summary_policy_data_with_customer_id):
    get_policy_data = get_case_summary_policy_data_with_customer_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0')
    get_policy_response = get_policy_data.json()
    common.check_reponse_message(get_policy_response, constants.invalid_customer_id_message)
    assert get_policy_response["isError"] is False
    logger.info("Fetch Asset Data With Invalid Customer ID Test Passed!")