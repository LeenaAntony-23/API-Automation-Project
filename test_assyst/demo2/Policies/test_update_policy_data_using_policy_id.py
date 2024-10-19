import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_life_assurance_policy.csv"))
def test_create_and_update_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,get_policy_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None,'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
             field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
             field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_policy_data = patch_policy_data(provider_correspondence_id,customer_id, policy_id, values, 'policies_life_assurance_policy', False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("policy Details for life assurance Updated Successfully")

    logger.info("Update policy life assurance Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_pensions_policy.csv"))
def test_update_pension_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,get_policy_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, patch_policy_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None,'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")
    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
            field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
            field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_policy_data = patch_policy_data(provider_correspondence_id,customer_id, policy_id, values, 'policies_pensions_policy', False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("policy Details for pension Updated Successfully")

    logger.info("Update policy pension Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_investments_policy.csv"))
def test_update_investment_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,get_policy_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
             field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
             field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_policy_data = patch_policy_data(provider_correspondence_id,customer_id, policy_id, values, 'policies_investments_policy', False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("policy Details for Investment policy Updated Successfully")

    logger.info("Update policy Investment Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_savings_plans_policy.csv"))
def test_update_savings_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,get_policy_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, patch_policy_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_policy_data = patch_policy_data(provider_correspondence_id,customer_id, policy_id, values, 'policies_savings_plans_policy', False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("policy Details for Savings policy Updated Successfully")

    logger.info("Update policy savings Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_income_protection_policy.csv"))
def test_update_income_protection_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,get_policy_data_with_customer_id,dataa,data, field_values, create_client, post_policy_data,
                                                   patch_policy_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_policy_data = patch_policy_data(provider_correspondence_id,customer_id, policy_id, values, 'policies_income_protection_policy', False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("policy Details for Income protection policy Updated Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Update policyIncome Protection Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_health_assurance_policy.csv"))
def test_update_health_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,get_policy_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, patch_policy_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")
    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_policy_data = patch_policy_data(provider_correspondence_id,customer_id, policy_id, values, 'policies_health_assurance_policy', False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("policy Details for Health assurance policy Updated Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Update policy Health assurance Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_general_policy.csv"))
def test_update_general_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,get_policy_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, patch_policy_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None,'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_policy_data = patch_policy_data(provider_correspondence_id,customer_id, policy_id, values, 'policies_general_policy', False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("policy Details for General policy Updated Successfully")
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Update policy General Test Passed!")
