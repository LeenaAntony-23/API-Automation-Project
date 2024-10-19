import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_show_non_current(customer_id,partner_cust_id,provider_correspondence_id,post_policy_data,post_liability_data,data,post_system_manager_data, dataa, create_client, post_asset_data, get_case_summary_show_noncurrent):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    post_policy = post_policy_data(customer_id, partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_details = get_case_summary_show_noncurrent(customer_id)
    case_response = case_details.json()
    logger.info(case_response)
    common.check_reponse_message(case_response, constants.get_case_show_summary_non_current_message)
    logger.info("Case Summary Policy Details Fetched Successfully")