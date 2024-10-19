import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_of_asset_investment_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_valuation_data ,get_valuation_data_with_valuation_id ):

    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset  Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_valuations = post_valuation_data(customer_id, asset_id, None, 'asset_investment_valuation', True )
    post_asset_valuation_response = post_asset_valuations.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuations_success_message)
    logger.info("Asset Valuation Details For Investment Added Successfully")

    valuation_id = post_asset_valuation_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id,valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Asset Investment Fetched Successfully")

    #common.compare_dicts(post_asset_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Asset Investment using Valuation ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_of_asset_share_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_valuation_data ,get_valuation_data_with_valuation_id ):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset  Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_valuations = post_valuation_data(customer_id, asset_id, None, 'asset_share_holdings_valuation', True )
    post_asset_valuation_response = post_asset_valuations.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuations_success_message)
    logger.info("Asset Valuation Details For Share holding Added Successfully")

    valuation_id = post_asset_valuation_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id,valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Asset Share holding Fetched Successfully")

    #common.compare_dicts(post_asset_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Asset Share holding using Valuation ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_of_asset_home_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_valuation_data ,get_valuation_data_with_valuation_id ):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_home_personal_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset  Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_valuations = post_valuation_data(customer_id, asset_id, None, 'asset_home_personal_valuation', True )
    post_asset_valuation_response = post_asset_valuations.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuations_success_message)
    logger.info("Asset Valuation Details For Personal Added Successfully")

    valuation_id = post_asset_valuation_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id,valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Asset Personal Fetched Successfully")

    #common.compare_dicts(post_asset_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Asset Personal using Valuation ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_of_asset_buildings_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_valuation_data ,get_valuation_data_with_valuation_id ):



    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset  Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_valuations = post_valuation_data(customer_id, asset_id, None, 'asset_banks_building_societies_valuation', True )
    post_asset_valuation_response = post_asset_valuations.json()
    logger.info(post_asset_valuation_response)
    common.check_reponse_message(post_asset_valuation_response, constants.add_valuations_success_message)
    logger.info("Asset Valuation Details For Bank Building Added Successfully")

    valuation_id = post_asset_valuation_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id,valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Asset Bank Building Fetched Successfully")

    #common.compare_dicts(post_asset_valuation_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Asset Bank Building using Valuation ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_of_policy_life_assurance_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_valuation_data,get_valuation_data_with_valuation_id ):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_policy_valuations = post_valuation_data(customer_id, policy_id, None, 'policies_life_assurance_valuation',
                                              True)
    post_policy_valuations_response = post_policy_valuations.json()
    logger.info(post_policy_valuations_response)
    common.check_reponse_message(post_policy_valuations_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Life Assurance Added Successfully")

    valuation_id = post_policy_valuations_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id, valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy Life Assurance Fetched Successfully")

    #common.compare_dicts(post_policy_valuations_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy Life Assurance using Valuation ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_of_policy_pension_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data,create_client, post_policy_data,post_valuation_data,get_valuation_data_with_valuation_id ):



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id ,None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pension Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_policy_valuations = post_valuation_data(customer_id, policy_id, None, 'policies_pensions_valuation',
                                              True)
    post_policy_valuations_response = post_policy_valuations.json()
    logger.info(post_policy_valuations_response)
    common.check_reponse_message(post_policy_valuations_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Pension Added Successfully")

    valuation_id = post_policy_valuations_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id, valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Pension Fetched Successfully")

    #common.compare_dicts(post_policy_valuations_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Pension using Valuation ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_of_policy_invest_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,data, post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_data_with_valuation_id ):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investments Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_policy_valuations = post_valuation_data(customer_id, policy_id, None, 'policies_investments_valuation',
                                              True)
    post_policy_valuations_response = post_policy_valuations.json()
    logger.info(post_policy_valuations_response)
    common.check_reponse_message(post_policy_valuations_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Policy Investments Added Successfully")

    valuation_id = post_policy_valuations_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id, valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy Investments Fetched Successfully")

    #common.compare_dicts(post_policy_valuations_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy Investments using Valuation ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_of_policy_income_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,data, post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_data_with_valuation_id ):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_policy_valuations = post_valuation_data(customer_id, policy_id, None, 'policies_income_protection_valuation',
                                              True)
    post_policy_valuations_response = post_policy_valuations.json()
    logger.info(post_policy_valuations_response)
    common.check_reponse_message(post_policy_valuations_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Policy Income Protection Added Successfully")

    valuation_id = post_policy_valuations_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id, valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy Income Protection Fetched Successfully")

    #common.compare_dicts(post_policy_valuations_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy Income Protection using Valuation ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_to_policy_health_assurance_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,data, post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_data_with_valuation_id ):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_policy_valuations = post_valuation_data(customer_id, policy_id, None, 'policies_health_assurance_valuation',
                                              True)
    post_policy_valuations_response = post_policy_valuations.json()
    logger.info(post_policy_valuations_response)
    common.check_reponse_message(post_policy_valuations_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Policy Health Assurance Added Successfully")

    valuation_id = post_policy_valuations_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id, valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy Health Assurance Fetched Successfully")

    #common.compare_dicts(post_policy_valuations_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy Health Assurance using Valuation ID Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_to_policy_general_valuations_using_valuation_id(partner_cust_id,customer_id,provider_correspondence_id,data, post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_data_with_valuation_id ):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_policy_valuations = post_valuation_data(customer_id, policy_id, None, 'policies_general_valuation',
                                              True)
    post_policy_valuations_response = post_policy_valuations.json()
    logger.info(post_policy_valuations_response)
    common.check_reponse_message(post_policy_valuations_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Policy General Added Successfully")

    valuation_id = post_policy_valuations_response['data']['valuation_id']

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id, valuation_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")

    #common.compare_dicts(post_policy_valuations_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy General using Valuation ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_general_valuations_data_with_invalid_valuation_id(customer_id,data, create_client, get_valuation_data_with_valuation_id):

    get_valuation_data = get_valuation_data_with_valuation_id(customer_id, "141d9ce8-5ac3-4c8c-8ab2-6ec22fd0fa31")
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_invalid_valuation_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")

    logger.info("Fetch Valuations Details For Policy General using Invalid Valuation ID Test Passed!")
