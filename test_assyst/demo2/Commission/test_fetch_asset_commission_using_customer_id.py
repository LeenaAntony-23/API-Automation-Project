import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_of_commission_using_customer_id(customer_id, partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_customer_id ):
    post_asset = post_asset_data(customer_id, partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, asset_id, payment_id, None,
                                                 'asset_investment_payment_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Asset Investment Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    payment_id = post_commission_response['data']['payment_id']
    case_id = post_commission_response['data']['case_id']

    get_commission_data = get_asset_commission_data_with_customer_id(customer_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Asset Investment using Customer ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_of_commission_using_invalid_customer_id(data, create_client,get_asset_commission_data_with_customer_id ):
    get_commission_data = get_asset_commission_data_with_customer_id('aff44303-74fa-4ba6-b18d-b6bd68f0725a')
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.invalid_commission_customer_id_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")
    logger.info("Fetch Commission Details For Asset Investment using Invalid Customer ID Test Passed!")

