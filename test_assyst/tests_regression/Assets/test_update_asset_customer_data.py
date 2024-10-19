import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_investment.csv"))
def test_update_data_to_asset_investment(post_partner_data,get_asset_data_with_customer_id,data,post_system_manager_data, dataa, field_values,  create_client, post_asset_data, patch_asset_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_asset = post_asset_data(customer_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")
    asset_details = get_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    asset_id = post_asset_response['data']['asset_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_asset_data = patch_asset_data(customer_id,partner_cust_id,provider_correspondence_id, asset_id, values, 'asset_investment_asset', False)
    update_asset_data_response = update_asset_data.json()
    common.check_reponse_message(update_asset_data_response, expected_message)
    logger.info("Asset Details For Investemnt Updated Successfully")
    logger.info(update_asset_data_response)
    logger.info("Update Asset Investment Data Test Passed!")
    asset_details = get_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")
    logger.info(asset_response)

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_share_holdings.csv"))
def test_update_data_to_asset_share_holdings(post_partner_data,get_asset_data_with_customer_id,data,post_system_manager_data, dataa, field_values,  create_client, post_asset_data, patch_asset_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_asset = post_asset_data(customer_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Share Holdings Added Successfully")
    asset_details = get_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    asset_id = post_asset_response['data']['asset_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    asset_data = patch_asset_data(customer_id,partner_cust_id,provider_correspondence_id, asset_id, values, 'asset_share_holdings_asset', False)
    update_asset_data_response = asset_data.json()
    common.check_reponse_message(update_asset_data_response, expected_message)
    logger.info("Asset Details For Share Holdings Updated Successfully")


    logger.info("Update Asset Share Holdings Data Test Passed!")
    asset_details = get_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")
    logger.info(asset_response)


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_home_personal.csv"))
def test_update_data_to_asset_home_personal(post_partner_data,get_asset_data_with_customer_id,data,post_system_manager_data, dataa, field_values,  create_client, post_asset_data, patch_asset_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_asset = post_asset_data(customer_id,provider_correspondence_id, None, 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Home And Personal Added Successfully")
    asset_details = get_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    asset_id = post_asset_response['data']['asset_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    asset_data = patch_asset_data(customer_id,partner_cust_id,provider_correspondence_id, asset_id, values, 'asset_home_personal_asset', False)
    update_asset_data_response = asset_data.json()
    common.check_reponse_message(update_asset_data_response, expected_message)
    logger.info("Asset Details For Home And Personal Updated Successfully")

    logger.info("Update Asset Home Personal Data Test Passed!")
    asset_details = get_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")
    logger.info(asset_response)


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/"
                                                         "test_data_asset_banks_building_societies.csv"))
def test_update_data_to_asset_banks_building_societies(post_partner_data,get_asset_data_with_customer_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data, patch_asset_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_asset = post_asset_data(customer_id, provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Banks/Building Societies Added Successfully")
    asset_details = get_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    asset_id = post_asset_response['data']['asset_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    asset_data = patch_asset_data(customer_id,partner_cust_id,provider_correspondence_id, asset_id, values, 'asset_banks_building_societies_asset', False)
    update_asset_data_response = asset_data.json()
    logger.info(update_asset_data_response)
    common.check_reponse_message(update_asset_data_response, expected_message)
    logger.info("Asset Details For Banks/Building Societies Updated Successfully")
    asset_details = get_asset_data_with_customer_id(customer_id)
    asset_response = asset_details.json()
    common.check_reponse_message(asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")
    logger.info(asset_response)

    logger.info("Update Asset Bank And Building Socities Data Test Passed!")

