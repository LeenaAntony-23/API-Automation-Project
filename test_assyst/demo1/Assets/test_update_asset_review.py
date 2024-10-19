import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_review.csv"))
def test_update_asset_investment_review_(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,patch_asset_review_data):

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    logger.info(asset_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    case_id=asset_id
    update_policy_data = patch_asset_review_data(customer_id,case_id, values, "asset_investment_review", False)
    update_policy_data_response = update_policy_data.json()
    logger.info(update_policy_data_response)
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Asset Details for Investment Review Updated Successfully")
    logger.info("Update Asset Investment Review Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_review.csv"))
def test_update_asset_share_holdings_review_(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,patch_asset_review_data):

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Share Holdings Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    case_id=asset_id
    logger.info(asset_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_asset_review_data(customer_id,case_id, values, "asset_share_holdings_review", False)
    update_policy_data_response = update_policy_data.json()
    logger.info(update_policy_data_response)
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Asset Details for Share Holdings Review Updated Successfully")
    logger.info("Update Asset Share Holdings Review Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_review.csv"))
def test_update_asset_home_personal_review_(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,patch_asset_review_data):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Home And Personal Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    case_id=asset_id
    logger.info(asset_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_asset_review_data(customer_id,case_id, values, "asset_home_personal_review", False)
    update_policy_data_response = update_policy_data.json()
    logger.info(update_policy_data_response)
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Asset Details for Home And Personal Review Updated Successfully")

    logger.info("Update Asset Home And Personal Review Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_review.csv"))
def test_update_asset_banks_building_societies_review_(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,patch_asset_review_data):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Banks/Building Societies Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    case_id= asset_id
    logger.info(asset_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_asset_review_data(customer_id,case_id, values, "asset_banks_building_societies_review", False)
    update_policy_data_response = update_policy_data.json()
    logger.info(update_policy_data_response)
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Asset Details for Banks/Building Societies Review Updated Successfully")

    logger.info("Update Asset Banks/Building Societies Review Test Passed!")


