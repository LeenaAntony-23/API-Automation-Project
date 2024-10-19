import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_single_life_assurance_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Life Assurance Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_multiple_life_assurance_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Life Assurance Details Added Successfully")
    policy_id_1 = post_policy_response['data']['policy_id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Life Assurance Details Added Successfully")
    policy_id_2 = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("First and Second Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("First Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Second Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id_1 not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_single_pension_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Pension Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_multiple_pension_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Pension Details Added Successfully")
    policy_id_1 = post_policy_response['data']['policy_id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy pension Details Added Successfully")
    policy_id_2 = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("First and Second Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("First Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Second Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id_1 not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_single_investments_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Investment Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_multiple_investment_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy investment Details Added Successfully")
    policy_id_1 = post_policy_response['data']['policy_id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Investment Details Added Successfully")
    policy_id_2 = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("First and Second Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("First Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Second Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id_1 not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_single_savings_plan_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Savings Plan Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_multiple_savings_plan_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Savings Plan Details Added Successfully")
    policy_id_1 = post_policy_response['data']['policy_id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Savings Plan Details Added Successfully")
    policy_id_2 = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("First and Second Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("First Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Second Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id_1 not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_single_income_protection_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Income Protection Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_multiple_income_protection_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Income Protection Details Added Successfully")
    policy_id_1 = post_policy_response['data']['policy_id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Income Protection Details Added Successfully")
    policy_id_2 = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("First and Second Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("First Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Second Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id_1 not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_single_health_assurance_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Health Assurance Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_multiple_health_assurance_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Health Assurance Details Added Successfully")
    policy_id_1 = post_policy_response['data']['policy_id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Health assurance Details Added Successfully")
    policy_id_2 = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("First and Second Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("First Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Second Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id_1 not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_single_general_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Health Assurance Details Added Successfully")
    policy_id = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_multiple_general_policy(delete_case_details,post_system_manager_data,dataa,data, create_client, post_policy_data,
                                                          get_policy_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Health Assurance Details Added Successfully")
    policy_id_1 = post_policy_response['data']['policy_id']

    # Create policy using json data
    post_policy = post_policy_data(customer_id, None, provider_correspondence_id, None,
                                   'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Health assurance Details Added Successfully")
    policy_id_2 = post_policy_response['data']['policy_id']

    #  Fetch policy data before deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    policy_response = policy_details.json()
    logger.info(policy_response)
    common.check_reponse_message(policy_response, constants.get_policy_success_message)
    logger.info("First and Second Policy Details Fetched Successfully")

    #  Delete first policy details
    delete_client_data = delete_case_details('policy', policy_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_policy_success_message)
    logger.info("First Policy Details Deleted Successfully")

    #  Fetch asset data after deletion
    policy_details = get_policy_data_with_customer_id(customer_id)
    get_client_response_after = policy_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_policy_invalid_message)
    logger.info("Second Policy Details Fetched Successfully")

    policy_after = get_client_response_after['data']
    assert policy_id_1 not in [data['policy_id'] for data in
                            policy_after], "Policy ID is not deleted from the response"

    logger.info("Confirmed that Policy data has been deleted successfully.")
