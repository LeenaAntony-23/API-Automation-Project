import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_general_fund_data_with_customer_id(customer_id,partner_cust_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_customer_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_asset_fund = post_fund_data(customer_id, policy_id, None, 'policies_general_funds', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For General Added Successfully")


    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For General With Customer ID Test Passed!")