import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
def test_delete_all_data_to_employmentpost(data,create_client,post_client_data,delete_client_details,get_client_data_with_customer_id):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    employment_data = common.read_json("./jsons/create_client_employment.json")
    client_employment = post_client_data(customer_id, employment_data, 'employment', True)
    client_employment_data = client_employment.json()
    logger.info(client_employment_data)
    common.check_reponse_message(client_employment_data, constants.add_client_success_message)
    logger.info("Client employment Added Successfully")
    employment_id = client_employment_data['data']['employment']['employment_id']

    get_client_data_before = get_client_data_with_customer_id(customer_id)
    get_client_response_before = get_client_data_before.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully Before Deletion")

    delete_client_data = delete_client_details('employment',employment_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_employment_success_message)
    logger.info("Employment Details Deleted Successfully")

    get_client_data_after = get_client_data_with_customer_id(customer_id)
    get_client_response_after = get_client_data_after.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully After Deletion")

    employment_before = get_client_response_before['data'].get('employment', [])
    employment_after = get_client_response_after['data'].get('employment', [])

    assert employment_id in [emp['employment_id'] for emp in
                             employment_before], "Employment ID should be in the initial response"
    assert employment_id not in [emp['employment_id'] for emp in
                                 employment_after], "Employment ID should be deleted from the response"

    logger.info("Confirmed that employment data has been deleted successfully.")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_all_data_to_attituderisk(data, create_client, post_client_data, delete_client_details,
                                         get_attituderisk_data):
    #  Create the client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    #  Add attitude to risk details
    attitudet_data = common.read_json("./jsons/create_new_attituderisk.json")
    client_att = post_client_data(customer_id, attitudet_data, 'attitude_to_risk', True)
    client_att_data = client_att.json()
    logger.info(client_att_data)
    common.check_reponse_message(client_att_data, constants.add_client_success_message)
    logger.info("Client Attitude to Risk Added Successfully")
    attituderisk_id = client_att_data['attitude_to_risk']['attituderisk_id']

    #  Fetch client data before deletion
    get_attituderisk_details = get_attituderisk_data(customer_id)
    get_client_response_before = get_attituderisk_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_attitude_to_risk_success_message)
    logger.info("Attitude Risk Details Fetched Successfully")

    #  Delete attitude to risk details
    delete_client_data = delete_client_details('attitude_to_risk', attituderisk_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_attitudeRisk_success_message)
    logger.info("Attitude Risk Details Deleted Successfully")

    #  Fetch client data after deletion
    get_attituderisk_details = get_attituderisk_data(customer_id)
    get_client_response_after = get_attituderisk_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_attitude_to_risk_after_delete_message)
    logger.info("Attitude Risk Details Fetched Successfully")

    # Compare before and after responses to confirm deletion
    attitude_risk_before = get_client_response_before['data']
    attitude_risk_after = get_client_response_after['data']

    # Ensure attituderisk_id is present before deletion
    assert attituderisk_id in [item['attituderisk_id'] for item in
                               attitude_risk_before], "Attitude Risk ID should be in the initial response"

    # Ensure attituderisk_id is not present after deletion
    assert attituderisk_id not in [item['attituderisk_id'] for item in
                                   attitude_risk_after], "Attitude Risk ID should be deleted from the response"

    logger.info("Confirmed that attitude to risk data has been deleted successfully.")


