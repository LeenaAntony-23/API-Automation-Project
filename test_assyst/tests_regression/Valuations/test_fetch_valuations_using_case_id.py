import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_asset_investment_valuations_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_asset_data, post_valuation_data ,get_valuation_data_with_case_id ):
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


    client_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset  Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_valuations = post_valuation_data(customer_id, asset_id, None, 'asset_investment_valuation', True)
    post_asset_valuation_response = post_asset_valuations.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuations_success_message)
    logger.info("Asset Valuation Details For Investment Added Successfully")


    case_id = post_asset_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Asset Fetched Successfully")

    #common.compare_dicts(post_asset_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Asset Investment  With Case ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_asset_share_holdings_valuations_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_asset_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    client_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset  Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_valuations = post_valuation_data(customer_id, asset_id, None, 'asset_share_holdings_valuation', True)
    post_asset_valuation_response = post_asset_valuations.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuations_success_message)
    logger.info("Asset Valuation Details For share holding Added Successfully")


    case_id = post_asset_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Asset Fetched Successfully")

    #common.compare_dicts(post_asset_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Asset Share Holdings With Case ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_asset_home_personal_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_asset_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    client_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_home_personal_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset  Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_valuations = post_valuation_data(customer_id, asset_id, None, 'asset_home_personal_valuation', True)
    post_asset_valuation_response = post_asset_valuations.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuations_success_message)
    logger.info("Asset Valuation Details For home personal Added Successfully")


    case_id = post_asset_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Asset Fetched Successfully")

    #common.compare_dicts(post_asset_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Asset Home personal With Case ID Test Passed!")



@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_asset_bank_building_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_asset_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    client_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset  Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_valuations = post_valuation_data(customer_id, asset_id, None, 'asset_banks_building_societies_valuation', True)
    post_asset_valuation_response = post_asset_valuations.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuations_success_message)
    logger.info("Asset Valuation Details For Bank building Added Successfully")


    case_id = post_asset_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Asset Fetched Successfully")

    #common.compare_dicts(post_asset_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Asset Bank building With Case ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_general_valuations_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_policy_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_general_valuation', True)
    post_valuation_response = post_valuation.json()
    logger.info(post_valuation_response)
    common.check_reponse_message(post_valuation_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy General Added Successfully")
    case_id = post_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")

    #common.compare_dicts(post_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy General With Case ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_life_assurance_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_policy_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For life assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_life_assurance_valuation', True)
    post_valuation_response = post_valuation.json()
    logger.info(post_valuation_response)
    common.check_reponse_message(post_valuation_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy life assurance Added Successfully")
    case_id = post_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy life assurance Fetched Successfully")

    #common.compare_dicts(post_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy life assurance With Case ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_pensions_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_policy_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details  Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_pensions_valuation', True)
    post_valuation_response = post_valuation.json()
    logger.info(post_valuation_response)
    common.check_reponse_message(post_valuation_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy pensions Added Successfully")
    case_id = post_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy pensions Fetched Successfully")

    #common.compare_dicts(post_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy pensions With Case ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_investments_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_policy_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details  Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_investments_valuation', True)
    post_valuation_response = post_valuation.json()
    logger.info(post_valuation_response)
    common.check_reponse_message(post_valuation_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy pensions Added Successfully")
    case_id = post_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy investments Fetched Successfully")

    #common.compare_dicts(post_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy investments With Case ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_income_protection_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_policy_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_income_protection_valuation', True)
    post_valuation_response = post_valuation.json()
    logger.info(post_valuation_response)
    common.check_reponse_message(post_valuation_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy Income protection Added Successfully")
    case_id = post_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy Income protection Fetched Successfully")

    #common.compare_dicts(post_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy Income protection With Case ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_health_assurance_data_with_case_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_policy_data, post_valuation_data ,get_valuation_data_with_case_id ):
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



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_valuation = post_valuation_data(customer_id, policy_id, None, 'policies_health_assurance_valuation', True)
    post_valuation_response = post_valuation.json()
    logger.info(post_valuation_response)
    common.check_reponse_message(post_valuation_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy Health Assurance Added Successfully")
    case_id = post_valuation_response['data']['case_id']

    get_valuation_data = get_valuation_data_with_case_id(case_id,customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy Health Assurance Fetched Successfully")

    #common.compare_dicts(post_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy Health Assurance With Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_policies_general_valuations_data_with_invalid_case_id(data,create_client,get_valuation_data_with_case_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    get_valuation_data = get_valuation_data_with_case_id('a2f84b63-4c41-4710-9b54-1ca075b48f10',customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_invalid_valuation_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Fetch Valuations Data With Invalid Case ID Test Passed!")