import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, get_case_summary_asset_data_with_customer_id):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    asset_details = get_case_summary_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_case_summary_asset_details_success_message)
    logger.info("Case Summary Asset Details Fetched Successfully")
    logger.info(asset_response)
    common.compare_dicts(post_asset_response['data'], asset_response['data'])

    logger.info("Fetch Case Summary Asset Data Of One Customer Test Passed!")



def test_fetch_asset_data_with_invalid_customer_id(get_case_summary_asset_data_with_customer_id):
    get_asset_data = get_case_summary_asset_data_with_customer_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0')
    get_asset_response = get_asset_data.json()
    common.check_reponse_message(get_asset_response, constants.invalid_casesummary_asset_customer_id_message )
    assert get_asset_response["isError"] is False
    logger.info("Fetch Asset Data With Invalid Customer ID Test Passed!")

