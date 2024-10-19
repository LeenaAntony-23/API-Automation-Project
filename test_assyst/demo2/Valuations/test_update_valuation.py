import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_asset_investment_valuation(customer_id,partner_cust_id,provider_correspondence_id,get_valuation_data_with_customer_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data, post_valuation_data, patch_valuation_data):
    # Create Client

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create fund for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_valuation = post_valuation_data(customer_id, asset_id, None, 'asset_investment_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message )
    logger.info("Valuation Details For Asset Investment Added Successfully")
    #logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, asset_id, values, 'asset_investment_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for life assurance Updated Successfully")

    logger.info("Update Investment valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_asset_share_holdings_valuation(partner_cust_id,customer_id,provider_correspondence_id,get_valuation_data_with_customer_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data, post_valuation_data, patch_valuation_data):
    # Create Client


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create fund for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_valuation = post_valuation_data(customer_id, asset_id, None, 'asset_share_holdings_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message )
    logger.info("Valuation Details For Asset ShareHolding Added Successfully")
    #logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, asset_id, values, 'asset_share_holdings_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for ShareHolding Updated Successfully")

    logger.info("Update ShareHolding valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_asset_home_personal_valuation(partner_cust_id,customer_id,provider_correspondence_id,get_valuation_data_with_customer_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data, post_valuation_data,
                                               patch_valuation_data):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create fund for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_valuation = post_valuation_data(customer_id, asset_id, None, 'asset_home_personal_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message )
    logger.info("Valuation Details For Asset Personal Added Successfully")
    # logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, asset_id, values,
                                                 'asset_home_personal_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for Personal Updated Successfully")

    logger.info("Update Personal  valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_asset_banks_building_societies_valuation(partner_cust_id,customer_id,provider_correspondence_id,get_valuation_data_with_customer_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data, post_valuation_data,
                                               patch_valuation_data):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create fund for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_valuation = post_valuation_data(customer_id, asset_id, None, 'asset_banks_building_societies_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message )
    logger.info("Valuation Details For Asset Bank Building Added Successfully")
    # logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, asset_id, values,
                                                 'asset_banks_building_societies_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for Bank Building Updated Successfully")

    logger.info("Update Bank Building  valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_policy_valuation(customer_id,partner_cust_id,provider_correspondence_id,get_valuation_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data , post_valuation_data,patch_valuation_data):
    # Create Client



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    post_asset_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_life_assurance_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message)
    logger.info("Valuation Details For policy Added Successfully")
    # logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, policy_id, values,
                                                 'policies_life_assurance_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for Policy Updated Successfully")

    logger.info("Update Policy life assurance valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_policy_pension_valuation(customer_id,partner_cust_id,provider_correspondence_id,get_valuation_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data , post_valuation_data,patch_valuation_data):



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    post_asset_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_pensions_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message)
    logger.info("Valuation Details For policy Added Successfully")
    # logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, policy_id, values,
                                                 'policies_pensions_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for Policy Updated Successfully")

    logger.info("Update Policy Pension valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_policies_investments_valuation(customer_id,partner_cust_id,provider_correspondence_id,get_valuation_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data , post_valuation_data,patch_valuation_data):



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    post_asset_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_investments_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message)
    logger.info("Valuation Details For policy Added Successfully")
    # logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, policy_id, values,
                                                 'policies_investments_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for Policy Updated Successfully")

    logger.info("Update Policy Investment valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_policies_income_protection_valuation(partner_cust_id,customer_id,provider_correspondence_id,get_valuation_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data , post_valuation_data,patch_valuation_data):



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    post_asset_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_income_protection_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message)
    logger.info("Valuation Details For policy Added Successfully")
    # logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, policy_id, values,
                                                 'policies_income_protection_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for Policy Updated Successfully")

    logger.info("Update Policy Income protection valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_policies_health_assurance_valuation(partner_cust_id,customer_id,provider_correspondence_id,get_valuation_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data , post_valuation_data,patch_valuation_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    post_asset_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_health_assurance_valuation', True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message)
    logger.info("Valuation Details For policy Added Successfully")
    # logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, policy_id, values,
                                                 'policies_health_assurance_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for Policy Updated Successfully")

    logger.info("Update Policy Health assurance valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/valuations/test_data_valuations.csv"))
def test_update_policies_general_valuation(partner_cust_id,customer_id,provider_correspondence_id,get_valuation_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                    post_valuation_data, patch_valuation_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    post_asset_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_general_valuation',
                                               True)
    post_asset_valuation_response = post_asset_valuation.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuation_success_message)
    logger.info("Valuation Details For policy Added Successfully")
    # logger.info(post_asset_withdrawal_response)

    valuation_id = post_asset_valuation_response['data']['valuation_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_valuation_data = patch_valuation_data(customer_id, valuation_id, policy_id, values,
                                                 'policies_general_valuation', False)
    update_valuation_data_response = update_valuation_data.json()
    common.check_reponse_message(update_valuation_data_response, expected_message)
    logger.info(update_valuation_data_response)
    logger.info("valuation Details for Policy Updated Successfully")

    logger.info("Update Policy General valuation Test Passed!")
    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")