@pytest.mark.parametrize("data",["./jsons/create_client.json"])
def test_delete_all_data_to_identity(data, create_client, post_client_data, delete_client_details, get_client_data_with_customer_id):

    #  Create the client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    #  Add identity details
    identity_data = common.read_json("./jsons/create_new_identity.json")
    client_identity = post_client_data(customer_id, identity_data, 'identity', True)
    client_identity_data = client_identity.json()
    logger.info(client_identity_data)
    common.check_reponse_message(client_identity_data, constants.add_identity_success_message)
    logger.info("Client Details For identity Added Successfully")
    identity_id = client_identity_data['data']['identity']['identity_id']

    #  Fetch client data before deletion
    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response_before = get_client_data.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully Before Deletion")

    #  Delete identity details
    delete_client_data = delete_client_details('identity', identity_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_identity_success_message)
    logger.info("Identity Details Deleted Successfully")

    #  Fetch client data after deletion
    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response_after = get_client_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully After Deletion")

    # Compare before and after responses to confirm deletion
    identity_before = get_client_response_before['data'].get('identity', [])
    identity_after = get_client_response_after['data'].get('identity', [])

    assert identity_id in [identity['identity_id'] for identity in identity_before], "Identity ID should be in the initial response"
    assert identity_id not in [identity['identity_id'] for identity in identity_after], "Identity ID should be deleted from the response"

    logger.info("Confirmed that identity data has been deleted successfully.")



@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_all_data_to_objective(data, create_client, post_client_data, delete_client_details,
                                      get_client_data_with_customer_id):
    #  Create the client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    #  Add objectives data
    objectives_data = common.read_json("./jsons/create_new_objectives.json")
    client_objectives = post_client_data(customer_id, objectives_data, 'objectives', True)
    client_objectives_data = client_objectives.json()
    logger.info(client_objectives_data)
    common.check_reponse_message(client_objectives_data, constants.add_objective_success_message)
    logger.info("Client Objectives Added Successfully")
    objective_id = client_objectives_data['data']['objectives']['objective_id']

    #  Fetch client data before deletion
    get_client_data_before = get_client_data_with_customer_id(customer_id)
    get_client_response_before = get_client_data_before.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully Before Deletion")

    #  Delete objective data
    delete_client_data = delete_client_details('objectives', objective_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_objective_success_message)
    logger.info("Objective Details Deleted Successfully")

    #  Fetch client data after deletion
    get_client_data_after = get_client_data_with_customer_id(customer_id)
    get_client_response_after = get_client_data_after.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully After Deletion")

    #Compare before and after responses to confirm deletion
    objectives_before = get_client_response_before['data'].get('objectives', [])
    objectives_after = get_client_response_after['data'].get('objectives', [])

    # Confirm objective ID exists before deletion and does not exist after deletion
    assert objective_id in [obj['objective_id'] for obj in
                            objectives_before], "Objective ID should be in the initial response"
    assert objective_id not in [obj['objective_id'] for obj in
                                objectives_after], "Objective ID should be deleted from the response"

    logger.info("Confirmed that objective data has been deleted successfully.")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_all_data_to_servicetype(data, create_client, post_client_data, delete_client_details, get_client_data_with_customer_id):

    #  Create the client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Add service type details
    servicetype_data = common.read_json("./jsons/create_new_servicetype.json")
    client_servicetype = post_client_data(customer_id, servicetype_data, 'service_type', True)
    client_servicetype_data = client_servicetype.json()
    logger.info(client_servicetype_data)
    common.check_reponse_message(client_servicetype_data, constants.add_servicetype_success_message)
    logger.info("Client Details For Service Type Added Successfully")
    servicetype_id = client_servicetype_data['data']['servicetype']['servicetype_id']

    # Fetch client data before deletion
    get_client_data_before = get_client_data_with_customer_id(customer_id)
    get_client_response_before = get_client_data_before.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully Before Deletion")

    # Delete service type details
    delete_client_data = delete_client_details('servicetype', servicetype_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_servicetype_success_message)
    logger.info("Service Type Details Deleted Successfully")

    # Step 5: Fetch client data after deletion
    get_client_data_after = get_client_data_with_customer_id(customer_id)
    get_client_response_after = get_client_data_after.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully After Deletion")

   #Compare before and after responses to confirm deletion
    servicetype_before = get_client_response_before['data'].get('servicetype', [])
    servicetype_after = get_client_response_after['data'].get('servicetype', [])

    assert servicetype_id in [stype['servicetype_id'] for stype in servicetype_before], "Service Type ID should be in the initial response"
    assert servicetype_id not in [stype['servicetype_id'] for stype in servicetype_after], "Service Type ID should be deleted from the response"

    logger.info("Confirmed that service type data has been deleted successfully.")
