import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_asset_investment_withdrawal(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,
                                                    post_asset_withdrawal_data,patch_withdrawal_data ):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment asset
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create withdrawal for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, asset_id, None, 'asset_investment_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For Asset Investment Added Successfully")
    #logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id,asset_id, values,'asset_investment_withdrawals', False)
    update_withdrawal_data_response = update_withdrawal_data.json()
    common.check_reponse_message(update_withdrawal_data_response, expected_message)
    logger.info(update_withdrawal_data_response)
    logger.info("Withdrawal Details for life assurance Updated Successfully")

    logger.info("Update Investment withdrawal  Test Passed!")
    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_asset_share_holdings_withdrawals(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa,  field_values, create_client, post_asset_data,
                                                    post_asset_withdrawal_data, patch_withdrawal_data ):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment asset
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create withdrawal for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, asset_id, None, 'asset_share_holdings_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For asset share holdings  Added Successfully")
    #logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id,asset_id, values,'asset_share_holdings_withdrawals', False)
    update_withdrawal_data_response = update_withdrawal_data.json()
    common.check_reponse_message(update_withdrawal_data_response, expected_message)
    logger.info("Withdrawal Details for shareholdings Updated Successfully")

    logger.info("Update Share holdings Withdrawal  Test Passed!")
    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_asset_banks_building_societies_withdrawals(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,
                                                    post_asset_withdrawal_data,patch_withdrawal_data ):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment asset
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create withdrawal for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, asset_id, None, 'asset_banks_building_societies_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For Asset  Added Successfully")
    #logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id,asset_id, values,'asset_banks_building_societies_withdrawals', False)
    update_withdrawal_data_response = update_withdrawal_data.json()
    common.check_reponse_message(update_withdrawal_data_response, expected_message)
    logger.info("Withdrawal Details for Bank building societies Updated Successfully")

    logger.info("Update Asset withdrawal  Test Passed!")
    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")

    #withdrawl for policy


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_life_assurance_policy(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_asset_withdrawal_data,patch_withdrawal_data):

     create_client = create_client(data, None, True)
     create_client_response = create_client.json()
     common.check_reponse_message(create_client_response, constants.add_client_success_message)
     logger.info("Client Details Added Successfully")

     # provider post
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
     common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
     logger.info("Policy Details Added Successfully")
     # logger.info(post_policy_response )

     policy_id= post_policy_response['data']['policy_id']
     post_policy_withdrawal = post_asset_withdrawal_data(customer_id, policy_id, None,'policies_life_assurance_withdrawals', True)
     post_policy_withdrawal_response = post_policy_withdrawal.json()
     # logger.info(post_policy_withdrawal_response)
     common.check_reponse_message(post_policy_withdrawal_response, constants.add_asset_withdrawal_success_message)
     logger.info("Withdrawal Details  Added Successfully")

     withdrawal_id = post_policy_withdrawal_response['data']['withdrawal']['withdrawal_id']
     logger.info(policy_id)
     logger.info(withdrawal_id)
     logger.info(customer_id)
     values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_id') else
                 field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
                 field_values.get(field) != ''}
     expected_message = values.get(list(values)[-1])
     values.popitem()
     values.popitem()
     logger.info(values)
     update_withdrawal_data = patch_withdrawal_data(customer_id,withdrawal_id,policy_id,values,'policies_life_assurance_withdrawals', False)
     update_withdrawal_data_response = update_withdrawal_data.json()
     logger.info(update_withdrawal_data_response)
     common.check_reponse_message(update_withdrawal_data_response, expected_message)
     logger.info("Withdrawal Details for Life assurance policy Updated Successfully")

     logger.info("Update policy withdrawal  Test Passed!")
     get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
     get_withdrawal_response = get_withdrawal_data.json()
     logger.info(get_withdrawal_response)
     common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
     logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_pension_withdrawal_policy(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_asset_withdrawal_data,patch_withdrawal_data):

        create_client = create_client(data, None, True)
        create_client_response = create_client.json()
        common.check_reponse_message(create_client_response, constants.add_client_success_message)
        logger.info("Client Details Added Successfully")

        # provider post
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
        common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
        logger.info("Policy Details Added Successfully")

        policy_id = post_policy_response['data']['policy_id']
        post_policy_withdrawal = post_asset_withdrawal_data(customer_id, policy_id, None,'policies_pensions_withdrawals', True)
        post_policy_withdrawal_response = post_policy_withdrawal.json()
        common.check_reponse_message(post_policy_withdrawal_response, constants.add_asset_withdrawal_success_message)
        logger.info("Withdrawal Details   Added Successfully")

        withdrawal_id = post_policy_withdrawal_response['data']['withdrawal']['withdrawal_id']
        values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
                 field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
                 field_values.get(field) != ''}
        expected_message = values.get(list(values)[-1])
        values.popitem()
        values.popitem()
        update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id, policy_id, values,
                                                       'policies_pensions_withdrawals', False)
        update_withdrawal_data_response = update_withdrawal_data.json()
        common.check_reponse_message(update_withdrawal_data_response, expected_message)
        logger.info("Withdrawal Details for Pension policy Updated Successfully")

        logger.info("Update policy withdrawal  Test Passed!")
        get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
        get_withdrawal_response = get_withdrawal_data.json()
        logger.info(get_withdrawal_response)
        common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
        logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_investment_withdrawal_policy(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_asset_withdrawal_data,patch_withdrawal_data):

        create_client = create_client(data, None, True)
        create_client_response = create_client.json()
        common.check_reponse_message(create_client_response, constants.add_client_success_message)
        logger.info("Client Details Added Successfully")

        # provider post
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
        common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
        logger.info("Policy Details Added Successfully")

        policy_id = post_policy_response['data']['policy_id']
        post_policy_withdrawal = post_asset_withdrawal_data(customer_id, policy_id, None,'policies_investments_withdrawals', True)
        post_policy_withdrawal_response = post_policy_withdrawal.json()
        common.check_reponse_message(post_policy_withdrawal_response, constants.add_asset_withdrawal_success_message)
        logger.info("Withdrawal Details   Added Successfully")

        withdrawal_id = post_policy_withdrawal_response['data']['withdrawal']['withdrawal_id']
        values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
                 field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
                 field_values.get(field) != ''}
        expected_message = values.get(list(values)[-1])
        values.popitem()
        values.popitem()
        update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id, policy_id, values,
                                                       'policies_investments_withdrawals', False)
        update_withdrawal_data_response = update_withdrawal_data.json()
        common.check_reponse_message(update_withdrawal_data_response, expected_message)
        logger.info("Withdrawal Details for Investment policy Updated Successfully")

        logger.info("Update policy withdrawal  Test Passed!")
        get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
        get_withdrawal_response = get_withdrawal_data.json()
        logger.info(get_withdrawal_response)
        common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
        logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")



