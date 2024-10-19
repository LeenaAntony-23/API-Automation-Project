import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_life_assurance_policy.csv"))
def test_add_all_data_to_life_assurance_policy(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data):


    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'policies_life_assurance_policy', False)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, expected_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    logger.info("Add Data To Life Assurance Policy Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_pensions_policy.csv"))
def test_add_all_data_to_pensions_policy(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'policies_pensions_policy', False)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, expected_message)
    logger.info("Policy Details For Pensions Added Successfully")

    logger.info("Add Data To Pension Policy Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_investments_policy.csv"))
def test_add_all_data_to_investments_policy(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'policies_investments_policy', False)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, expected_message)
    logger.info("Policy Details For Investment Added Successfully")

    logger.info("Add Data To Investment Policy Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_savings_plans_policy.csv"))
def test_add_all_data_to_savings_plans_policy(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'policies_savings_plans_policy', False)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, expected_message)
    logger.info("Policy Details For Savings Plan Added Successfully")

    logger.info("Add Data To Savings Plan Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_income_protection_policy.csv"))
def test_add_all_data_to_income_protection_policy(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'policies_income_protection_policy', False)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, expected_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    logger.info("Add Data To Income Protection Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_health_assurance_policy.csv"))
def test_add_all_data_to_health_assurance_policy(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'policies_health_assurance_policy', False)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, expected_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    logger.info("Add Data To Health Assurance Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Policy/test_data_general_policy.csv"))
def test_add_all_data_to_general_policy(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'policies_general_policy', False)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, expected_message)
    logger.info("Policy Details For General Added Successfully")

    logger.info("Add Data To General Policy Test Passed!")
