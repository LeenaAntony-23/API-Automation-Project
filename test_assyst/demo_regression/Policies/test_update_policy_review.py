import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_policy_review.csv"))
def test_update_policies_life_assurance_review_(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_review_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, "policies_life_assurance_policy", True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    logger.info(policy_id)
    case_id = policy_id
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_policy_review_data(customer_id,case_id, values, "policies_life_assurance_review", False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Policy Details for Life Assurance Review Updated Successfully")

    logger.info("Update Policy Life Assurance Review Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_policy_review.csv"))
def test_update_policies_pensions_review_(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_review_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, "policies_pensions_policy", True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    case_id = policy_id
    logger.info(policy_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_policy_review_data(customer_id,case_id, values, "policies_pensions_review", False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Policy Details for Pension Review Updated Successfully")

    logger.info("Update Policy Pension Review Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_policy_review.csv"))
def test_update_policies_investments_review_(partner_cust_id,customer_id,provider_correspondence_id, post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_review_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, "policies_investments_policy", True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    case_id = policy_id
    logger.info(policy_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_policy_review_data(customer_id,case_id, values, "policies_investments_review", False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Policy Details for Investments Review Updated Successfully")

    logger.info("Update Policy Investments Review Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_policy_review.csv"))
def test_update_policies_savings_plans_review_(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_review_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, "policies_savings_plans_policy", True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    case_id=policy_id
    logger.info(policy_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_policy_review_data(customer_id,case_id, values, "policies_savings_plans_review", False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Policy Details for Savings Plan Review Updated Successfully")

    logger.info("Update Policy Savings Plan Review Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_policy_review.csv"))
def test_update_policies_income_protection_review_(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_review_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, "policies_income_protection_policy", True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    case_id=policy_id
    logger.info(policy_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_policy_review_data(customer_id,case_id, values, "policies_income_protection_review", False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Policy Details for Income Protection Review Updated Successfully")

    logger.info("Update Policy Income Protection Review Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_policy_review.csv"))
def test_update_policies_health_assurance_review_(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_review_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, "policies_health_assurance_policy", True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    case_id=policy_id
    logger.info(policy_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_policy_review_data(customer_id,case_id, values, "policies_health_assurance_review", False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Policy Details for Health Assurance Review Updated Successfully")

    logger.info("Update Policy Health Assurance Review Test Passed!")



@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_policy_review.csv"))
def test_update_policies_general_review_(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,patch_policy_review_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, "policies_general_policy", True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    case_id=policy_id
    logger.info(policy_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    update_policy_data = patch_policy_review_data(customer_id,case_id, values, "policies_general_review", False)
    update_policy_data_response = update_policy_data.json()
    common.check_reponse_message(update_policy_data_response, expected_message)
    logger.info("Policy Details for General Review Updated Successfully")

    logger.info("Update Policy General Review Test Passed!")