@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_savings_withdrawal_policy(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_asset_withdrawal_data,patch_withdrawal_data):

        create_client = create_client(data, None, True)
        create_client_response = create_client.json()
        common.check_reponse_message(create_client_response, constants.add_client_success_message)
        logger.info("Client Details Added Successfully")

        # provider post
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

        post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
        post_policy_response = post_policy.json()
        common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
        logger.info("Policy Details Added Successfully")

        policy_id = post_policy_response['data']['policy_id']
        post_policy_withdrawal = post_asset_withdrawal_data(customer_id, policy_id, None,'policies_savings_plans_withdrawals', True)
        post_policy_withdrawal_response = post_policy_withdrawal.json()
        common.check_reponse_message(post_policy_withdrawal_response, constants.add_asset_withdrawal_success_message)
        logger.info("Withdrawal Details   Added Successfully")

        withdrawal_id = post_policy_withdrawal_response['data']['withdrawal']['withdrawal_id']
        values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
                 field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
                 field_values.get(field) != ''}
        expected_message = values.get(list(values)[-1])
        values.popitem()
        values.popitem()
        update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id, policy_id, values,
                                                       'policies_savings_plans_withdrawals', False)
        update_withdrawal_data_response = update_withdrawal_data.json()
        common.check_reponse_message(update_withdrawal_data_response, expected_message)
        logger.info("Withdrawal Details for Savings policy Updated Successfully")

        logger.info("Update policy withdrawal  Test Passed!")
        get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
        get_withdrawal_response = get_withdrawal_data.json()
        logger.info(get_withdrawal_response)
        common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
        logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_health_withdrawal_policy(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_asset_withdrawal_data,patch_withdrawal_data):

        create_client = create_client(data, None, True)
        create_client_response = create_client.json()
        common.check_reponse_message(create_client_response, constants.add_client_success_message)
        logger.info("Client Details Added Successfully")

        # provider post
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
        common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
        logger.info("Policy Details Added Successfully")

        policy_id = post_policy_response['data']['policy_id']
        post_policy_withdrawal = post_asset_withdrawal_data(customer_id, policy_id, None,'policies_health_assurance_withdrawals', True)
        post_policy_withdrawal_response = post_policy_withdrawal.json()
        common.check_reponse_message(post_policy_withdrawal_response, constants.add_asset_withdrawal_success_message)
        logger.info("Withdrawal Details   Added Successfully")

        withdrawal_id = post_policy_withdrawal_response['data']['withdrawal']['withdrawal_id']
        values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
                 field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
                 field_values.get(field) != ''}
        expected_message = values.get(list(values)[-1])
        values.popitem()
        values.popitem()
        update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id, policy_id, values,
                                                       'policies_health_assurance_withdrawals', False)
        update_withdrawal_data_response = update_withdrawal_data.json()
        common.check_reponse_message(update_withdrawal_data_response, expected_message)
        logger.info("Withdrawal Details for Health assurance policy Updated Successfully")

        logger.info("Update policy withdrawal  Test Passed!")
        get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
        get_withdrawal_response = get_withdrawal_data.json()
        logger.info(get_withdrawal_response)
        common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
        logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_income_withdrawal_policy(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_asset_withdrawal_data,patch_withdrawal_data):

        create_client = create_client(data, None, True)
        create_client_response = create_client.json()
        common.check_reponse_message(create_client_response, constants.add_client_success_message)
        logger.info("Client Details Added Successfully")

        # provider post
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
        common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
        logger.info("Policy Details Added Successfully")

        policy_id = post_policy_response['data']['policy_id']
        post_policy_withdrawal = post_asset_withdrawal_data(customer_id, policy_id, None,'policies_income_protection_withdrawals', True)
        post_policy_withdrawal_response = post_policy_withdrawal.json()
        common.check_reponse_message(post_policy_withdrawal_response, constants.add_asset_withdrawal_success_message)
        logger.info("Withdrawal Details   Added Successfully")

        withdrawal_id = post_policy_withdrawal_response['data']['withdrawal']['withdrawal_id']
        values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
                 field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
                 field_values.get(field) != ''}
        expected_message = values.get(list(values)[-1])
        values.popitem()
        values.popitem()
        update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id, policy_id, values,
                                                       'policies_income_protection_withdrawals', False)
        update_withdrawal_data_response = update_withdrawal_data.json()
        common.check_reponse_message(update_withdrawal_data_response, expected_message)
        logger.info("Withdrawal Details for Income protection policy Updated Successfully")

        logger.info("Update policy withdrawal  Test Passed!")
        get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
        get_withdrawal_response = get_withdrawal_data.json()
        logger.info(get_withdrawal_response)
        common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
        logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Withdrawal/test_data_asset_withdrawals.csv"))
