import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_investment_payment_commission_data_using_commission_id(customer_id,partner_cust_id, provider_correspondence_id,data, post_system_manager_data, dataa, create_client, post_asset_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_commission_id ):
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
    logger.info("Asset Payment Commission Details For Investment Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id,commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Asset Investment using Commission ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_share_holdings_commission_data_using_commission_id(customer_id,partner_cust_id, provider_correspondence_id,data, post_system_manager_data, dataa, create_client, post_asset_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_commission_id ):
    post_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Share Holdings Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_share_holdings_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Share Holdings Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, asset_id, payment_id, None,
                                                 'asset_share_holdings_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Asset Payment Commission Details For Share Holdings Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id,commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Share Holdings Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Asset Share Holdings using Commission ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_banks_building_data_using_commission_id(customer_id, partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_commission_id ):
    post_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_banks_building_societies_asset',
                                 True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Banks/Building Societies Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_banks_building_societies_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Banks Building Societies Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, asset_id, payment_id, None,
                                                 'asset_banks_building_societies_payment_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Asset Payment Commission Details For Banks Building Societies Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id,commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Banks Building Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Asset Banks Building using Commission ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_from_liabilities_mortgages_payment_commission(customer_id, partner_cust_id,provider_correspondence_id,data, post_system_manager_data, dataa, create_client, post_liability_data,
                                                       post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):
    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Mortgages Liability Details For Liability Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_mortgages_payment', True)
    post_mortgage_response = post_mortgage.json()
    logger.info(post_mortgage_response)
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For Mortgages Added Successfully")

    payment_id = post_mortgage_response['data']['Payment_id']
    post_comission = post_asset_commission_data(customer_id, liability_id, payment_id, None,
                                                    'liabilities_mortgages_payment_commission', True)
    post_commission_response = post_comission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Liability Payment Commission Details For Mortgages Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Liability Mortgages Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Liability Mortgages using Commission ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_from_liabilities_loan_hire_payment_commission(customer_id,partner_cust_id, provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_liability_data,
                                                       post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):
    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Loan Hire Purchase Details For Liability Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_loan_hire_purchase_payments', True)
    post_mortgage_response = post_mortgage.json()
    logger.info(post_mortgage_response)
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For Loan Hire Purchase Added Successfully")

    payment_id = post_mortgage_response['data']['Payment_id']
    post_comission = post_asset_commission_data(customer_id, liability_id, payment_id, None,
                                                    'liabilities_loan_hire_purchase_payments_commission', True)
    post_commission_response = post_comission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Liability Payment Commission Details For Loan Hire Purchase Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Liability Loan Hire Purchase Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Liability Loan Hire Purchase using Commission ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_from_liabilities_credit_card_payment_commission(customer_id,partner_cust_id, provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_liability_data,
                                                       post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):
    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Credit cards Details For Liability Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_credit_cards_payments', True)
    post_mortgage_response = post_mortgage.json()
    logger.info(post_mortgage_response)
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For Credit Card Added Successfully")

    payment_id = post_mortgage_response['data']['Payment_id']
    post_comission = post_asset_commission_data(customer_id, liability_id, payment_id, None,
                                                    'liabilities_credit_cards_payments_commission', True)
    post_commission_response = post_comission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Liability Payment Commission Details For Credit Card Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Liability  Credit Card Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Liability  Credit Card using Commission ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_from_policies_life_assurance_payment_commission(customer_id,partner_cust_id, provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                         post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_life_assurance_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    logger.info(post_life_assurance_response)
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Life Assurance Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                    'policies_life_assurance_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Policy Payment Commission Details For Life Assurance Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy Life Assurance Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy Life Assurance using Commission ID Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_from_policies_pension_payment_commission(customer_id,partner_cust_id, provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                         post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_pensions_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    logger.info(post_life_assurance_response)
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Pensions Added Successfullys")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                    'policies_pensions_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Policy Payment Commission Details For Pensions Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy Pensions Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy Pensions using Commission ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_from_policies_investment_payment_commission(customer_id,partner_cust_id, provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                         post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investments Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_investments_payments', True)
    post_life_assurance_response = post_life_assurance.json()
    logger.info(post_life_assurance_response)
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Investments Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                    'policies_investments_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Policy Payment Commission Details For Investments Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy Investments Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy Investments using Commission ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_from_policies_savingsplan_payment_commission(customer_id,partner_cust_id, provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                         post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Plan Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_savings_plans_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    logger.info(post_life_assurance_response)
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Savings Plan Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                    'policies_savings_plans_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Policy Payment Commission Details For Savings Plan Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy Payment Commission Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy Payment Commission using Commission ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_from_policies_income_payment_commission(customer_id,partner_cust_id, provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                         post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_income_protection_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    logger.info(post_life_assurance_response)
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Income Protection Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                    'policies_income_protection_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Policy Payment Commission Details For Income Protection Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['commission']['payment_id']
    # case_id = post_commission_response['data']['commission']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy Income Protection Commission Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy Income Protection using Commission ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_from_policies__general_payment_commission(customer_id,partner_cust_id, provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                         post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_commission_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_general_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    logger.info(post_life_assurance_response)
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For General Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                    'policies_general_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Policy Payment Commission Details For General Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    # payment_id = post_commission_response['data']['payment_id']
    # case_id = post_commission_response['data']['case_id']

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy General Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy General using Commission ID Test Passed!")



@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_commission_using_invalid_commission_id(customer_id, data, create_client, post_asset_data,
                                                         get_asset_commission_data_with_commission_id):

    get_commission_data = get_asset_commission_data_with_commission_id(customer_id,"aff44303-74fa-4ba6-b18d-b6bd68f0725a")
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_invalid_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy General Fetched Successfully")
    logger.info("Fetch Commission Details using Invalid Commission ID Test Passed!")

