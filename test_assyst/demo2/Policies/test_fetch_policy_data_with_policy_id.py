import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                     get_policy_data_with_policy_id):



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None,'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    policy_details = get_policy_data_with_policy_id(policy_id, customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Fetch Policy Data Of One Customer Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_policies_pensions_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                     get_policy_data_with_policy_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None,'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    policy_details = get_policy_data_with_policy_id(policy_id, customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Fetch Policy Data Of One Customer Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_policies_investments_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                     get_policy_data_with_policy_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None,'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    policy_details = get_policy_data_with_policy_id(policy_id, customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Fetch Policy Data Of One Customer Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_policies_savings_plans_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                                          get_policy_data_with_policy_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    policy_details = get_policy_data_with_policy_id(policy_id, customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Fetch Policy Data Of One Customer Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_policies_income_protection_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                                          get_policy_data_with_policy_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    policy_details = get_policy_data_with_policy_id(policy_id, customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Fetch Policy Data Of One Customer Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_policies_health_assurance_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                                          get_policy_data_with_policy_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    policy_details = get_policy_data_with_policy_id(policy_id, customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Fetch Policy Data Of One Customer Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_policies_general_policy_data_with_policy_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                                          get_policy_data_with_policy_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    policy_details = get_policy_data_with_policy_id(policy_id, customer_id)
    policy_response = policy_details.json()
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    logger.info("Fetch Policy Data Of One Customer Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policy_data_with_invalid_policy_id(customer_id,data, create_client, get_policy_data_with_policy_id):

    get_policy_data = get_policy_data_with_policy_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0', customer_id)
    get_policy_response = get_policy_data.json()
    common.check_reponse_message(get_policy_response, constants.invalid_policy_message)
    assert get_policy_response["isError"] is False
    logger.info("Fetch Asset Data With Invalid Policy ID Test Passed!")