def test_update_general_withdrawal_policy(post_partner_data,get_withdrawal_data_with_withdrawal_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_asset_withdrawal_data,patch_withdrawal_data):

        create_client = create_client(data, None, True)
        create_client_response = create_client.json()
        common.check_reponse_message(create_client_response, constants.add_client_success_message)
        logger.info("Client Details Added Successfully")

        # provider post
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
        common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
        logger.info("Policy Details Added Successfully")

        policy_id = post_policy_response['data']['policy_id']
        post_policy_withdrawal = post_asset_withdrawal_data(customer_id, policy_id, None,'policies_general_withdrawals', True)
        post_policy_withdrawal_response = post_policy_withdrawal.json()
        common.check_reponse_message(post_policy_withdrawal_response, constants.add_asset_withdrawal_success_message)
        logger.info("Withdrawal Details   Added Successfully")

        withdrawal_id = post_policy_withdrawal_response['data']['withdrawal']['withdrawal_id']
        values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
                 field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
                 field_values.get(field) != ''}
        expected_message = values.get(list(values)[-1])
        values.popitem()
        values.popitem()
        update_withdrawal_data = patch_withdrawal_data(customer_id, withdrawal_id, policy_id, values,
                                                       'policies_general_withdrawals', False)
        update_withdrawal_data_response = update_withdrawal_data.json()
        common.check_reponse_message(update_withdrawal_data_response, expected_message)
        logger.info("Withdrawal Details for general policy Updated Successfully")

        logger.info("Update policy withdrawal  Test Passed!")
        get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
        get_withdrawal_response = get_withdrawal_data.json()
        logger.info(get_withdrawal_response)
        common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
        logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")

