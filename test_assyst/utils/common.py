import json
import logging
import configparser
import csv
from datetime import datetime

import faker

#import faker

logger = logging.getLogger('my_logger')

# Global variables
extra_fields = ['case_type', 'provider_correspondence', 'total_fund_value', 'link_to_mortgage', 'review_date',
                'review_interval', 'review_completed', 'review_note', 'review_assigned']


def update_outgoing_json_data(customer_id=None):
    if customer_id is not None:
        json_file_path = "./jsons/create_new_outgoing.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        json_data["outgoings"]["customer_id"] = customer_id

        payload = json.dumps(json_data)
        return payload

def update_commission_json_data(customer_id=None):
    if customer_id is not None:
        json_file_path = "./jsons/create_new_commission.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        json_data["fees_charges"]["customer_id"] = customer_id

        payload = json.dumps(json_data)
        return payload


def update_profile_data():

        json_file_path = "./jsons/create_client_profile.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)


        payload = json.dumps(json_data)
        return payload

def update_email_json_data(customer_id):
    fake = faker.Faker()
    json_file_path = "./jsons/create_new_email_post.json"
    with open(json_file_path, "r") as file:
        json_data = json.load(file)
    logger.info(json_data)
    json_data["to"] = [customer_id]
    json_data["notificationId"] =fake.uuid4()
    payload = json.dumps(json_data)
    logger.info(payload)
    return payload

def update_notes_json_data(customer_id=None):
    if customer_id is not None:
        json_file_path = "./jsons/create_client_notes.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)

        json_data["customer_id"] = customer_id

        payload = json.dumps(json_data)

        return payload

def update_fact_find_notes_json_data(customer_id=None):
    if customer_id is not None:
        json_file_path = "./jsons/create_client_factfind_notes.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)

        json_data["customer_id"] = customer_id

        payload = json.dumps(json_data)
        return payload


def update_portfolionetworth_data(customer_id):
    json_file_path = "./jsons/create_new_networth_report.json"
    with open(json_file_path, "r") as file:
        json_data = json.load(file)

    json_data["customerId"] = customer_id

    payload = json.dumps(json_data)
    return payload

def update_all_client_report_data():
    json_file_path = "./jsons/create_new_report_allclient.json"
    with open(json_file_path, "r") as file:
        json_data = json.load(file)



    payload = json.dumps(json_data)
    return payload


def update_timeallocation_json_data(customer_id=None):
    if customer_id is not None:
        json_file_path = "./jsons/create_new_timeallocation.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        json_data["contacts_time_allocation"]["customer_id"] = customer_id

        payload = json.dumps(json_data)
        return payload


def update_patch_data(file, data):
    with open(file, "r") as file:
        json_data = json.load(file)
    for i, j in data.items():
        json_data["name_and_address"][i] = j
    payload = json.dumps(json_data)
    return payload


def update_dependant_json_data(customer_id=None):
    if customer_id is not None:
        json_file_path = "./jsons/create_new_dependant.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        json_data["dependants"]["customer_id"] = customer_id

        payload = json.dumps(json_data)
        return payload

def update_document_folder_json_data(customer_id=None):
    if customer_id is not None:
        json_file_path = "./jsons/create_new_document_folder.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        # Get the current date and time
        now = datetime.now()
        # Convert datetime object to string
        date_string = now.strftime("%Y-%m-%d %H:%M:%S")
        json_data["customer_id"] = customer_id
        json_data["folderName"] = customer_id+"/"+date_string+"/"

        payload = json.dumps(json_data)
        logger.info(payload)

        return payload


def update_document_file_json_data(customer_id,foldername):

        json_file_path = "./jsons/create_new_document_folder_file.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)


        json_data["customer_id"] = customer_id
        json_data["folderName"] = foldername

        payload = json.dumps(json_data)
        logger.info(payload)
        return payload


# def update_asset_json_data(customer_id=None, context=None):
#     if customer_id is not None:
#         data = {}
#         json_file_path = "./jsons/create_new_asset.json"
#         with open(json_file_path, "r") as file:
#             json_data = json.load(file)
#         if context == None:
#             json_data["asset_investment_asset"]["customer_id"] = customer_id
#             json_data["asset_investment_asset"]["case_type"] = "3"
#             json_data["asset_share_holdings_asset"]["customer_id"] = customer_id
#             json_data["asset_share_holdings_asset"]["case_type"] = "1"
#             json_data["asset_home_personal_asset"]["customer_id"] = customer_id
#             json_data["asset_home_personal_asset"]["case_type"] = "2"
#             json_data["asset_banks_building_societies_asset"]["customer_id"] = customer_id
#             json_data["asset_banks_building_societies_asset"]["case_type"] = "0"
#             data = json_data
#         elif context == "asset_investment_asset":
#             json_data["asset_investment_asset"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "asset_share_holdings_asset":
#             json_data["asset_share_holdings_asset"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "asset_home_personal_asset":
#             json_data["asset_home_personal_asset"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "asset_banks_building_societies_asset":
#             json_data["asset_banks_building_societies_asset"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         else:
#             logger.error("Context Not Implemented")
#         payload = json.dumps(data)
#         return payload

def update_client_action_json_data(customer_id=None):
    if customer_id is not None:
        json_file_path = "./jsons/create_client_contexts.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        json_data["contacts_client_action"]["customer_id"] = customer_id

        payload = json.dumps(json_data)
        return payload

