import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_asset_investment_withdrawals(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,
                                                      post_asset_withdrawal_data):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    # asset_id = "2755c563-ca34-49ba-8f73-c4205a8b6a89"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_withdrawal_data(customer_id, asset_id, values, 'asset_investment_withdrawals', False)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Asset Withdrawal Details For Investment Added Successfully")

    logger.info("Add Data To Asset Investment Withdrawal Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_asset_share_holdings_withdrawals(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,
                                                          post_asset_withdrawal_data):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Share Holdings Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    # asset_id = "7340f3df-61d9-4478-a904-f79bd4e6961b"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_withdrawal_data(customer_id, asset_id, values, 'asset_share_holdings_withdrawals', False)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Asset Withdrawal Details For Share Holdings Added Successfully")

    logger.info("Add Data To Asset Share Holdings Withdrawal Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_asset_banks_building_societies_withdrawals(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,
                                                                    post_asset_withdrawal_data):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Banks Building Societies Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    # asset_id = "90ec8727-5769-4140-ad88-afdf30dc37a7"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_withdrawal_data(customer_id, asset_id, values, 'asset_banks_building_societies_withdrawals', False)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Asset Withdrawal Details For Share Holdings Added Successfully")

    logger.info("Add Data To Asset Banks Building Societies Withdrawal Test Passed!")

#
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_policies_life_assurance_withdrawal(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, field_values, create_client, post_policy_data,
                                                         post_asset_withdrawal_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    # policy_id ="ef01c2b9-e427-4c87-af44-d90e86ae25eb"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_life_assurance = post_asset_withdrawal_data(customer_id, policy_id, values,
                                                  'policies_life_assurance_withdrawals', False)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, expected_message)
    logger.info("Asset Withdrawal Details For Life Assurance Added Successfully")

    logger.info("Add Data To Policy Life Assurance Withdrawal Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_policies_pensions_withdrawal(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                   post_asset_withdrawal_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")


    policy_id = post_policy_response['data']['policy_id']
    # policy_id ="3633231d-64fa-4d56-b01d-5829b9d0d669"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_pension = post_asset_withdrawal_data(customer_id, policy_id, values, 'policies_pensions_withdrawals', False)
    post_pension_response = post_pension.json()
    common.check_reponse_message(post_pension_response, expected_message)
    logger.info("Asset Withdrawal Details For Pensions Added Successfully")

    logger.info("Add Data To Policy Pensions Withdrawal Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_policies_investments_withdrawal(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                       post_asset_withdrawal_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investment Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    # policy_id= "3272f256-ef5d-4978-a3ab-966d9a4809dd"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_investment = post_asset_withdrawal_data(customer_id, policy_id, values, 'policies_investments_withdrawals', False)
    post_investment_response = post_investment.json()
    common.check_reponse_message(post_investment_response, expected_message)
    logger.info("Asset Withdrawal Details For Investment Added Successfully")

    logger.info("Add Data To Policy Investment Withdrawal Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_policies_savings_plans_withdrawal(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                        post_asset_withdrawal_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Plan Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    # policy_id = "e5c718ce-42e1-4b30-9366-6c7fa29bd12b"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_savings_plan = post_asset_withdrawal_data(customer_id, policy_id, values, 'policies_savings_plans_withdrawals', False)
    post_savings_plan_response = post_savings_plan.json()
    common.check_reponse_message(post_savings_plan_response, expected_message)
    logger.info("Asset Withdrawal Details For Savings Plan Added Successfully")

    logger.info("Add Data To Policy Savings Plan Withdrawal Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_policies_income_protection_withdrawal(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, field_values, create_client, post_policy_data,
                                                            post_asset_withdrawal_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id,  None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    # policy_id ="9297e0f8-e8d0-4f25-ad3f-3cfb1c222ccf"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_income_protection = post_asset_withdrawal_data(customer_id, policy_id, values,
                                                        'policies_income_protection_withdrawals', False)
    post_income_protection_response = post_income_protection.json()
    logger.info(post_income_protection_response)
    common.check_reponse_message(post_income_protection_response, expected_message)
    logger.info("Asset Withdrawal Details For Income Protection Added Successfully")

    logger.info("Add Data To Policy Income Protection Withdrawal Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_policies_health_assurance_withdrawal(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                           post_asset_withdrawal_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    # policy_id ="e1de03b2-b904-45fc-97a7-1b0ace78af11"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_health_assurance = post_asset_withdrawal_data(customer_id, policy_id, values,
                                                       'policies_health_assurance_withdrawals', False)
    post_health_assurance_response = post_health_assurance.json()
    common.check_reponse_message(post_health_assurance_response, expected_message)
    logger.info("Asset Withdrawal Details For Health Assurance Added Successfully")

    logger.info("Add Data To Policy Health Assurance Withdrawal Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Withdrawal/"
                                                         "test_data_asset_withdrawals.csv"))
def test_add_all_data_to_policies_general_withdrawal(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, field_values, create_client, post_policy_data,
                                                  post_asset_withdrawal_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    # policy_id ="eb8ffac6-03cf-420b-ad25-c0410a7629f3"
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_general = post_asset_withdrawal_data(customer_id, policy_id, values, 'policies_general_withdrawals', False)
    post_general_response = post_general.json()
    common.check_reponse_message(post_general_response, expected_message)
    logger.info("Asset Withdrawal Details For General Added Successfully")

    logger.info("Add Data To Policy General Withdrawal Test Passed!")