def update_asset_json_data(provider_correspondence_id, customer_id=None, context=None):
    if customer_id is not None:
        data = {}
        json_file_path = "./jsons/create_new_asset.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)

        if context == None:
            json_data["asset_investment_asset"]["customer_id"] = customer_id
            json_data["asset_investment_asset"]["case_type"] = "3"
            json_data["asset_share_holdings_asset"]["customer_id"] = customer_id
            json_data["asset_share_holdings_asset"]["case_type"] = "1"
            json_data["asset_home_personal_asset"]["customer_id"] = customer_id
            json_data["asset_home_personal_asset"]["case_type"] = "2"
            json_data["asset_banks_building_societies_asset"]["customer_id"] = customer_id
            json_data["asset_banks_building_societies_asset"]["case_type"] = "0"
            data = json_data
        elif context == "asset_investment_asset":
            json_data["asset_investment_asset"]["customer_id"] = customer_id
            json_data["asset_investment_asset"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "asset_share_holdings_asset":
            json_data["asset_share_holdings_asset"]["customer_id"] = customer_id
            json_data["asset_share_holdings_asset"]["provider_correspondence"] = provider_correspondence_id

            data.update({context: json_data[context]})
        elif context == "asset_home_personal_asset":
            json_data["asset_home_personal_asset"]["customer_id"] = customer_id
            json_data["asset_home_personal_asset"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "asset_banks_building_societies_asset":
            json_data["asset_banks_building_societies_asset"]["customer_id"] = customer_id
            json_data["asset_banks_building_societies_asset"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")


        payload = json.dumps(data)
        return payload


def update_liability_json_data(customer_id,provider_correspondence_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_new_liability.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            json_data["liabilities_mortgages_liability"]["customer_id"] = customer_id
            ["liabilities_mortgages_liability"]["provider_id"] = customer_id
            json_data["liabilities_mortgages_liability"]["provider_correspondence"] = provider_correspondence_id
            json_data["liabilities_mortgages_liability"]["case_type"] = 'Mortgages'
            json_data["liabilities_loan_hire_purchase_liability"]["customer_id"] = customer_id
            json_data["liabilities_loan_hire_purchase_liability"]["provider_correspondence"] = provider_correspondence_id
            json_data["liabilities_loan_hire_purchase_liability"]["case_type"] = 'Loans/Lease/HP'
            json_data["liabilities_credit_cards_liability"]["customer_id"] = customer_id
            json_data["liabilities_credit_cards_liability"]["provider_correspondence"] = provider_correspondence_id
            json_data["liabilities_credit_cards_liability"]["case_type"] = 'Credit Cards'
            data = json_data
        elif context == "liabilities_mortgages_liability":
            json_data["liabilities_mortgages_liability"]["customer_id"] = customer_id
            #json_data["liabilities_mortgages_liability"]["provider_id"] = customer_id
            json_data["liabilities_mortgages_liability"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "liabilities_loan_hire_purchase_liability":
            json_data["liabilities_loan_hire_purchase_liability"]["customer_id"] = customer_id
            json_data["liabilities_loan_hire_purchase_liability"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "liabilities_credit_cards_liability":
            json_data["liabilities_credit_cards_liability"]["customer_id"] = customer_id
            json_data["liabilities_credit_cards_liability"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(data)
        return payload


# def update_policy_json_data(customer_id, context):
#     data = {}
#     if customer_id is not None:
#         json_file_path = "./jsons/create_new_policy.json"
#         with open(json_file_path, "r") as file:
#             json_data = json.load(file)
#         if context == None:
#             json_data['policies_life_assurance_policy']['customer_id'] = customer_id
#             json_data['policies_life_assurance_policy']['case_type'] = 'Life Assurance'
#             json_data['policies_pensions_policy']['customer_id'] = customer_id
#             json_data['policies_pensions_policy']['case_type'] = 'Pensions'
#             json_data['policies_investments_policy']['customer_id'] = customer_id
#             json_data['policies_investments_policy']['case_type'] = 'Investments'
#             json_data['policies_savings_plans_policy']['customer_id'] = customer_id
#             json_data['policies_savings_plans_policy']['case_type'] = 'Savings Plans'
#             json_data['policies_income_protection_policy']['customer_id'] = customer_id
#             json_data['policies_income_protection_policy']['case_type'] = 'Income Protection'
#             json_data['policies_health_assurance_policy']['customer_id'] = customer_id
#             json_data['policies_health_assurance_policy']['case_type'] = 'Health Assurance'
#             json_data['policies_general_policy']['customer_id'] = customer_id
#             json_data['policies_general_policy']['case_type'] = 'General'
#             data = json_data
#         elif context == "policies_life_assurance_policy":
#             json_data["policies_life_assurance_policy"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "policies_pensions_policy":
#             json_data["policies_pensions_policy"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "policies_investments_policy":
#             json_data["policies_investments_policy"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "policies_savings_plans_policy":
#             json_data["policies_savings_plans_policy"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "policies_income_protection_policy":
#             json_data["policies_income_protection_policy"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "policies_health_assurance_policy":
#             json_data["policies_health_assurance_policy"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         elif context == "policies_general_policy":
#             json_data["policies_general_policy"]["customer_id"] = customer_id
#             data.update({context: json_data[context]})
#         else:
#             logger.error("Context Not Implemented")
#
#         payload = json.dumps(data)
#         return payload
#

def update_policy_json_data(provider_correspondence_id,customer_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_new_policy.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            json_data['policies_life_assurance_policy']['customer_id'] = customer_id
            json_data['policies_life_assurance_policy']['case_type'] = 'Life Assurance'
            json_data['policies_pensions_policy']['customer_id'] = customer_id
            json_data['policies_pensions_policy']['case_type'] = 'Pensions'
            json_data['policies_investments_policy']['customer_id'] = customer_id
            json_data['policies_investments_policy']['case_type'] = 'Investments'
            json_data['policies_savings_plans_policy']['customer_id'] = customer_id
            json_data['policies_savings_plans_policy']['case_type'] = 'Savings Plans'
            json_data['policies_income_protection_policy']['customer_id'] = customer_id
            json_data['policies_income_protection_policy']['case_type'] = 'Income Protection'
            json_data['policies_health_assurance_policy']['customer_id'] = customer_id
            json_data['policies_health_assurance_policy']['case_type'] = 'Health Assurance'
            json_data['policies_general_policy']['customer_id'] = customer_id
            json_data['policies_general_policy']['case_type'] = 'General'
            data = json_data
        elif context == "policies_life_assurance_policy":
            json_data["policies_life_assurance_policy"]["customer_id"] = customer_id
            json_data["policies_life_assurance_policy"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_policy":
            json_data["policies_pensions_policy"]["customer_id"] = customer_id
            json_data["policies_pensions_policy"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_policy":
            json_data["policies_investments_policy"]["customer_id"] = customer_id
            json_data["policies_investments_policy"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_policy":
            json_data["policies_savings_plans_policy"]["customer_id"] = customer_id
            json_data["policies_savings_plans_policy"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_policy":
            json_data["policies_income_protection_policy"]["customer_id"] = customer_id
            json_data["policies_income_protection_policy"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_policy":
            json_data["policies_health_assurance_policy"]["customer_id"] = customer_id
            json_data["policies_health_assurance_policy"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        elif context == "policies_general_policy":
            json_data["policies_general_policy"]["customer_id"] = customer_id
            json_data["policies_general_policy"]["provider_correspondence"] = provider_correspondence_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")

        payload = json.dumps(data)
        return payload


def update_json_data(customer_id=None, context=None):
    json_file_path = ''
    if customer_id is not None:
        if context == 'asset':
            json_file_path = "./jsons/create_new_asset.json"
        elif context == 'policy':
            json_file_path = "./jsons/create_new_policy.json"
        elif context == 'income':
            json_file_path = "./jsons/create_new_income.json"
        elif context == 'address_book':
            json_file_path = "./jsons/create_new_addressbook.json"
        elif context == 'liability':
            json_file_path = "./jsons/create_new_liability.json"
        elif context == 'attitude':
            json_file_path = "./jsons/create_new_attituderisk.json"

        with open(json_file_path, "r") as file:
            json_data = json.load(file)

        if context == 'client':
            json_data["name_and_address"]["customer_id"] = customer_id
        elif context == 'income':
            json_data["income"]["customer_id"] = customer_id
        elif context == 'attitude':
            json_data["attitude_to_risk"]["customer_id"] = customer_id
        elif context == 'address_book':
            json_data["address_book"]["customer_id"] = customer_id
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(json_data)
        return payload


def update_business_json_data(customer_id, case_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_new_business.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            pass
            data = json_data
        elif context == "asset_investment_actions":
            json_data["asset_investment_actions"]["customer_id"] = customer_id
            json_data["asset_investment_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_mortgages_actions":
            json_data["liabilities_mortgages_actions"]["customer_id"] = customer_id
            json_data["liabilities_mortgages_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_loan_hire_purchase_actions":
            json_data["liabilities_loan_hire_purchase_actions"]["customer_id"] = customer_id
            json_data["liabilities_loan_hire_purchase_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_loan_hire_purchase_payments_actions":
            json_data["liabilities_loan_hire_purchase_payments_actions"]["customer_id"] = customer_id
            json_data["liabilities_loan_hire_purchase_payments_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_actions":
            json_data["policies_life_assurance_actions"]["customer_id"] = customer_id
            json_data["policies_life_assurance_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_actions":
            json_data["policies_pensions_actions"]["customer_id"] = customer_id
            json_data["policies_pensions_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_actions":
            json_data["policies_investments_actions"]["customer_id"] = customer_id
            json_data["policies_investments_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_actions":
            json_data["policies_savings_plans_actions"]["customer_id"] = customer_id
            json_data["policies_savings_plans_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_actions":
            json_data["policies_income_protection_actions"]["customer_id"] = customer_id
            json_data["policies_income_protection_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_actions":
            json_data["policies_health_assurance_actions"]["customer_id"] = customer_id
            json_data["policies_health_assurance_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_general_actions":
            json_data["policies_general_actions"]["customer_id"] = customer_id
            json_data["policies_general_actions"]["case_id"] = case_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(data)
        return payload


def update_asset_payment_json_data(customer_id, case_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_new_asset_payment.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            pass
            data = json_data
        elif context == "asset_investment_payment":
            json_data["asset_investment_payment"]["customer_id"] = customer_id
            json_data["asset_investment_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_share_holdings_payment":
            json_data["asset_share_holdings_payment"]["customer_id"] = customer_id
            json_data["asset_share_holdings_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_banks_building_societies_payment":
            json_data["asset_banks_building_societies_payment"]["customer_id"] = customer_id
            json_data["asset_banks_building_societies_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_mortgages_payment":
            json_data["liabilities_mortgages_payment"]["customer_id"] = customer_id
            json_data["liabilities_mortgages_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_loan_hire_purchase_payments":
            json_data["liabilities_loan_hire_purchase_payments"]["customer_id"] = customer_id
            json_data["liabilities_loan_hire_purchase_payments"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_credit_cards_payments":
            json_data["liabilities_credit_cards_payments"]["customer_id"] = customer_id
            json_data["liabilities_credit_cards_payments"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_payment":
            json_data["policies_life_assurance_payment"]["customer_id"] = customer_id
            json_data["policies_life_assurance_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_payment":
            json_data["policies_pensions_payment"]["customer_id"] = customer_id
            json_data["policies_pensions_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_payments":
            json_data["policies_investments_payments"]["customer_id"] = customer_id
            json_data["policies_investments_payments"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_payment":
            json_data["policies_savings_plans_payment"]["customer_id"] = customer_id
            json_data["policies_savings_plans_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_payment":
            json_data["policies_income_protection_payment"]["customer_id"] = customer_id
            json_data["policies_income_protection_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_payment":
            json_data["policies_health_assurance_payment"]["customer_id"] = customer_id
            json_data["policies_health_assurance_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_general_payment":
            json_data["policies_general_payment"]["customer_id"] = customer_id
            json_data["policies_general_payment"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_investment_review":
            json_data["asset_investment_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "asset_share_holdings_review":
            json_data["asset_share_holdings_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "asset_home_personal_review":
            json_data["asset_home_personal_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "asset_banks_building_societies_review":
            json_data["asset_banks_building_societies_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "liabilities_mortgages_review":
            json_data["liabilities_mortgages_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "liabilities_loan_hire_purchase_review":
            json_data["liabilities_loan_hire_purchase_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "liabilities_credit_cards_review":
            json_data["liabilities_credit_cards_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_review":
            json_data["policies_life_assurance_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_review":
            json_data["policies_pensions_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_review":
            json_data["policies_investments_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_review":
            json_data["policies_savings_plans_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_review":
            json_data["policies_income_protection_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_review":
            json_data["policies_health_assurance_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "policies_general_review":
            json_data["policies_general_review"]["customer_id"] = customer_id
            data.update({context: json_data[context]})
        elif context == "asset_investment_payment_complaince":
            json_data["asset_investment_payment_complaince"]["customer_id"] = customer_id
            json_data["asset_investment_payment_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_share_holdings_complaince":
            json_data["asset_share_holdings_complaince"]["customer_id"] = customer_id
            json_data["asset_share_holdings_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_banks_building_societies_complaince":
            json_data["asset_banks_building_societies_complaince"]["customer_id"] = customer_id
            json_data["asset_banks_building_societies_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_mortgages_payment_complaince":
            json_data["liabilities_mortgages_payment_complaince"]["customer_id"] = customer_id
            json_data["liabilities_mortgages_payment_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_loan_hire_purchase_payments_complaince":
            json_data["liabilities_loan_hire_purchase_payments_complaince"]["customer_id"] = customer_id
            json_data["liabilities_loan_hire_purchase_payments_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "liabilities_credit_cards_payments_complaince":
            json_data["liabilities_credit_cards_payments_complaince"]["customer_id"] = customer_id
            json_data["liabilities_credit_cards_payments_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_payments_complaince":
            json_data["policies_life_assurance_payments_complaince"]["customer_id"] = customer_id
            json_data["policies_life_assurance_payments_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_payments_complaince":
            json_data["policies_pensions_payments_complaince"]["customer_id"] = customer_id
            json_data["policies_pensions_payments_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_payments_complaince":
            json_data["policies_investments_payments_complaince"]["customer_id"] = customer_id
            json_data["policies_investments_payments_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_payments_complaince":
            json_data["policies_savings_plans_payments_complaince"]["customer_id"] = customer_id
            json_data["policies_savings_plans_payments_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_payments_complaince":
            json_data["policies_income_protection_payments_complaince"]["customer_id"] = customer_id
            json_data["policies_income_protection_payments_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_complaince":
            json_data["policies_health_assurance_complaince"]["customer_id"] = customer_id
            json_data["policies_health_assurance_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_general_payments_complaince":
            json_data["policies_general_payments_complaince"]["customer_id"] = customer_id
            json_data["policies_general_payments_complaince"]["case_id"] = case_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(data)
        return payload


def update_asset_withdrawal_json_data(customer_id, case_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_new_asset_withdrawals.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            pass
            data = json_data
        elif context == "asset_investment_withdrawals":
            json_data["asset_investment_withdrawals"]["customer_id"] = customer_id
            json_data["asset_investment_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_share_holdings_withdrawals":
            json_data["asset_share_holdings_withdrawals"]["customer_id"] = customer_id
            json_data["asset_share_holdings_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_banks_building_societies_withdrawals":
            json_data["asset_banks_building_societies_withdrawals"]["customer_id"] = customer_id
            json_data["asset_banks_building_societies_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_withdrawals":
            json_data["policies_life_assurance_withdrawals"]["customer_id"] = customer_id
            json_data["policies_life_assurance_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_withdrawals":
            json_data["policies_pensions_withdrawals"]["customer_id"] = customer_id
            json_data["policies_pensions_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_withdrawals":
            json_data["policies_investments_withdrawals"]["customer_id"] = customer_id
            json_data["policies_investments_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_withdrawals":
            json_data["policies_savings_plans_withdrawals"]["customer_id"] = customer_id
            json_data["policies_savings_plans_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_withdrawals":
            json_data["policies_income_protection_withdrawals"]["customer_id"] = customer_id
            json_data["policies_income_protection_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_withdrawals":
            json_data["policies_health_assurance_withdrawals"]["customer_id"] = customer_id
            json_data["policies_health_assurance_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_general_withdrawals":
            json_data["policies_general_withdrawals"]["customer_id"] = customer_id
            json_data["policies_general_withdrawals"]["case_id"] = case_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(data)
        return payload


def update_asset_valuation_json_data(customer_id, case_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_new_valuations.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            pass
            data = json_data
        elif context == "asset_investment_valuation":
            json_data["asset_investment_valuation"]["customer_id"] = customer_id
            json_data["asset_investment_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_share_holdings_valuation":
            json_data["asset_share_holdings_valuation"]["customer_id"] = customer_id
            json_data["asset_share_holdings_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_home_personal_valuation":
            json_data["asset_home_personal_valuation"]["customer_id"] = customer_id
            json_data["asset_home_personal_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_banks_building_societies_valuation":
            json_data["asset_banks_building_societies_valuation"]["customer_id"] = customer_id
            json_data["asset_banks_building_societies_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_valuation":
            json_data["policies_life_assurance_valuation"]["customer_id"] = customer_id
            json_data["policies_life_assurance_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_valuation":
            json_data["policies_pensions_valuation"]["customer_id"] = customer_id
            json_data["policies_pensions_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_valuation":
            json_data["policies_investments_valuation"]["customer_id"] = customer_id
            json_data["policies_investments_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_valuation":
            json_data["policies_income_protection_valuation"]["customer_id"] = customer_id
            json_data["policies_income_protection_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_valuation":
            json_data["policies_health_assurance_valuation"]["customer_id"] = customer_id
            json_data["policies_health_assurance_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_general_valuation":
            json_data["policies_general_valuation"]["customer_id"] = customer_id
            json_data["policies_general_valuation"]["case_id"] = case_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(data)
        return payload


def update_fund_json_data(customer_id, case_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_new_funds.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            pass
            data = json_data
        elif context == "asset_investment_fund":
            json_data["asset_investment_fund"]["customer_id"] = customer_id
            json_data["asset_investment_fund"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_funds":
            json_data["policies_life_assurance_funds"]["customer_id"] = customer_id
            json_data["policies_life_assurance_funds"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_funds":
            json_data["policies_pensions_funds"]["customer_id"] = customer_id
            json_data["policies_pensions_funds"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_funds":
            json_data["policies_investments_funds"]["customer_id"] = customer_id
            json_data["policies_investments_funds"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_funds":
            json_data["policies_savings_plans_funds"]["customer_id"] = customer_id
            json_data["policies_savings_plans_funds"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_funds":
            json_data["policies_income_protection_funds"]["customer_id"] = customer_id
            json_data["policies_income_protection_funds"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_funds":
            json_data["policies_health_assurance_funds"]["customer_id"] = customer_id
            json_data["policies_health_assurance_funds"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "policies_general_funds":
            json_data["policies_general_funds"]["customer_id"] = customer_id
            json_data["policies_general_funds"]["case_id"] = case_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(data)
        return payload


def update_asset_commission_json_data(customer_id, case_id, payment_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_new_asset_payment_commission.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            pass
            data = json_data
        elif context == "asset_investment_payment_commission":
            json_data["asset_investment_payment_commission"]["customer_id"] = customer_id
            json_data["asset_investment_payment_commission"]["payment_id"] = payment_id
            json_data["asset_investment_payment_commission"]["case_id"] = case_id
            data.update({context: json_data[context]})
        elif context == "asset_share_holdings_commission":
            json_data["asset_share_holdings_commission"]["customer_id"] = customer_id
            json_data["asset_share_holdings_commission"]["case_id"] = case_id
            json_data["asset_share_holdings_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "asset_banks_building_societies_payment_commission":
            json_data["asset_banks_building_societies_payment_commission"]["customer_id"] = customer_id
            json_data["asset_banks_building_societies_payment_commission"]["case_id"] = case_id
            json_data["asset_banks_building_societies_payment_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "liabilities_mortgages_payment_commission":
            json_data["liabilities_mortgages_payment_commission"]["customer_id"] = customer_id
            json_data["liabilities_mortgages_payment_commission"]["case_id"] = case_id
            json_data["liabilities_mortgages_payment_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "liabilities_loan_hire_purchase_payments_commission":
            json_data["liabilities_loan_hire_purchase_payments_commission"]["customer_id"] = customer_id
            json_data["liabilities_loan_hire_purchase_payments_commission"]["case_id"] = case_id
            json_data["liabilities_loan_hire_purchase_payments_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "liabilities_credit_cards_payments_commission":
            json_data["liabilities_credit_cards_payments_commission"]["customer_id"] = customer_id
            json_data["liabilities_credit_cards_payments_commission"]["case_id"] = case_id
            json_data["liabilities_credit_cards_payments_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_payments_commission":
            json_data["policies_life_assurance_payments_commission"]["customer_id"] = customer_id
            json_data["policies_life_assurance_payments_commission"]["case_id"] = case_id
            json_data["policies_life_assurance_payments_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_payments_commission":
            json_data["policies_pensions_payments_commission"]["customer_id"] = customer_id
            json_data["policies_pensions_payments_commission"]["case_id"] = case_id
            json_data["policies_pensions_payments_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_payments":
            json_data["policies_investments_payments"]["customer_id"] = customer_id
            json_data["policies_investments_payments"]["case_id"] = case_id
            json_data["asset_investment_payment_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_payments_commission":
            json_data["policies_investments_payments_commission"]["customer_id"] = customer_id
            json_data["policies_investments_payments_commission"]["case_id"] = case_id
            json_data["policies_investments_payments_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_payments_commission":
            json_data["policies_savings_plans_payments_commission"]["customer_id"] = customer_id
            json_data["policies_savings_plans_payments_commission"]["case_id"] = case_id
            json_data["policies_savings_plans_payments_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_payments_commission":
            json_data["policies_income_protection_payments_commission"]["customer_id"] = customer_id
            json_data["policies_income_protection_payments_commission"]["case_id"] = case_id
            json_data["policies_income_protection_payments_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        elif context == "policies_general_payments_commission":
            json_data["policies_general_payments_commission"]["customer_id"] = customer_id
            json_data["policies_general_payments_commission"]["case_id"] = case_id
            json_data["policies_general_payments_commission"]["payment_id"] = payment_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(data)
        return payload

def update_partner_json_data(customer_id=None, context=None):
    # json_file_path = ''
    if customer_id is not None:
        json_file_path = "./jsons/create_client_contexts.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        json_data["name_and_address"]["client_value"] = 'partner'
        json_data["name_and_address"]["customer_id"] = customer_id
        logger.info(json_data[context])
        payload = json.dumps(json_data)
        return payload


def update_default_income_category(customer_id, income_id):
    if customer_id is not None:
        json_file_path = "./jsons/create_default_income_category.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        logger.info(json_data)
        json_data["income"]["customer_id"] = customer_id
        logger.info(json_data)
        json_data["income"]["income_categories"][0]["income_category_id"] = income_id
        logger.info(json_data)

        payload = json.dumps(json_data)
        return payload


def update_default_load_standard_case_action(customer_id, case_id, tracking_id, context):
    data = {}
    if customer_id is not None:
        json_file_path = "./jsons/create_default_load_standard_case_action.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        if context == None:
            pass
            data = json_data
        elif context == "asset_investment_actions":
            json_data["asset_investment_actions"]["customer_id"] = customer_id
            json_data["asset_investment_actions"]["case_id"] = case_id
            json_data["asset_investment_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "liabilities_mortgages_actions":
            json_data["liabilities_mortgages_actions"]["customer_id"] = customer_id
            json_data["liabilities_mortgages_actions"]["case_id"] = case_id
            json_data["liabilities_mortgages_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "liabilities_loan_hire_purchase_actions":
            json_data["liabilities_loan_hire_purchase_actions"]["customer_id"] = customer_id
            json_data["liabilities_loan_hire_purchase_actions"]["case_id"] = case_id
            json_data["liabilities_loan_hire_purchase_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "policies_life_assurance_actions":
            json_data["policies_life_assurance_actions"]["customer_id"] = customer_id
            json_data["policies_life_assurance_actions"]["case_id"] = case_id
            json_data["policies_life_assurance_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "policies_pensions_actions":
            json_data["policies_pensions_actions"]["customer_id"] = customer_id
            json_data["policies_pensions_actions"]["case_id"] = case_id
            json_data["policies_pensions_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "policies_investments_actions":
            json_data["policies_investments_actions"]["customer_id"] = customer_id
            json_data["policies_investments_actions"]["case_id"] = case_id
            json_data["policies_investments_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "policies_savings_plans_actions":
            json_data["policies_savings_plans_actions"]["customer_id"] = customer_id
            json_data["policies_savings_plans_actions"]["case_id"] = case_id
            json_data["policies_savings_plans_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "policies_income_protection_actions":
            json_data["policies_income_protection_actions"]["customer_id"] = customer_id
            json_data["policies_income_protection_actions"]["case_id"] = case_id
            json_data["policies_income_protection_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "policies_health_assurance_actions":
            json_data["policies_health_assurance_actions"]["customer_id"] = customer_id
            json_data["policies_health_assurance_actions"]["case_id"] = case_id
            json_data["policies_health_assurance_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        elif context == "policies_general_actions":
            json_data["policies_general_actions"]["customer_id"] = customer_id
            json_data["policies_general_actions"]["case_id"] = case_id
            json_data["policies_general_actions"]["tracking_case_actions"][0]["tracking_id"] = tracking_id
            data.update({context: json_data[context]})
        else:
            logger.error("Context Not Implemented")
        payload = json.dumps(data)
        return payload


def update_default_attituderisk_category(customer_id, category_id, rating_id):
    if customer_id is not None:
        json_file_path = "./jsons/create_default_attitude_risk.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        #logger.info(json_data)
        json_data["attitude_to_risk"]["customer_id"] = customer_id
        #logger.info(json_data)
        json_data["attitude_to_risk"]["attitude_risks"][0]["category_id"] = category_id
        #logger.info(json_data)
        json_data["attitude_to_risk"]["attitude_risks"][0]["rating_id"] = rating_id
        #logger.info(json_data)

        payload = json.dumps(json_data)
        return payload


def update_userdefined_value(customer_id, category_id,context):
    if customer_id is not None:
        json_file_path = "./jsons/create_client_contexts.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        #logger.info(json_data)

        if context == "user_defined_values":
            json_data["user_defined_values"][0]["customer_id"] = customer_id
            json_data["user_defined_values"][0]["user_defined_field_id"] = category_id

            #logger.info(category_id)

        payload = json.dumps(json_data)
        return payload


def update_name_field(json_data,context,field_name):
    fake = faker.Faker()

    json_data[context][field_name] = fake.job()[:25]


def patch_userdefined_value(value_id, category_id,context):
    if value_id is not None:
        json_file_path = "./jsons/create_new_user_defined_value.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        #logger.info(json_data)

        if context == "user_defined_values":
            json_data["user_defined_values"][0]["user_defined_value_id"] = value_id
            json_data["user_defined_values"][0]["user_defined_field_id"] = category_id
            #logger.info(category_id)

        payload = json.dumps(json_data)
        return payload


def update_manage_user(data):
    logger.info(data)
    json_file_path = "./jsons/create_new_manage_user.json"
    with open(json_file_path, "r") as file:
        json_data = json.load(file)

    for key, value in data.items():
        if key == "value":
            if json_data.get("credentials"):
                json_data["credentials"][0]["value"] = value
        elif key in json_data:
            json_data[key] = value
    logger.info(json_data)

    realm = data.get('role')
    logger.info(realm)

    logger.info(realm)


    if realm == 'SuperAdmin':
            new_role = {
                "id": "891af1ca-348c-4524-858e-5d9de0125cea",
                "name": "ifa-admin",
                "description": "Super Admin",
                "composite": True,
                "clientRole": False,
                "containerId": "8ab4bf74-c012-4142-93ae-c67b5e329679"
            }
            json_data["realmRoles"].append(new_role)
    if realm == "Advisor Role":
            new_role = {
                "id": "e4d593c3-7c9e-4be9-894c-0199a6a4faff",
                "name": "advisor",
                "description": "Advisor Role",
                "composite": True,
                "clientRole": False,
                "containerId": "b9a2238b-476b-45b7-97b1-563d6ed5fab8"
            }
            json_data["realmRoles"].append(new_role)
    if realm == "Planner":
            new_role = {
                "id": "d74a9f50-17f4-416c-b5d5-de447a13726e",
                "name": "planner",
                "description": "Planner",
                "composite": True,
                "clientRole": False,
                "containerId": "b9a2238b-476b-45b7-97b1-563d6ed5fab8"
            }
            json_data["realmRoles"].append(new_role)
    if realm == "Manager Role":
            new_role = {
                "id": "eac50e92-1168-43af-ae74-96496aa1fa33",
                "name": "manager",
                "description": "Manager Role",
                "composite": True,
                "clientRole": False,
                "containerId": "b9a2238b-476b-45b7-97b1-563d6ed5fab8"
            }
            json_data["realmRoles"].append(new_role)
    if realm == "View Only User":
            new_role = {
                "id": "d7da7d5d-3daa-45f7-a357-bd6b78412ff8",
                "name": "viewer",
                "description": "View Only User",
                "composite": True,
                "clientRole": False,
                "containerId": "b9a2238b-476b-45b7-97b1-563d6ed5fab8"
            }
            json_data["realmRoles"].append(new_role)



    payload = json.dumps(json_data)
    return payload

def update_vulnerability(customer_id,data,context):
    logger.info(data)

    json_file_path = "./jsons/create_new_vulnerability.json"
    with open(json_file_path, "r") as file:
        json_data = json.load(file)

    drive = data.get('driver')
    character = data.get('characteristics')


    if drive == "Health" and character == "Physical disability":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "cd2191bf-b54d-45b4-bc9a-132d9709769d"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "78379c0d-229c-451d-b31d-d8dfdde92fc3"

        data.update({context: json_data[context]})
    elif drive == "Health" and character == "Severe or long-term illness":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "cd2191bf-b54d-45b4-bc9a-132d9709769d"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "56631eb9-6e95-45a8-92a6-8a91ababc7f3"
        data.update({context: json_data[context]})
    elif drive == "Health" and character == "Hearing or visual impairment":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "cd2191bf-b54d-45b4-bc9a-132d9709769d"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "71839620-050c-471a-9cec-d91eec1134fd"
        data.update({context: json_data[context]})
    elif drive == "Health" and character == "Addition":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "cd2191bf-b54d-45b4-bc9a-132d9709769d"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "7d19e721-637c-45b0-b6a9-d0e3395a6567"
        data.update({context: json_data[context]})
    elif drive == "Health" and character == "Low mental capacity or cognitive disability":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "cd2191bf-b54d-45b4-bc9a-132d9709769d"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "38d5b8de-30ec-4d4f-b9c4-347a6396666b"
        data.update({context: json_data[context]})
    elif drive == "Health" and character == "Other":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "cd2191bf-b54d-45b4-bc9a-132d9709769d"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "c94aaa55-01f8-40ac-9bbe-fea66b7b4a70"
        data.update({context: json_data[context]})
    elif drive == "Life Events" and character == "Bereavement":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "b460e206-fdc2-4464-bb22-b8278c92a4aa"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "7fb148fa-6d1c-40df-8103-7180510d84a8"
        data.update({context: json_data[context]})
    elif drive == "Life Events" and character == "Income shock":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "b460e206-fdc2-4464-bb22-b8278c92a4aa"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "80c7f471-453e-4db6-ac27-709071a7c0de"
        data.update({context: json_data[context]})
    elif drive == "Life Events" and character == "Relationship breakdown":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "b460e206-fdc2-4464-bb22-b8278c92a4aa"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "7d02bc22-f4cd-4947-a010-2a4659f9ae38"
        data.update({context: json_data[context]})
    elif drive == "Life Events" and character == "Domestic abuse(including ecnomic control)":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "b460e206-fdc2-4464-bb22-b8278c92a4aa"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "42b2e5e9-6bd5-455a-aeb8-0f2c5cdbe924"
        data.update({context: json_data[context]})
    elif drive == "Life Events" and character == "Caring responsibilities":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "b460e206-fdc2-4464-bb22-b8278c92a4aa"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "8acb0654-482f-4a22-9142-0e4bc1df59db"
        data.update({context: json_data[context]})
    elif drive == "Life Events" and character == "Other":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "b460e206-fdc2-4464-bb22-b8278c92a4aa"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "8620c457-9947-438f-860f-7414bbedcc07"
        data.update({context: json_data[context]})
    elif drive == "Resilience" and character == "Inadequate(outgong exceed income) or erratic income":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "ce026716-5b56-494e-b3ef-191f9d59e73b"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "bdc29d01-c21b-46a7-bce2-dd51e13f44a2"
        data.update({context: json_data[context]})
    elif drive == "Resilience" and character == "Over-indebtedness":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "ce026716-5b56-494e-b3ef-191f9d59e73b"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "8f32184a-0bdc-4fde-8a2f-d3e7c554736a"
        data.update({context: json_data[context]})
    elif drive == "Resilience" and character == "Low savings":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "ce026716-5b56-494e-b3ef-191f9d59e73b"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "7545dbb1-2b96-4d98-ac9f-b90aba796520"
        data.update({context: json_data[context]})
    elif drive == "Resilience" and character == "Low emotional resilience":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "ce026716-5b56-494e-b3ef-191f9d59e73b"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "0c02daa9-7afa-4288-893f-e8f90705a4ea"
        data.update({context: json_data[context]})
    elif drive == "Resilience" and character == "Other":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "ce026716-5b56-494e-b3ef-191f9d59e73b"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "36717935-c6be-4d85-bc41-fbfe9c40daf5"
        data.update({context: json_data[context]})
    elif drive == "Capability" and character == "Low knowledge or confidence in managing finanace":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "aebc587e-5006-4aea-b9c9-229d7a594fb0"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "b663f13d-ba2a-4049-97f1-4b3738f18828"
        data.update({context: json_data[context]})
    elif drive == "Capability" and character == "Poor literacy or numeracy skill":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "aebc587e-5006-4aea-b9c9-229d7a594fb0"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "adf37b1e-b102-4c25-a298-447ec46c31cf"
        data.update({context: json_data[context]})
    elif drive == "Capability" and character == "Poor English language skills":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "aebc587e-5006-4aea-b9c9-229d7a594fb0"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "a587584d-5f1a-437d-a5ea-5b776f55a554"
        data.update({context: json_data[context]})
    elif drive == "Capability" and character == "Poor or non-existent digital skill":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "aebc587e-5006-4aea-b9c9-229d7a594fb0"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "907817a0-30ce-4218-8253-29f8b4861197"
        data.update({context: json_data[context]})
    elif drive == "Capability" and character == "Learning difficulties":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "aebc587e-5006-4aea-b9c9-229d7a594fb0"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "12287fec-ef5c-496c-b259-21e2f9facd73"
        data.update({context: json_data[context]})
    elif drive == "Capability" and character == "No or low access to help or support":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "aebc587e-5006-4aea-b9c9-229d7a594fb0"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "16aeb8bd-2316-4121-a54b-066f8b519ce0"
        data.update({context: json_data[context]})
    elif drive == "Capability" and character == "Other":
        json_data["vulnerability"]["customer_id"] = customer_id
        json_data["vulnerability"]["vulnerabilitydriver_id"] = "aebc587e-5006-4aea-b9c9-229d7a594fb0"
        json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "23da6e30-e5ca-4204-9f3a-caed129980f9"
        json_data["vulnerability"]["ratings"] = data.get('ratings')
        data.update({context: json_data[context]})
    else:
        logger.error("Invalid input")
    payload = json.dumps(json_data)
    return payload

def update_vulnerability_post(customer_id):
    json_file_path = "./jsons/create_new_vulnerability.json"
    with open(json_file_path, "r") as file:
        json_data = json.load(file)
    # logger.info(json_data)
    json_data["vulnerability"]["customer_id"] = customer_id

    json_data["vulnerability"]["vulnerabilitydriver_id"] = "cd2191bf-b54d-45b4-bc9a-132d9709769d"
    json_data["vulnerability"]["vulnerabilitycharacteristic_id"] = "78379c0d-229c-451d-b31d-d8dfdde92fc3"

    # logger.info(json_data)

    payload = json.dumps(json_data)
    return payload
def update_manage_user_read_json(customer_id,datas):
        datas = "./jsons/create_new_manage_user_1.json"
        with open(datas, "r") as file:
            json_data = json.load(file)

        json_data["username"] = customer_id+"@tekknology.com"
        json_data["email"] = customer_id+"@tekknology.com"
        payload = json.dumps(json_data)
        logger.info(payload)
        return payload


def update_manage_user_business_read_json(customer_id, datas):
    datas = "./jsons/create_new_manage_user_for_patch.json"
    with open(datas, "r") as file:
        json_data = json.load(file)
    json_data["username"] = customer_id+"@tekknology.com"
    json_data["email"] = customer_id+"@tekknology.com"
    payload = json.dumps(json_data)
    logger.info(payload)
    return payload

def update_default_objective_category(customer_id, objective_id):
    if customer_id is not None:
        json_file_path = "./jsons/create_default_objective_category.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        #logger.info(json_data)
        json_data["Objective"]["customer_id"] = customer_id
        #logger.info(json_data)
        json_data["Objective"]["objectives"][0]["detail_id"] = objective_id
        #logger.info(json_data)

        payload = json.dumps(json_data)
        return payload


def compare_dicts(dict1, dict2):
    for key, value1 in dict1.items():
        if isinstance(value1, int):
            value1 = round(value1, 4)
        if key in dict2:
            value2 = dict2[key]
            if isinstance(value2, int):
                value2 = round(value2, 4)
            if isinstance(value1, dict) and isinstance(value2, dict):
                compare_dicts(value1, value2)
            elif value1 != value2:
                if key =='customer_id':
                    pass
                elif (value1 == 0 and float(value2) == 0.0000) or key in extra_fields:
                    pass
                else:
                    logger.warning(f"Values for '{key}' do not match. Expected: {value1}, Actual: {value2}")
                    assert False
                # assert False
    # for key in dict2.keys():
    #     if key not in dict1:
    #         logger.warning(f"'{key}' not found in the expected values.")
    #         fields.append(key)
    #         if fields:
    #             return fields



# def check_reponse_message(response, expected_message):
#     validation_error_codes = [10006, '11004']
#     if 'error' in response:
#         if response['error']['code'] in validation_error_codes:
#             assert response["isError"] is True, "API call failed ['isError'] should be True"
#             if response['error']["message"][0] != expected_message:
#                 assert False, f"API call failed with message: {response['error']['message']}"
#         elif response['error']['message'] != '':
#             if response['error']['message']:
#                 assert response['error']['message'] == expected_message, f"API call failed with message: {response['error']['message']}"
#             elif response['message']:
#                 assert response['message'] == expected_message, f"API call failed with message: {response['message']}"
#     else:
#         assert response['statusCode'] == 200, f"API call failed with StatusCode: {response['statusCode']}"
#         assert response["isError"] is False, "API call failed ['isError'] should be False"
#         assert response["message"] == expected_message, \
#             f"API call failed with message: {response['message']}"

#
# def check_reponse_message(response, expected_message):
#     logger.info(expected_message)
#     # logger.info(response["messages"])
#     validation_error_codes = [10006,'11004', '30003', '40006','40007','30004', '10009','60019']
#     # if 'error' in response and response['error']['code'] != '':
#     if 'error' in response:
#         logger.info(response['error']['code'])
#         if response['error']['code'] in validation_error_codes:
#             assert response["isError"] is True, "API call failed ['isError'] should be True"
#             if response['error']["message"][0] != expected_message:
#                 assert False, f"API call failed with message: {response['error']['message']}"
#         elif response['error']['message'] != '':
#             if response['error']['message']:
#                 assert response['error']['message'] == expected_message, f"API call failed with message: {response['error']['message']}"
#             elif response['message']:
#                 assert response['message'] == expected_message, f"API call failed with message: {response['message']}"
#     else:
#         logger.info("##############")
#         assert response['statusCode'] == 200, f"API call failed with StatusCode: {response['statusCode']}"
#         assert response["isError"] is False, "API call failed ['isError'] should be False"
#         try:
#             assert response["message"] == expected_message, \
#                 f"API call failed with message: {response['message']}"
#         except:
#             assert response["messages"] == expected_message, \
#                 f"API call failed with message: {response['message']}"
#

# def convert_data_types(json_payload, expected_data_types, context):
#     for field, expected_type_str in expected_data_types[context].items():
#         if field in json_payload[context]:
#             current_value = json_payload[context][field]
#             expected_type = type(expected_type_str)
#             if expected_type == int and isinstance(current_value, str):
#                 # If the expected type is int and the current value is a string, keep it as string
#                 json_payload[context][field] = current_value
#             elif expected_type == int and (isinstance(current_value, float) or isinstance(current_value, str)):
#                 # If the expected type is int and the current value is a float or a string,
#                 # update the value to float and then to int
#                 try:
#                     json_payload[context][field] = int(float(current_value))
#                 except ValueError:
#                     logger.warning(f"Error converting '{field}' to {expected_type.__name__}. Using default value instead.")
#                     json_payload[context][field] = 0  # or any other default value for integers
#             elif not isinstance(current_value, expected_type):
#                 try:
#                     json_payload[context][field] = expected_type(current_value)
#                 except ValueError:
#                     logger.warning(f"Error converting '{field}' to {expected_type.__name__}. Using default value instead.")
#     return json_payload
#
def update_default_expense_category(customer_id, expense_id):
    if customer_id is not None:
        json_file_path = "./jsons/create_default_expense_category.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        logger.info(json_data)
        json_data["outgoings"]["customer_id"] = customer_id
        logger.info(json_data)
        json_data["outgoings"]["expense_categories"][0]["expense_category_id"] = expense_id
        logger.info(json_data)

        payload = json.dumps(json_data)
        return payload

def update_default_clientaction_category(customer_id, tracking_id):
    if customer_id is not None:
        json_file_path = "./jsons/create_default_clientaction_category.json"
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        logger.info(json_data)
        json_data["contacts_client_action"]["customer_id"] = customer_id
        logger.info(json_data)
        json_data["contacts_client_action"]["tracking_client_actions"][0]["tracking_id"] = tracking_id
        logger.info(json_data)

        payload = json.dumps(json_data)
        return payload


# def check_reponse_message(response, expected_message):
#     validation_error_codes = [10006,1006, '11004', '30003', '40006', '30004', '10009', '40007','60019',2090,2043, 2049,4037,2107,2088,1041, 2002,1000,3009,3004,2033,4005,2020,2048,2049,2004,3010,2069]
#     if 'error' in response and  response['error']['code'] != '':
#         if response['error']['code'] in validation_error_codes:
#             assert response["isError"] is True, "API call failed ['isError'] should be True"
#             if response['error']["message"][0] != expected_message:
#                 assert False, f"API call failed with message: {response['error']['message']}"
#         elif response['error']['message'] != '':
#             if response['error']['message']:
#                 assert response['error']['message'] == expected_message, f"API call failed with message: {response['error']['message']}"
#             elif response['message']:
#                 assert response['message'] == expected_message, f"API call failed with message: {response['message']}"
#     else:
#         assert response['statusCode'] == 200, f"API call failed with StatusCode: {response['statusCode']}"
#         assert response["isError"] is False, "API call failed ['isError'] should be False"
#         assert response["data"][0]["message"] == expected_message, \
#                 f"API call failed with message: {response['message']}"
#         if "message" in response :
#                assert response["message"] == expected_message, \
#                  f"API call failed with message: {response['message']}"
#
#         elif "messages" in response:
#             assert response["messages"] == expected_message, \
#                 f"API call failed with message: {response['messages']}"
#         elif "message" == '' in response :
#                assert response["message"] == expected_message, \
#                  f"API call failed with message: {response['message']}"

def check_reponse_message(response, expected_message):
    validation_error_codes = [2018,10006,1006,'1001', '11004', '30003', '40006', '30004', '10009', '40007','60019',7000,2090,2043, 2049,4037,2107,2088,1041, 2002,1000,3009,3004,2033,4005,2020,2048,2049,2004,3010,2069]
    if 'error' in response and  response['error']['code'] != '':
        if response['error']['code'] in validation_error_codes:
            assert response["isError"] is True, "API call failed ['isError'] should be True"
            if response['error']["message"][0] != expected_message:
                assert False, f"API call failed with message: {response['error']['message']}"
        elif response['error']['message'] != '':
            if response['error']['message']:
                assert response['error']['message'] == expected_message, f"API call failed with message: {response['error']['message']}"
            elif response['message']:
                assert response['message'] == expected_message, f"API call failed with message: {response['message']}"
    else:
        assert response['statusCode'] == 200, f"API call failed with StatusCode: {response['statusCode']}"
        assert response["isError"] is False, "API call failed ['isError'] should be False"

        try:
               assert response["message"] == expected_message, \
                 f"API call failed with message: {response['message']}"

        except:
            assert response["messages"] == expected_message, \
                f"API call failed with message: {response['messages']}"



def convert_data_types(json_payload, expected_data_types, context):
    for field, expected_type_str in expected_data_types[context].items():
        if field in json_payload[context]:
            current_value = json_payload[context][field]
            expected_type = type(expected_type_str)
            if expected_type == int and (isinstance(current_value, float) or isinstance(current_value, str)):
                json_payload[context][field] = float(current_value)
            elif not\
                    isinstance(current_value, expected_type):
                try:
                    json_payload[context][field] = expected_type(current_value)
                except ValueError:
                    logger.warning(f"Error converting '{field}' to {expected_type.__name__}")
    return json_payload

# def convert_data_types(json_payload, expected_data_types, context):
#     for field, expected_type_str in expected_data_types[context].items():
#         current_value = json_payload[context][field]
#         expected_type = type(expected_type_str)
#         if expected_type == int and (isinstance(current_value, float) or isinstance(current_value, str)):
#             json_payload[context][field] = float(current_value)
#         elif not isinstance(current_value, expected_type):
#             try:
#                 json_payload[context][field] = expected_type(current_value)
#             except ValueError:
#                 logger.warning(f"Error converting '{field}' to {expected_type.__name__}")
#     return json_payload

def read_config(section, tag, file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    if section not in config:
        raise ValueError(f"Section '{section}' not found in the config file.")

    config_values = dict(config[section])
    value = config_values.get(tag)
    return value


def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def read_json(json_file_path):
    with open(json_file_path, "r") as file:
        json_data = json.load(file)
    return json_data

