import pytest
import pytest_html
import requests
import json
import logging
from faker import Faker
from datetime import datetime

from test_assyst.utils import common


logger = logging.getLogger('my_logger')


def get_bearer_token():
    '''
    Function to generate accsess token
    '''

    authentication_url = "https://auth-dev.assyst.cloud/realms/a18e71b5-0191-4a84-a6a6-0ac86f22858f/protocol/openid-connect/token"#'https://auth-dev.assyst.cloud/realms/489c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token' ## # https://auth-dev.assyst.cloud/realms/489c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token'##'https://auth-dev.assyst.cloud/realms/75937879-3944-4672-a904-f911ada300c0/protocol/openid-connect/token'#'https://auth-dev.assyst.cloud/realms/489c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token'################'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'## ####'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token' #####'https://auth.assyst.cloud/realms/799c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token'#####'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token' #'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'##'https://auth-dev.assyst.cloud/realms/tenant4-realm/protocol/openid-connect/token'#'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username = 'rejani@gnx.com'#'reg_test@myvedtekk.com' # # 'ifa-adm'apiauto@gmail.com'#in@myvedtekk.com'######'admin@vedikatekk.com'#####'testgnx@myvedtekk.com'######'amartvm@tekknology.com'######'api@tekknology.com'### ## #'ifa-admin@vedikatekk.com'#'ifa-admin@vedmytekk.com'##api@tekknology.com' # # #'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'rejani@123'  # 'initialpasswordQA'######'Tekk@2024'###'tekk123'##### #'tekk123'######'a344f28ea0c3'#####'initialpassword123'## #'a344f28ea0c3' #'tekk123'#'tekk123'  #'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    # organisation = 'mytekk'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    # client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'
    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        # 'client_secret': client_secret,
        'grant_type': grant_type,
        # 'organisation': organisation
    }

    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)

def get_bearer_token_profile():
    '''
    Function to generate accsess token
    '''

    authentication_url = 'https://auth-dev.assyst.cloud/realms/eb0d4501-ef6a-42ed-a142-89cc1d6294dc/protocol/openid-connect/token'  # 'https://auth-dev.assyst.cloud/realms/489c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token'##'https://auth-dev.assyst.cloud/realms/75937879-3944-4672-a904-f911ada300c0/protocol/openid-connect/token'#'https://auth-dev.assyst.cloud/realms/489c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token'################'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'## ####'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token' #####'https://auth.assyst.cloud/realms/799c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token'#####'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token' #'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'##'https://auth-dev.assyst.cloud/realms/tenant4-realm/protocol/openid-connect/token'#'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username = 'api@gmail.com'  # 'ifa-admin@myvedtekk.com'######'admin@vedikatekk.com'#####'testgnx@myvedtekk.com'######'amartvm@tekknology.com'######'api@tekknology.com'### ## #'ifa-admin@vedikatekk.com'#'ifa-admin@vedmytekk.com'##api@tekknology.com' # # #'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'tekk123'  # 'initialpasswordQA'######'Tekk@2024'###'tekk123'##### #'tekk123'######'a344f28ea0c3'#####'initialpassword123'## #'a344f28ea0c3' #'tekk123'#'tekk123'  #'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    organisation = 'genericqa'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    # client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'

    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        # 'client_secret': client_secret,
        'grant_type': grant_type,
        'organisation': organisation

    }

    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)
def get_bearer_token_action():
    '''
    Function to generate accsess token
    '''
    authentication_url = 'https://auth-dev.assyst.cloud/realms/489c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token'#'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username = 'leena01@myvedtekk.com' # #'amartvm@tekknology.com' #'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'tekk123' #'tekk123'#'tekk123'  #'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    #organisation = 'abc'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'


    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
        #'organisation': organisation


    }
    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)



def get_bearer_token_superadmin():
    #All Clients, Allow View Client, Allow Add Client, Update Client
    '''
    Function to generate accsess token
    '''
    authentication_url = 'https://auth-dev.assyst.cloud/realms/489c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token' #'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username ='apisuperadmintest@myvedtekk.com' #'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'tekk123'  #'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    #organisation = 'abc'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'


    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
        #'organisation': organisation


    }
    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)

def get_bearer_token_viewall():
    #Allow View Client, Allow Add Client
    '''
    Function to generate accsess token
    '''
    authentication_url ="'https://auth-dev.assyst.cloud/realms/489c0fe3-0b1f-449a-a690-c83970f77313/protocol/openid-connect/token'"
    username ='apiviewallusertest@myvedtekk.com'
    password = 'tekk123'  #'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    #organisation = 'abc'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'


    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
        #'organisation': organisation


    }
    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)



def get_bearer_token_user_2():
    #All Clients, Allow View Client, Update Client
    '''
    Function to generate accsess token
    '''
    authentication_url = 'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'  # 'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username = 'apiautomation2@tekknology.com'  # 'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'tekk123'  # 'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    # organisation = 'abc'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'

    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
        # 'organisation': organisation

    }
    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)

def get_bearer_token_user_3():
     # All clients
    '''
    Function to generate accsess token
    '''
    authentication_url = 'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'  # 'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username = 'apiautomation3@tekknology.com'  # 'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'tekk123'  # 'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    # organisation = 'abc'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'

    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
        # 'organisation': organisation

    }
    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)

def get_bearer_token_user_4():
    '''
    Function to generate accsess token
    '''
    authentication_url = 'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'  # 'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username = 'apiautomation4@tekknology.com'  # 'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'tekk123'  # 'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    # organisation = 'abc'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'

    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
        # 'organisation': organisation

    }
    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)

def get_bearer_token_user_5():
    '''
    Function to generate accsess token
    '''
    authentication_url = 'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'  # 'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username = 'apiautomation5@tekknology.com'  # 'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'tekk123'  # 'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    # organisation = 'abc'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'

    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
        # 'organisation': organisation

    }
    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)


def get_bearer_token_user_6():
    '''
    Function to generate accsess token
    '''
    authentication_url = 'https://auth-dev.assyst.cloud/realms/tenant2-realm/protocol/openid-connect/token'  # 'https://keycloak-dev.assyst.cloud/realms/tenant1-realm/protocol/openid-connect/token'
    username = 'apiautomation6@tekknology.com'  # 'test_automation@gmail.com'  #   #'ifa.manager'
    password = 'tekk123'  # 'tekk#2024''gnxtekk#2023'
    client_id = 'client'
    # organisation = 'abc'
    # client_secret = 'prPFVH4mAT5Jm2JSbSzE43ilMAat7jel'
    client_secret = 'bhryDV6Fn4tpyelMiQR4YDnuX96Bs12R'
    grant_type = 'password'

    # Payload for authentication request (adjust based on API requirements)
    payload = {
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
        # 'organisation': organisation

    }
    response = requests.post(authentication_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        bearer_token = token_data.get('access_token')
        return bearer_token
    else:
        print(f"Authentication failed with status code {response.status_code}")
        print(response.text)


@pytest.fixture
def define_env(request):
    '''
    Function to define the environment
    '''
    env_value = request.config.getoption("--env")
    if env_value == "dev":
        return "https://dev-api.assyst.cloud/secured"

    elif env_value == "qa":
        return "https://qa-api.assyst.cloud/secured"

    elif env_value == "prod":
        return "https://api.assyst.cloud/secured"
    else:
        raise ValueError(f"Unsupported environment: {env_value}")


# @pytest.fixture
# def define_test(pytestconfig):
#
#     value = pytestconfig.getoption("--test")
#     if value == "regression":
#         with open('./test_data/AddressBook/test_data_addressbook.csv', mode='r') as file:
#             reader = csv.reader(file)
#             first_two_lines = [next(reader) for _ in range(2)]
#             logger.info(first_two_lines)
#         return first_two_lines
#     else:
#         raise ValueError(f"Unsupported : {value}")



@pytest.fixture
def create_client(define_env):
    '''
    Function to send post request to create a client
    '''
    def _use_fixture_with_parameter(data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing' : "api-automation"
        }
        endpoint = define_env

        if file == True:
            json_file = open(data)
            payload = json.load(json_file)
            logger.info(payload)
        elif file == 'e2e':
            data = data[context]
            payload = {}
            payload.update(({context: data}))
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        fake = Faker()
        payload['name_and_address']['last_name'] = fake.last_name()
        payload['name_and_address']['first_names'] = fake.first_name()
        logger.info(payload)
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def create_client_superadmin(define_env):
    '''
    Function to send post request to create a client
    '''
    def _use_fixture_with_parameter(data, context, file):
        bearer_token = get_bearer_token_superadmin()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing' : "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-middleware.assyst.cloud"
        if file == True:
            json_file = open(data)
            payload = json.load(json_file)
            logger.info(payload)
        elif file == 'e2e':
            data = data[context]
            payload = {}
            payload.update(({context: data}))
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        fake = Faker()
        payload['name_and_address']['last_name'] = fake.last_name()
        payload['name_and_address']['first_names'] = fake.first_name()
        logger.info(payload)
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter




# @pytest.fixture
# def post_client_data(define_env):
#     '''
#     Function to send post request to create different contexts for a client
#     '''
#     def _use_fixture_with_parameter(customer_id, data, context, file):
#         bearer_token = get_bearer_token()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#         }
#
#         endpoint = define_env
#         if file != 'e2e' or not isinstance(data, dict):
#             data.update({'customer_id': customer_id})
#         if file == True and not isinstance(data, dict):
#             json_file = open(data)
#             payload = json.load(json_file)
#         elif (file == 'e2e' or isinstance(data, dict)) and context in data:
#             data = data[context]
#             data["customer_id"] = customer_id
#             json_payload = {}
#             json_payload.update(({context: data}))
#             payload = json.dumps(json_payload)
#             payload = json.loads(payload)
#         else:
#             json_payload = {}
#             json_payload.update(({context: data}))
#             payload = json.dumps(json_payload)
#             payload = json.loads(payload)
#
#         logger.info(payload)
#         response = requests.post(endpoint + "/client", json=payload, headers=headers)
#         status_code_check(response.status_code)
#         if status_code_check:
#             return response
#         else:
#             return False, response.json()
#     return _use_fixture_with_parameter


@pytest.fixture
def post_client_data(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env

        if file != 'e2e' or not isinstance(data, dict):
            data.update({'customer_id': customer_id})
        if file == True and not isinstance(data, dict):
            json_file = open(data)
            payload = json.load(json_file)
        elif (file == 'e2e' or isinstance(data, dict)) and context in data:
            data = data[context]
            data["customer_id"] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
            logger.info(payload)
        file_path = './jsons/create_client_contexts.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_client_data_superadmin(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env

        if file != 'e2e' or not isinstance(data, dict):
            data.update({'customer_id': customer_id})
        if file == True and not isinstance(data, dict):
            json_file = open(data)
            payload = json.load(json_file)
        elif (file == 'e2e' or isinstance(data, dict)) and context in data:
            data = data[context]
            data["customer_id"] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
            logger.info(payload)
        file_path = './jsons/create_client_contexts.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_client_data_with_customer_id(define_env):
    '''
    Function to send get request to get client details using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_client_data_superadmin_customer_id(define_env):
    '''
    Function to send get request to get client details using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_client_data_with_customer_id_user_1(define_env):
    '''
    Function to send get request to get client details using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token_superadmin()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_client_details(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/client", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_category_listing(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/report/category?type=Report", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter




@pytest.fixture
def patch_client_data(define_env):
    '''
    Function to send patch request to update the client details
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if file == 'e2e':
            data = data[context]
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_payload = json.dumps(data)
            json_payload = json.loads(json_payload)
            payload = {}
            payload.update(({context: json_payload}))
        if context == 'personal' :
           payload['personal']['date_of_birth'] = '2022-12-12'
        logger.info(payload)
        file_path = './jsons/create_client_contexts.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        logger.info(payload)
        response = requests.patch(endpoint + f"/client/{customer_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_client_commission_data(define_env):
    '''
    Function to send patch request to update the client details
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if file == 'e2e':
            data = data[context]
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_payload = json.dumps(data)
            json_payload = json.loads(json_payload)
            payload = {}
            payload.update(({context: json_payload}))
        logger.info(payload)
        file_path = './jsons/create_client_contexts.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        response = requests.patch(endpoint + f"/client/update_commission/{customer_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_outgoing_data(define_env):
    '''
    Function to send post request to add all data to expense
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        payload = common.update_outgoing_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_outgoing.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        logger.info(json_payload)
        response = requests.post(endpoint + "/assystcashflow/expense", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def patch_outgoing_data(define_env):
    '''
    Function to send post request to add all data to expense
    '''
    def _use_fixture_with_parameter(customer_id,expense_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        payload = common.update_outgoing_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_outgoing.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.patch(endpoint + f"/assystcashflow/expense/{expense_id}", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter




@pytest.fixture
def get_outgoing_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch outgoing data using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/assystcashflow/expense/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_outgoing_data_with_outgoing_id(define_env):
    '''
    Function to send get request to fetch expense data using expense id
    '''
    def _use_fixture_with_parameter(expense_id,customer_id):

        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_expense_data = requests.get(endpoint + f"/assystcashflow/expense/{expense_id}/customer/{customer_id}", headers=headers)
        status_code_check(get_expense_data.status_code)
        if status_code_check:
            return get_expense_data
        else:
            return False, get_expense_data.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_notes_data_with_customer_id(define_env):
    '''
       Function to send post request to add all data to expense
       '''

    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        # endpoint = "https://qa-middleware.assyst.cloud/client"
        payload = common.update_notes_json_data(customer_id)
        json_payload = json.loads(payload)
        #logger.info(json_payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j
        response = requests.post(endpoint + "/client", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_notes_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch contact note data using customer id
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env  # "https://qa-middleware.assyst.cloud"
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/notes/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter

@pytest.fixture
def get_notes_data_with_doc_id(define_env):
    '''
    Function to send get request to fetch contact note data using customer id
    '''

    def _use_fixture_with_parameter(doc_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/document/{doc_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter

@pytest.fixture
def post_fact_findnotes_outgoing_data_with_customer_id(define_env):
    '''
       Function to send post request to add all data to expense
       '''

    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        # endpoint = "https://qa-middleware.assyst.cloud/client"
        payload = common.update_fact_find_notes_json_data(customer_id)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j
        logger.info(json_payload)
        response = requests.post(endpoint + "/client", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_fact_find_notes_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch outgoing data using customer id
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env  # "https://qa-middleware.assyst.cloud"
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        params = {"type": 'fact-find'}
        get_client_data = requests.get(endpoint + f"/client/notes/{customer_id}?type=fact-find",params=params, headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter

@pytest.fixture
def get_fact_find_notes_data_with_notes_id(define_env):
    '''
    Function to send get request to fetch expense data using notes id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        #endpoint = "https://qa-middleware.assyst.cloud/client"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/note/notebycustomer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter

@pytest.fixture
def patch_employment_data(define_env):
    '''
    Function to send patch request to update the client details
    '''
    def _use_fixture_with_parameter(customer_id, employment_id, data,  context, file):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if file == 'e2e':
            data = data[context]
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        response = requests.patch(endpoint + f"/client/{customer_id}/employment/{employment_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_employment_data_superadmin(define_env):
    '''
    Function to send patch request to update the client details
    '''
    def _use_fixture_with_parameter(customer_id, employment_id, data,  context, file):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if file == 'e2e':
            data = data[context]
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        response = requests.patch(endpoint + f"/client/{customer_id}/employment/{employment_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_dependant_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch dependant data using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/depentant/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_folder_list_with_customer_id(define_env):
    '''
    Function to send get request to fetch dependant data using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/list-of-folders?customerid={customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_folder_list(define_env):
    '''
    Function to send get request to fetch dependant data using customer id
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/document/list-of-folder", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter




@pytest.fixture
def get_dependant_data_with_dependant_id(define_env):
    '''
    Function to send get request to fetch dependant data using customer id
    '''
    def _use_fixture_with_parameter(dependant_id, customer_id):
        endpoint = define_env
       # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        #endpoint = "https://qa-middleware.assyst.cloud/client"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/{dependant_id}/dependent/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_dependant_data(define_env):
    '''
    Function to send post request to add all data to dependant
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
             'Testing': "api-automation",
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        payload = common.update_dependant_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_dependant.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        response = requests.post(endpoint + "/client", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_folder_data(define_env):
    '''
    Function to send post request to add all data to dependant
    '''
    def _use_fixture_with_parameter(customer_id, data, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
             'Testing': "api-automation",
        }
        endpoint = define_env

        payload = common.update_document_folder_json_data(customer_id)
        payload = json.loads(payload)
        if file == True:
            pass
        
        else:
            for i, j in data.items():
                payload[i] = j

        

        response = requests.post(endpoint + "/client/create-folder", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response,payload
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_file_in_folder_data(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''
    def _use_fixture_with_parameter(customer_id,data,file,foldername):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation",
        }
        endpoint = define_env
        file_path = "C:/APITestAutomation/Screenshot.png"

        # Open the file here and ensure it remains open during the request
        file_obj = open(file_path, "rb")
        try:
            files = {'file': ('Screenshot.png', file_obj, 'image/png')}

            logger.info(data)
            payload = common.update_document_file_json_data(customer_id, foldername)
            logger.info(payload)
            json_payload = json.loads(payload)

            if file == True:
                pass
            else:
                for i, j in data.items():
                    json_payload[i] = j

            # Convert json_payload to form data
            form_data = {key: (str(value)) for key, value in json_payload.items()}
            logger.info(form_data)

            response = requests.post(endpoint+"/client/upload-file", files=files,  data=form_data, headers=headers)
            logger.info(response.json())
            status_code_check(response.status_code)
            if status_code_check:
                return response
            else:
                return False, response.json()
        finally:
            file_obj.close()

    return _use_fixture_with_parameter


# @pytest.fixture
# def post_file_in_folder_data(define_env):
#     '''
#     Function to send post request to create different contexts for a client
#     '''
#     def _use_fixture_with_parameter(customer_id,data,file,foldername):
#         bearer_token = get_bearer_token()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#             'Testing': "api-automation",
#         }
#         endpoint = define_env #"https://qa-api.assyst.cloud/secured/client"
#         with open("C:/Users/USER/Pictures/Screenshots/Screenshot 2024-08-14 105734.png", "rb") as File:
#             file_content = File.read()
#             files = {'file_name': file_content}
#         logger.info(data)
#         payload = common.update_document_file_json_data(customer_id,foldername)
#         logger.info(payload)
#         json_payload = json.loads(payload)
#
#         if file == True:
#            pass
#         else:
#             for i, j in data.items():
#                 json_payload[i] = j
#         # Convert json_payload to form data
#         form_data = {key: ( str(value)) for key, value in json_payload.items()}
#         logger.info(form_data)
#         response = requests.post(endpoint+"/client/upload-file",  files= files, data=form_data,  headers=headers)
#         logger.info(response.json())
#         status_code_check(response.status_code)
#         if status_code_check:
#             return response
#         else:
#             return False, response.json()
#
#     return _use_fixture_with_parameter


# @pytest.fixture
# def post_file_in_folder_data(define_env):
#     '''
#     Function to send POST request to create different contexts for a client
#     '''
#
#     def _use_fixture_with_parameter(customer_id, data, file, foldername):
#         bearer_token = get_bearer_token()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#             'Testing': "api-automation",
#         }
#         endpoint = define_env
#
#         # Open the file and prepare it for the form data
#         file_path = "C:/Users/USER/Pictures/Screenshots/Screenshot 2024-08-14 105734.png"
#         with open(file_path, "rb") as file_obj:
#             files = {'file': ('Screenshot.png', file_obj, 'image/png')}
#
#             # Prepare the form data payload
#             form_data = {
#                 'file_name': 'Screenshot.png',
#                 'folder_name': foldername,
#                 'date': '2040-04-02T05:37:51.247Z',
#                 'description': '',  # Assuming description is empty
#                 'customer_id': customer_id,
#                 'visible': 'public'
#             }
#
#             # Update form_data with additional data if file == False
#             if not file:
#                 form_data.update(data)
#
#             logger.info(form_data)
#
#             # Send the POST request with form data and files
#             response = requests.post(
#                 f"{endpoint}/client/upload-file",
#                 files=files,  # Files as binary
#                 data=form_data,  # Form data
#                 headers=headers
#             )
#
#             logger.info(response.json())
#             status_code_check(response.status_code)
#             if status_code_check:
#                 return response
#             else:
#                 return False, response.json()
#
#     return _use_fixture_with_parameter

@pytest.fixture
def post_folder_data_invalid_url(define_env):
    '''
    Function to send post request to add all data to dependant
    '''

    def _use_fixture_with_parameter(customer_id, data, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation",
        }
        endpoint = define_env

        payload = common.update_document_folder_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass

        else:
            for i, j in data.items():
                json_payload[i] = j

        response = requests.post(endpoint + "/client/create-", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def patch_dependant_data(define_env):
    '''
    Function to send patch request to update dependant data
    '''
    def _use_fixture_with_parameter(customer_id,dependant_id, data, context):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        json_data = json.dumps(data)
        json_payload = json.loads(json_data)
        payload = {}
        payload.update(({context: json_payload}))
        logger.info(payload)
        response = requests.patch(endpoint + f"/client/{customer_id}/depentant/{dependant_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_asset_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch asset data using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/asset/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/asset/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter


@pytest.fixture
def post_asset_data(define_env):
    '''
    Function to send post request to add data to assets
    '''
    def _use_fixture_with_parameter(customer_id,partner_cust_id,provider_correspondence_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }

        endpoint = define_env
        logger.info(partner_cust_id)
        payload = common.update_asset_json_data(provider_correspondence_id,customer_id, context)
        payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            payload = {}
            payload.update(({context: data}))
        else:
            for i, j in data.items():
                payload[context][i] = j


        file_path = './jsons/create_new_asset.json'
        expected_data_types = common.read_json(file_path)

        common.convert_data_types(payload, expected_data_types, context)
        if payload[context]['joint_indicator'] == 0:
            pass
        elif payload[context]['joint_indicator'] == 1:
             payload[context]["customer_id"] = partner_cust_id

        response = requests.post(endpoint + "/case/asset", json=payload, headers=headers)
        # response = requests.post(endpoint + "/asset", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_asset_data(define_env):
    '''
    Function to send patch request to update asset data
    '''
    def _use_fixture_with_parameter(customer_id,provider_correspondence_id, asset_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_json_data(provider_correspondence_id,customer_id, context)
        payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j

        file_path = './jsons/create_new_asset.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        response = requests.patch(endpoint + f"/case/asset/{asset_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/asset/{asset_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_asset_data(define_env):
    '''
    Function to send get request to fetch asset data
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/asset/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter

@pytest.fixture
def create_commission_client(define_env):
    '''
    Function to send post request to create a client
    '''
    def _use_fixture_with_parameter(data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing' : "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-middleware.assyst.cloud"
        if file == True:
            json_file = open(data)
            payload = json.load(json_file)
        elif file == 'e2e':
            data = data[context]
            payload = {}
            payload.update(({context: data}))
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))

        response = requests.post(endpoint + "/client/create_commission", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_asset_details_with_asset_id(define_env):
    '''
    Function to send get request to fetch asset data using asset id
    '''
    def _use_fixture_with_parameter(asset_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/asset/{asset_id}/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/asset/{asset_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_asset_withdrawal_data(define_env):
    '''
    Function to send post request to add data to asset payment
    '''
    def _use_fixture_with_parameter(customer_id, case_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_withdrawal_json_data(customer_id, case_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_asset_withdrawals.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.post(endpoint + "/case/withdrawal", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_withdrawal_data(define_env):
    '''
    Function to send patch request to update withdrawal data
    '''
    def _use_fixture_with_parameter(customer_id, withdrawal_id, case_id, data, context, file):
        logger.info(case_id)
        logger.info(withdrawal_id)
        logger.info(customer_id)
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_withdrawal_json_data(customer_id,case_id, context)
        payload = json.loads(payload)
        #logger.info(payload)

        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j

        file_path = './jsons/create_new_asset_withdrawals.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        logger.info(payload)
        response = requests.patch(endpoint + f"/case/withdrawal/{withdrawal_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/asset/{asset_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter
@pytest.fixture
def get_assetwithdrawal_with_asset_id(define_env):
    '''
    Function to send get request to fetch assetwithdrawal data
    '''
    def _use_fixture_with_parameter(customer_id,case_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/withdrawal/case/{case_id}/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_withdrawal_data_with_withdrawal_id(define_env):
    '''
    Function to send get request to fetch withdrawal data using withdrawal id
    '''
    def _use_fixture_with_parameter(withdrawal_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/withdrawal/{withdrawal_id}/customer/{customer_id}", headers=headers)
        # response = requests.get(endpoint + f"/get_payment/{case_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_valuation_data(define_env):
    '''
    Function to send post request to add data to asset payment
    '''
    def _use_fixture_with_parameter(customer_id, case_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_valuation_json_data(customer_id, case_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_valuations.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.post(endpoint + "/case/valuation", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_valuation_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/valuation/customer/{customer_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def patch_valuation_data(define_env):
    '''
    Function to send patch request to update withdrawal data
    '''
    def _use_fixture_with_parameter(customer_id, valuation_id, case_id, data, context, file):
        # logger.info(case_id)
        # logger.info(withdrawal_id)
        # logger.info(customer_id)
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_valuation_json_data(customer_id,case_id, context)
        payload = json.loads(payload)
        #logger.info(payload)

        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j

        file_path = './jsons/create_new_valuations.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        logger.info(payload)
        response = requests.patch(endpoint + f"/case/valuation/{valuation_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/asset/{asset_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter







@pytest.fixture
def get_valuation_data_with_case_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(case_id,customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/valuation/case/{case_id}/customer/{customer_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_valuation_data_with_valuation_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(customer_id,valuation_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/valuation/{valuation_id}/customer/{customer_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_policy_data(define_env):
    '''
    Function to send post request to add data to policy
    '''
    def _use_fixture_with_parameter(customer_id,partner_cust_id,provider_correspondence_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_policy_json_data(provider_correspondence_id,customer_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_policy.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        if json_payload[context]['policy_holder'] == 0:
            pass
        elif json_payload[context]['policy_holder'] == 1:
             json_payload[context]["customer_id"] = partner_cust_id
        response = requests.post(endpoint + "/case/policy", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/policy", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_policy_review_data(define_env):
    '''
    Function to send patch request to update asset payment data
    '''

    def _use_fixture_with_parameter(customer_id, case_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_payment_json_data(customer_id, case_id, context)
        payload = json.loads(payload)
        logger.info(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j
        file_path = './jsons/create_new_asset_payment.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        # logger.info(payload)

        response = requests.patch(endpoint + f"/case/policy/{case_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/update_payment/{payment_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter

@pytest.fixture
def post_manage_user_data(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(data,file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': 'api-automation'
        }
        endpoint = define_env
        logger.info(bearer_token)
        payload = common.update_manage_user(data)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[i] = j
        logger.info(json_payload)
        response = requests.post(endpoint + "/user", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter





@pytest.fixture
def get_user_id_details(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/user/profile/{user_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_user_id_details_invalid_token(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = "https://qa-middleware.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGcUpNZ3NsSkd4SE0xWUN2X003ZEJKeWdFeldfRFE2WkVwamg1Rml1c3RRIn0.eyJleHAiOjE3MTYxOTM2MjYsImlhdCI6MTcxNjE5MDAyNiwianRpIjoiYTMzMTY3ZDktNThjMy00OWI1LWIyNGUtNzZjNmFlZWNiMmI2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWRldi5hc3N5c3QuY2xvdWQvcmVhbG1zL3RlbmFudDItcmVhbG0iLCJhdWQiOiJyZWFsbS1tYW5hZ2VtZW50Iiwic3ViIjoiMzQ0ODUyM2MtY2YwNy00Zjc5LWFmZmQtNTUwY2M2NmY3NjU3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2Rldi5hc3N5c3QuY2xvdWQuczMtd2Vic2l0ZS11cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsImh0dHBzOi8vZGV2LWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwczovL3FhLWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwOi8vcWEuYXNzeXN0LmNsb3VkLnMzLXdlYnNpdGUtdXMtZWFzdC0xLmFtYXpvbmF3cy5jb20iLCJodHRwczovL3FhLW1pZGRsZXdhcmUuYXNzeXN0LmNsb3VkIiwiLyoiLCJodHRwOi8vbG9jYWxob3N0LmFzc3lzdC5jbG91ZDozMDAwIiwiaHR0cDovL2xvY2FsaG9zdDo0MDAwIiwiaHR0cHM6Ly9kZXYtbWlkZGxld2FyZS5hc3N5c3QuY2xvdWQiLCJodHRwczovL2Rldi5hc3N5c3QuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImFsbG93LWNyZWF0ZS11c2VyIiwiYWxsb3ctdXBkYXRlLW1hc3Rlci1kYXRhIiwiYWxsb3ctcmVhc3NpZ24tYWN0aW9ucyIsImFsbG93LXJlc3RyaWN0ZWQtY2xpZW50IiwiYWxsb3ctY2xpZW50LWV4cG9ydHMiLCJhbGxvdy12aWV3LWNsaWVudCIsImFsbG93LWNsaWVudC1yZXBvcnRzIiwiYWxsb3ctdXBkYXRlLWNsaWVudCIsImxpbWl0LWNsaWVudHMtZm9yLXVzZXIiLCJ2aWV3LWFsbC1jbGllbnQiLCJhbGxvdy1kZWxldGUtdXNlciIsImFsbG93LWJ1c2luZXNzLXJlcG9ydHMiLCJhbGxvdy1hZGQtY2xpZW50IiwiYWxsb3ctZGVsZXRlLWNsaWVudCIsImFsbG93LWFkZC11c2VyIiwiYWxsb3ctdmlldy11c2VyIiwiYWxsb3ctY2xpZW50LXVwbG9hZHMiLCJhbGxvdy11cGRhdGUtdXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1yZWFsbSIsInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfSwiY2xpZW50Ijp7InJvbGVzIjpbImFsbG93LWFkZC1jbGllbnQiLCJhbGxvdy12aWV3LWNsaWVudCJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsInNjaGVtYSI6InRlbmFudDIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkFtYXIgVHZtIiwicmVhbG0iOiJ0ZW5hbnQyLXJlYWxtIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYW1hcnR2bUB0ZWtrbm9sb2d5LmNvbSIsImdpdmVuX25hbWUiOiJBbWFyIiwiZmFtaWx5X25hbWUiOiJUdm0iLCJlbWFpbCI6ImFtYXJ0dm1AdGVra25vbG9neS5jb20ifQ.EJHQEAeyWtKLY6q_2OVsfj-tukoROQrIKvgXN8mIDiPyMXb6roPGND_ML_IDw7LRu7dJybcaYTevHUlh6ty-eTSQ5Q89Sh7qVYIJWRh90qvsH1O-Oh-AWB5jPla9VBBSZ-QauW7nbPgWvkBnzgA5fuiDTGgmAgwyRZs4SHGNdkz8nSK6VP2XgbwYp-k8g3r-tYbY78Qn2IEz7X-DlSvfU7BYOT2D3GdP7oyr9J8XOEBQz6QqBuFOuG_HeIpSbuTdjtEci1D68EpCWnD295l-w0C9vwjtoRkUA3qmh34snNO_2QqGm1syJO_pQ-VjF5-jMyUSOE03ZJJjew-qYJ9FFQ"}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/user/profile/{user_id}", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_user_role_details_using_user_id(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/user/auth/{user_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_user_role_details_with_invalid_token(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter(user_id):
        endpoint = "https://qa-middleware.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGcUpNZ3NsSkd4SE0xWUN2X003ZEJKeWdFeldfRFE2WkVwamg1Rml1c3RRIn0.eyJleHAiOjE3MTYxOTM2MjYsImlhdCI6MTcxNjE5MDAyNiwianRpIjoiYTMzMTY3ZDktNThjMy00OWI1LWIyNGUtNzZjNmFlZWNiMmI2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWRldi5hc3N5c3QuY2xvdWQvcmVhbG1zL3RlbmFudDItcmVhbG0iLCJhdWQiOiJyZWFsbS1tYW5hZ2VtZW50Iiwic3ViIjoiMzQ0ODUyM2MtY2YwNy00Zjc5LWFmZmQtNTUwY2M2NmY3NjU3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2Rldi5hc3N5c3QuY2xvdWQuczMtd2Vic2l0ZS11cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsImh0dHBzOi8vZGV2LWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwczovL3FhLWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwOi8vcWEuYXNzeXN0LmNsb3VkLnMzLXdlYnNpdGUtdXMtZWFzdC0xLmFtYXpvbmF3cy5jb20iLCJodHRwczovL3FhLW1pZGRsZXdhcmUuYXNzeXN0LmNsb3VkIiwiLyoiLCJodHRwOi8vbG9jYWxob3N0LmFzc3lzdC5jbG91ZDozMDAwIiwiaHR0cDovL2xvY2FsaG9zdDo0MDAwIiwiaHR0cHM6Ly9kZXYtbWlkZGxld2FyZS5hc3N5c3QuY2xvdWQiLCJodHRwczovL2Rldi5hc3N5c3QuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImFsbG93LWNyZWF0ZS11c2VyIiwiYWxsb3ctdXBkYXRlLW1hc3Rlci1kYXRhIiwiYWxsb3ctcmVhc3NpZ24tYWN0aW9ucyIsImFsbG93LXJlc3RyaWN0ZWQtY2xpZW50IiwiYWxsb3ctY2xpZW50LWV4cG9ydHMiLCJhbGxvdy12aWV3LWNsaWVudCIsImFsbG93LWNsaWVudC1yZXBvcnRzIiwiYWxsb3ctdXBkYXRlLWNsaWVudCIsImxpbWl0LWNsaWVudHMtZm9yLXVzZXIiLCJ2aWV3LWFsbC1jbGllbnQiLCJhbGxvdy1kZWxldGUtdXNlciIsImFsbG93LWJ1c2luZXNzLXJlcG9ydHMiLCJhbGxvdy1hZGQtY2xpZW50IiwiYWxsb3ctZGVsZXRlLWNsaWVudCIsImFsbG93LWFkZC11c2VyIiwiYWxsb3ctdmlldy11c2VyIiwiYWxsb3ctY2xpZW50LXVwbG9hZHMiLCJhbGxvdy11cGRhdGUtdXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1yZWFsbSIsInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfSwiY2xpZW50Ijp7InJvbGVzIjpbImFsbG93LWFkZC1jbGllbnQiLCJhbGxvdy12aWV3LWNsaWVudCJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsInNjaGVtYSI6InRlbmFudDIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkFtYXIgVHZtIiwicmVhbG0iOiJ0ZW5hbnQyLXJlYWxtIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYW1hcnR2bUB0ZWtrbm9sb2d5LmNvbSIsImdpdmVuX25hbWUiOiJBbWFyIiwiZmFtaWx5X25hbWUiOiJUdm0iLCJlbWFpbCI6ImFtYXJ0dm1AdGVra25vbG9neS5jb20ifQ.EJHQEAeyWtKLY6q_2OVsfj-tukoROQrIKvgXN8mIDiPyMXb6roPGND_ML_IDw7LRu7dJybcaYTevHUlh6ty-eTSQ5Q89Sh7qVYIJWRh90qvsH1O-Oh-AWB5jPla9VBBSZ-QauW7nbPgWvkBnzgA5fuiDTGgmAgwyRZs4SHGNdkz8nSK6VP2XgbwYp-k8g3r-tYbY78Qn2IEz7X-DlSvfU7BYOT2D3GdP7oyr9J8XOEBQz6QqBuFOuG_HeIpSbuTdjtEci1D68EpCWnD295l-w0C9vwjtoRkUA3qmh34snNO_2QqGm1syJO_pQ-VjF5-jMyUSOE03ZJJjew-qYJ9FFQ"}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/user/auth/{user_id}", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter


@pytest.fixture
def patch_manage_user_data(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(data,file,user_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': 'api-automation'
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud"
        #payload = common.update_manage_user(data)
        payload = json.dumps(data)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[i] = j

        response = requests.patch(endpoint + f"/user/{user_id}", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def patch_manage_user(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(data,file,user_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': 'api-automation'
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud"
        #payload = common.update_manage_user(data)
        payload = json.dumps(data)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[i] = j

        response = requests.patch(endpoint + f"/user/profile/{user_id}", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_manage_user_data_user_6(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(data,file,user_id):
        bearer_token = get_bearer_token_user_6()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': 'api-automation'
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud"
        #payload = common.update_manage_user(data)
        payload = json.dumps(data)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[i] = j

        response = requests.patch(endpoint + f"/user/{user_id}", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_manage_user_data_user_5(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(data,file):
        bearer_token = get_bearer_token_user_5()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': 'api-automation'
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud"
        payload = common.update_manage_user(data)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[i] = j

        response = requests.post(endpoint + "/user", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_vulnerability_data(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(customer_id,data,context,file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': 'api-automation'
        }
        endpoint = define_env


        if file == True:
            payload = common.update_vulnerability_post(customer_id)
            json_payload = json.loads(payload)

        else:

            payload = common.update_vulnerability(customer_id, data, context)
            json_payload = json.loads(payload)

        logger.info(json_payload)
        response = requests.post(endpoint + "/client/vulnerability", json=json_payload, headers=headers)
        #logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_vulnerability_data(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(customer_id,vulnerability_id,data,context,file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': 'api-automation'
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud"
        if file == True:
             data = data[context]
             data['customer_id'] = customer_id
             #logger.info(data)
             json_payload = {}
             json_payload.update(({context: data}))
        else:
            payload = common.update_vulnerability(customer_id, data, context)
            json_payload = json.loads(payload)
            for i, j in data.items():
                json_payload[i] = j

        response = requests.patch(endpoint + f"/client/vulnerability/{vulnerability_id}", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_vulnerability_driver_details(define_env):
    '''
    Function to send get request to get all vulnerability driver details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/client/vulnerability/driver", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_vulnerability_characteristics_details(define_env):
    '''
    Function to send get request to get all vulnerability driver characteristics details
    '''
    def _use_fixture_with_parameter(driver_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/vulnerability/characteristics/{driver_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_vulnerability_characteristics_empty_driver_id(define_env):
    '''
    Function to send get request to get all vulnerability driver characteristics details
    '''
    def _use_fixture_with_parameter(driver_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/vulnerability/characteristics/{driver_id}", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_vulnerability_using_customer_id(define_env):
    '''
    Function to send get request to get appointment details using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/vulnerability/customer/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def patch_asset_review_data(define_env):
    '''
    Function to send patch request to update asset payment data
    '''
    # def _use_fixture_with_parameter(asset_id, data, context, file):
    #     bearer_token = get_bearer_token()
    #     headers = {
    #         'Authorization': f'Bearer {bearer_token}',
    #         'Testing': "api-automation"
    #     }
    #     endpoint = define_env
    #     if file == True:
    #         pass
    #     else:
    #         json_data = json.dumps(data)
    #         json_payload = json.loads(json_data)
    #         payload = {}
    #         payload.update(({context: json_payload}))
    #
    #     file_path = './jsons/create_new_asset_review.json'
    #     expected_data_types = common.read_json(file_path)
    #     common.convert_data_types(payload, expected_data_types, context)
    #
    #     response = requests.patch(endpoint + f"/case/asset/{asset_id}", json=payload, headers=headers)
    #     status_code_check(response.status_code)
    #     if status_code_check:
    #         return response
    #     else:
    #         return False, response.json()
    # return _use_fixture_with_parameter
    def _use_fixture_with_parameter(customer_id, case_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing' : "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_payment_json_data(customer_id, case_id, context)
        payload = json.loads(payload)
        logger.info(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j
        file_path = './jsons/create_new_asset_payment.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        #logger.info(payload)

        response = requests.patch(endpoint + f"/case/asset/{case_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/update_payment/{payment_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter



@pytest.fixture
def patch_liability_review_data(define_env):
    '''
    Function to send patch request to update asset payment data
    '''

    def _use_fixture_with_parameter(customer_id, case_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_payment_json_data(customer_id, case_id, context)
        payload = json.loads(payload)
        logger.info(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j
        file_path = './jsons/create_new_asset_payment.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        # logger.info(payload)

        response = requests.patch(endpoint + f"/case/liability/{case_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/update_payment/{payment_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_policy_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch policy data
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/policy/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/policy/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_policy_data_with_policy_id(define_env):
    '''
    Function to send get request to fetch policy data using policy id
    '''
    def _use_fixture_with_parameter(policy_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/policy/{policy_id}/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/policy/{policy_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_policy_data(define_env):
    '''
    Function to send patch request to update asset data
    '''
    def _use_fixture_with_parameter(provider_correspondence_id,customer_id, policy_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_policy_json_data(provider_correspondence_id,customer_id, context)
        payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j

        file_path = './jsons/create_new_policy.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        logger.info(payload)
        response = requests.patch(endpoint + f"/case/policy/{policy_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/asset/{asset_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def post_income_data(define_env):
    '''
    Function to send post request to add data to income
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        payload = common.update_json_data(customer_id, context)
        logger.info(data)

        json_payload = json.loads(payload)
        if data["income"]["owner"] == 1 :
            json_payload['income']['owner'] = 1
        logger.info(json_payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data["customer_id"] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_income.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        response = requests.post(endpoint + "/assystcashflow/income", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_income_superadmin(define_env):
    '''
    Function to send post request to add data to income
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token_superadmin()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        payload = common.update_json_data(customer_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data["customer_id"] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_income.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        response = requests.post(endpoint + "/assystcashflow/income", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_income_with_income_id(define_env):
    '''
    Function to send get request to fetch addressbook data
    '''
    def _use_fixture_with_parameter(income_id,customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/assystcashflow/income/{income_id}/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_email_using_templateid_custid(define_env):
    '''
    Function to send get request to fetch addressbook data
    '''
    def _use_fixture_with_parameter(template_id,customer_id):
        endpoint = define_env

        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/notification/get-template/{template_id}/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_income_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch income data
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/assystcashflow/income/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_income_data(define_env):
    '''
    Function to send patch request to update asset data
    '''
    def _use_fixture_with_parameter(customer_id, income_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_json_data(customer_id, context)
        payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j

        file_path = './jsons/create_new_income.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        logger.info(payload)
        response = requests.patch(endpoint + f"/assystcashflow/income/{income_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/asset/{asset_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def patch_profile_data(define_env):
    '''
    Function to send patch request to update asset data
    '''
    def _use_fixture_with_parameter( data,id, file):
        bearer_token = get_bearer_token_profile()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_profile_data()
        logger.info(payload)
        payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[i] = j


        logger.info(payload)
        response = requests.patch(endpoint + f"/user/profile/{id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/asset/{asset_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def patch_income_superadmin(define_env):
    '''
    Function to send patch request to update asset data
    '''
    def _use_fixture_with_parameter(customer_id, income_id, data, context, file):
        bearer_token = get_bearer_token_superadmin()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_json_data(customer_id, context)
        payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j

        file_path = './jsons/create_new_income.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        logger.info(payload)
        response = requests.patch(endpoint + f"/assystcashflow/income/{income_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/asset/{asset_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def post_asset_commission_data(define_env):
    '''
    Function to send post request to add data to asset payment commission
    '''
    def _use_fixture_with_parameter(customer_id, case_id, payment_id,  data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_commission_json_data(customer_id, case_id, payment_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_asset_payment_commission.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.post(endpoint + "/case/commission", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_asset_commission_data_with_payment_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(customer_id,payment_id,case_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/commission/{payment_id}/customer/{customer_id}/case/{case_id}", headers=headers)
        #response = requests.get(endpoint + f"/case/commissionbycustomer/{customer_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_asset_commission_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/commissionbycustomer/{customer_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_asset_commission_data_with_commission_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(customer_id,commission_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/commission/{commission_id}/customer/{customer_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def patch_payment_commission_data(define_env):
    '''
    Function to send patch request to update withdrawal data
    '''
    def _use_fixture_with_parameter(customer_id, commission_id, case_id,payment_id, data, context, file):

        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_commission_json_data(customer_id,case_id,payment_id,context)
        payload = json.loads(payload)
        #logger.info(payload)

        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j

        file_path = './jsons/create_new_asset_payment_commission.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        #logger.info(payload)
        response = requests.patch(endpoint + f"/case/commission/{commission_id}", json=payload, headers=headers)

        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



# @pytest.fixture
# def post_addressbook_data(define_env):
#     '''
#     Function to send post request to add data to addressbook
#     '''
#     def _use_fixture_with_parameter(customer_id, data, context, file):
#         bearer_token = get_bearer_token()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#         }
#         endpoint = define_env
#         #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
#         payload = common.update_json_data(customer_id, context)
#         json_payload = json.loads(payload)
#         if file == True:
#             pass
#         elif file == 'e2e':
#             data = data[context]
#             data["customer_id"] = customer_id
#             json_payload = {}
#             json_payload.update(({context: data}))
#         else:
#             for i, j in data.items():
#                 json_payload[context][i] = j
#         response = requests.post(endpoint + "/client", json=json_payload, headers=headers)
#         status_code_check(response.status_code)
#         if status_code_check:
#             return response
#         else:
#             return False, response.json()
#     return _use_fixture_with_parameter
@pytest.fixture
def post_addressbook_data(define_env):
    '''
    Function to send post request to add data to addressbook
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        logger.info(data)
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
       # endpoint = "https://qa-middleware.assyst.cloud/client"
        payload = common.update_json_data(customer_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data["customer_id"] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_addressbook.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        response = requests.post(endpoint +"/client", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/addressbook", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_addressbook_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch addressbook data
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/addressbook/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_addressbook_data_with_address_id(define_env):
    '''
    Function to send get request to fetch addressbook data
    '''
    def _use_fixture_with_parameter(customer_id,address_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/{address_id}/addressbook/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_addressbook_data(define_env):
    '''
        Function to send patch request to update the addressbook details
        '''

    def _use_fixture_with_parameter(customer_id,address_id, data, context, file):
        logger.info(data)
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        #endpoint = "https://qa-middleware.assyst.cloud/client"
        payload = common.update_json_data(customer_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data["customer_id"] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j
        logger.info(json_payload)
        file_path = './jsons/create_new_addressbook.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        response = requests.patch(endpoint + f"/client/{customer_id}/addressbook/{address_id}", json=json_payload,
                                  headers=headers)
        # response = requests.post(endpoint + "/addressbook", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter




@pytest.fixture
def post_attituderisk_data(define_env):
    '''
    Function to send post request to add data to attitude risk
    '''
    def _use_fixture_with_parameter(customer_id, type, data, file, context):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        if file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            payload = common.update_json_data(customer_id, 'attitude')
            json_payload = json.loads(payload)

        if type == 'attituderisk':
            response = requests.post(endpoint + "/client", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def patch_attitude_data(define_env):
    '''
    Function to send patch request to update dependant data
    '''
    def _use_fixture_with_parameter(customer_id,attitude_id, data, context,file):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        # logger.info(customer_id)
        # logger.info(attitude_id)
        if file == 'e2e':
            data = data[context]
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
            logger.info(payload)
        response = requests.patch(endpoint + f"/client/{customer_id}/attituderisk/{attitude_id}", json=payload,
                                  headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter

@pytest.fixture
def get_attituderisk_data(define_env):
    '''
    Function to send get request to fetch attituderisk data
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/attituderisk/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


# @pytest.fixture
# def post_liability_data(define_env):
#     '''
#     Function to send post request to add data to liability
#     '''
#     def _use_fixture_with_parameter(customer_id,provider_correspondence_id, data, context, file):
#         bearer_token = get_bearer_token()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#             'Testing': "api-automation"
#         }
#         endpoint = define_env
#         payload = common.update_liability_json_data(customer_id,provider_correspondence_id, context)
#         json_payload = json.loads(payload)
#         if file == True:
#             pass
#         elif file == 'e2e':
#             data = data[context]
#             data['customer_id'] = customer_id
#             #data['provider_id'] = customer_id
#             json_payload = {}
#             json_payload.update(({context: data}))
#         else:
#             for i, j in data.items():
#                 json_payload[context][i] = j
#
#         file_path = './jsons/create_new_liability.json'
#         expected_data_types = common.read_json(file_path)
#         common.convert_data_types(json_payload, expected_data_types, context)
#
#         response = requests.post(endpoint + "/case/liability", json=json_payload, headers=headers)
#         # response = requests.post(endpoint + "/liability", json=json_payload, headers=headers)
#         status_code_check(response.status_code)
#         if status_code_check:
#             return response
#         else:
#             return False, response.json()
#     return _use_fixture_with_parameter

@pytest.fixture
def post_liability_data(define_env):
    '''
    Function to send post request to add data to liability
    '''
    def _use_fixture_with_parameter(customer_id,partner_cust_id,provider_correspondence_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_liability_json_data(customer_id,provider_correspondence_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id

            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_liability.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        if json_payload[context]['joint_indicator'] == 0:
            pass
        elif json_payload[context]['joint_indicator'] == 1:
            json_payload[context]["customer_id"] = partner_cust_id



        response = requests.post(endpoint + "/case/liability", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/liability", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_liability_data(define_env):
    '''
    Function to send patch request to update data to liability
    '''
    def _use_fixture_with_parameter(customer_id,provider_correspondence_id, liability_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_liability_json_data(customer_id,provider_correspondence_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            data['provider_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_liability.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        response = requests.patch(endpoint + f"/case/liability/{liability_id}", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/liability", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_liability_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch liability data
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/liability/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/liability/liabilitybycustomer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_liability_data_with_liability_id(define_env):
    '''
    Function to send get request to fetch liability data using liability id
    '''
    def _use_fixture_with_parameter(liability_id, customerid):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/liability/{liability_id}/customer/{customerid}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/liability/{liability_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_business_data(define_env):
    '''
    Function to send post request to add data to action
    '''
    def _use_fixture_with_parameter(customer_id, case_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_business_json_data(customer_id, case_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_business.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        response = requests.post(endpoint + "/case/business", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/business", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_business_data_with_case_id(define_env):
    '''
    Function to send get request to fetch action data
    '''
    def _use_fixture_with_parameter(case_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/business/customer/{customer_id}/case/{case_id}", headers=headers)
        # response = requests.get(endpoint + f"/business/business_case/{case_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_business_data_with_action_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(action_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/business/{action_id}/customer/{customer_id}", headers=headers)
        # response = requests.get(endpoint + f"/business/business_action/{action_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_business_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/business/customer/{customer_id}", headers=headers)
        # response = requests.get(endpoint + f"/business/business_action/{action_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def patch_business_data(define_env):
    '''
    Function to send patch request to update action data
    '''
    def _use_fixture_with_parameter(customer_id, case_id, business_id,  data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_business_json_data(customer_id, case_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_business.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)

        response = requests.patch(endpoint + f"/case/business/{business_id}", json=json_payload, headers=headers)
        # response = requests.patch(endpoint + f"/business/{business_id}", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_asset_payment_data(define_env):
    '''
    Function to send post request to add data to asset payment
    '''
    def _use_fixture_with_parameter(customer_id, case_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_payment_json_data(customer_id, case_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        file_path = './jsons/create_new_asset_payment.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.post(endpoint + "/case/payments", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/add_payment", json=json_payload, headers=headers)

        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_payment_data_with_case_id(define_env):
    '''
    Function to send get request to fetch payment data using case id
    '''
    def _use_fixture_with_parameter(case_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/payments/case/{case_id}/customer/{customer_id}", headers=headers)
        # response = requests.get(endpoint + f"/get_payment/{case_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_asset_payment_data(define_env):
    '''
    Function to send patch request to update asset payment data
    '''
    def _use_fixture_with_parameter(customer_id, case_id,payment_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_asset_payment_json_data(customer_id, case_id, context)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[context][i] = j
        file_path = './jsons/create_new_asset_payment.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.patch(endpoint + f"/case/payments/{payment_id}", json=json_payload, headers=headers)
        # response = requests.patch(endpoint + f"/update_payment/{payment_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter




@pytest.fixture
def get_appointment_data_with_appointment_id(define_env):
    '''
    Function to send get request to get appointment details using appointment id
    '''
    def _use_fixture_with_parameter(appointment_id, customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/appointment/{appointment_id}/customer/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_appointment_data_with_customer_id(define_env):
    '''
    Function to send get request to get appointment details using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/appointmentbycustomer/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def patch_appointment_data(define_env):
    '''
    Function to send patch request to update the appointment details
    '''
    def _use_fixture_with_parameter(customer_id, appointment_id, data, context, file):
        endpoint = define_env
        #endpoint = 'https://qa-api.assyst.cloud/asc/api/v1.0'
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        payload = common.update_client_action_json_data(customer_id)
        json_payload = json.loads(payload)
        # if file == 'e2e':
        #     data = data[context]
        #     json_payload = {}
        #     json_payload.update(({context: data}))
        #     payload = json.dumps(json_payload)
        #     payload = json.loads(payload)
        # else:
        #     logger.info(json_payload)
        #     json_payload = json.dumps(data)
        #     json_payload = json.loads(json_payload)
        #     payload = {}
        #     payload.update(({context: json_payload}))
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[i] = j


        logger.info(json_payload)
        response = requests.patch(endpoint + f"/client/appointment/{appointment_id}", json=json_payload,
                                  headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter
#
# @pytest.fixture
# def patch_fact_findnote_data(define_env):
#     '''
#     Function to send post request to create different contexts for a client
#     '''
#     def _use_fixture_with_parameter(customer_id,note_id,data,file):
#         bearer_token = get_bearer_token()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#             'Testing': "api-automation"
#         }
#         endpoint = define_env
#         with open("C:/Users/USER/Pictures/Screenshots/Screenshot 2024-08-14 105734.png", "rb") as File:
#             file_content = File.read()
#             files = {'file': file_content}
#         logger.info(data)
#         payload = common.update_fact_find_notes_json_data(customer_id)
#         #logger.info(customer_id)
#         #logger.info(note_id)
#         json_payload = json.loads(payload)
#         if file == True:
#            pass
#         else:
#             for i, j in data.items():
#                 json_payload[i] = j
#         #logger.info(json_payload)
#         #response = requests.patch(endpoint + f"/client/{customer_id}/note/{note_id}", data=json_payload, files=files, headers=headers)
#         response = requests.patch(endpoint + f"/client/notes/{note_id}", data=json_payload, files=files, headers=headers)
#         status_code_check(response.status_code)
#         if status_code_check:
#             return response
#         else:
#             return False, response.json()
#
#     return _use_fixture_with_parameter

@pytest.fixture
def patch_fact_findnote_data(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''

    def _use_fixture_with_parameter(customer_id, note_id, data, file_link, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation",
            'userid': "c854b92b-f0c8-4308-ba5f-c3708bb765d9"
        }
        endpoint = define_env
        # file_path = "C:/APITestAutomation/Screenshot.png"
        #
        # # Open the file and ensure it remains open during the request
        # file_obj = open(file_path, "rb")
        # try:
        #     files = {'file': ('Screenshot.png', file_obj)}
        #     logger.info(data)
        payload = common.update_fact_find_notes_json_data(customer_id)
        logger.info(payload)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[i] = j
        logger.info(json_payload)
        json_payload['file'] = file_link
        logger.info(json_payload)
        # Convert json_payload to form data
        form_data = {key: str(value) for key, value in json_payload.items()}
        logger.info(form_data)

        # response = requests.patch(endpoint + f"/client/{customer_id}/note/{note_id}", data=json_payload, files=files, headers=headers)
        response = requests.patch(endpoint + f"/client/notes/{note_id}", data=form_data, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
        # finally:
        #     file_obj.close()

    return _use_fixture_with_parameter


@pytest.fixture
def patch_note_data(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''
    def _use_fixture_with_parameter(customer_id,note_id,data,file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation",
             'userid': "82b8f31c-81b2-403c-87ff-176129d1b64f"
        }
        endpoint = define_env
        with open("C:/APITestAutomation/Screenshot.png", "rb") as File:
            file_content = File.read()
            files = {'file': file_content}
        logger.info(data)
        payload = common.update_notes_json_data(customer_id)
        #logger.info(customer_id)
        #logger.info(note_id)
        json_payload = json.loads(payload)
        if file == True:
           pass
        else:
            for i, j in data.items():
                json_payload[i] = j
        #logger.info(json_payload)
        #response = requests.patch(endpoint + f"/client/{customer_id}/note/{note_id}", data=json_payload, files=files, headers=headers)
        response = requests.patch(endpoint + f"/client/notes/{note_id}", data=json_payload, files=files, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


# @pytest.fixture
# def patch_employment_data(define_env):
#     '''
#     Function to send patch request to update the client details
#     '''
#     def _use_fixture_with_parameter(customer_id,employment_id, data,  context, file):
#         endpoint = define_env
#         bearer_token = get_bearer_token()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#             'Testing': "api-automation"
#         }
#         if file == 'e2e':
#             data = data[context]
#             json_payload = {}
#             json_payload.update(({context: data}))
#             payload = json.dumps(json_payload)
#             payload = json.loads(payload)
#         else:
#             json_data = json.dumps(data)
#             json_payload = json.loads(json_data)
#             payload = {}
#             payload.update(({context: json_payload}))
#         response = requests.patch(endpoint + f"/client/{customer_id}/employment/{employment_id}", json=payload, headers=headers)
#         status_code_check(response.status_code)
#         if status_code_check:
#             return response
#         else:
#             return False, response.json()
#     return _use_fixture_with_parameter

@pytest.fixture
def patch_clientservicetype_data(define_env):
    '''
    Function to send patch request to update the client details
    '''
    def _use_fixture_with_parameter(customer_id, servicetype_id, data, context, file):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if file == 'e2e':
            data = data[context]
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        file_path = './jsons/create_new_servicetype.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)

        response = requests.patch(endpoint + f"/client/{customer_id}/servicetype/{servicetype_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def patch_clientidentity_data(define_env):
    '''
    Function to send patch request to update the client details
    '''
    def _use_fixture_with_parameter(customer_id, identity_id, data, context, file):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if file == 'e2e':
            data = data[context]
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))

        file_path = './jsons/create_new_identity.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        response = requests.patch(endpoint + f"/client/{customer_id}/identity/{identity_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def patch_clientobjectives_data(define_env):
    '''
    Function to send patch request to update the client details
    '''
    def _use_fixture_with_parameter(customer_id, objective_id, data, context, file):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if file == 'e2e':
            data = data[context]
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        file_path = './jsons/create_new_objectives.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        response = requests.patch(endpoint + f"/client/{customer_id}/objective/{objective_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_timeallocation_data_with_customer_id(define_env):
    '''
    Function to send get request to get client details using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/timeallocationbycustomer/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def patch_commission_data(define_env):
    '''
    Function to send post request to add all data to expense
    '''
    def _use_fixture_with_parameter(customer_id,commission_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_commission_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        logger.info(json_payload)
        response = requests.patch(endpoint + f"/client/{customer_id}/commission/{commission_id}", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_commission_data_with_customer_id(define_env):
    '''
    Function to send get request to get client details using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/commissionbycustomer/customer/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_commission_data_with_commission_id(define_env):
    '''
    Function to send get request to get client details using commission id
    '''
    def _use_fixture_with_parameter(customer_id,commission_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/commission/{commission_id}/customer/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter





@pytest.fixture
def get_timeallocation_data_with_timeallocation_id(define_env):
    '''
    Function to send get request to get client details using timeallocation_id
    '''
    def _use_fixture_with_parameter(customer_id,timeallocation_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/timeallocation/{timeallocation_id}/customer/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter



@pytest.fixture
def patch_timeallocation_data(define_env):
    '''
    Function to send post request to add all data to expense
    '''
    def _use_fixture_with_parameter(customer_id,timeallocation_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_timeallocation_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j

        response = requests.patch(endpoint + f"/client/{customer_id}/timeallocation/{timeallocation_id}", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_fund_data(define_env):
    '''
    Function to send post request to add data to asset fund
    '''
    def _use_fixture_with_parameter(customer_id, case_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_fund_json_data(customer_id, case_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[context][i] = j
                #FUND-CREATE   dev-middleware.assyst.cloud/case/fund

        file_path = './jsons/create_new_funds.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        logger.info(json_payload)

        response = requests.post(endpoint + "/case/fund", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/add_payment", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def patch_fund_data(define_env):
    '''
    Function to send patch request to update withdrawal data
    '''
    def _use_fixture_with_parameter(customer_id, fund_id, case_id, data, context, file):
        # logger.info(case_id)
        # logger.info(withdrawal_id)
        # logger.info(customer_id)
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common. update_fund_json_data(customer_id,case_id, context)
        payload = json.loads(payload)
        #logger.info(payload)

        if file == True:
            pass
        else:
            for i, j in data.items():
                payload[context][i] = j

        file_path = './jsons/create_new_funds.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        logger.info(payload)
        response = requests.patch(endpoint + f"/case/fund/{fund_id}", json=payload, headers=headers)
        # response = requests.patch(endpoint + f"/asset/{asset_id}", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_fund_data_with_fund_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(fund_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/fund/{fund_id}/customer/{customer_id}", headers=headers)
        # response = requests.get(endpoint + f"/business/business_action/{action_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_fund_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/fund/customer/{customer_id}", headers=headers)
        # response = requests.get(endpoint + f"/business/business_action/{action_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_partner_data(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        logger.info(type(data))
        endpoint = define_env
        payload = common.update_partner_json_data(customer_id, context)
        payloads = json.loads(payload)
        json_payload = payloads[context]
        up_json_payload = {}
        up_json_payload.update(({context: json_payload}))
        logger.info(up_json_payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                up_json_payload[context][i] = j

        file_path = './jsons/create_client_contexts.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(up_json_payload, expected_data_types, context)
        response = requests.post(endpoint + "/client", json=up_json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_client_data_with_partner_customer_id(define_env):
    '''
    Function to send get request to get client details using customer id
    '''
    def _use_fixture_with_parameter(partner_cust_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/{partner_cust_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_attituderisk_partner_data(define_env):
    '''
    Function to send post request to add data to attitude risk
    '''
    def _use_fixture_with_parameter(customer_id, type, data, file, context):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        if file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))

        else:
            payload = common.update_json_data(customer_id, 'attitude')
            json_payload = json.loads(payload)

        if type == 'attituderisk':
            response = requests.post(endpoint + "/client", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

#
# @pytest.fixture
# def post_expense_category_data(define_env):
#     '''
#     Function to send post request to add all data to expense
#     '''
#     def _use_fixture_with_parameter(data, context, file):
#         bearer_token = get_bearer_token()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#         }
#         endpoint = define_env
#         json_file_path = './jsons/create_new_expense_category.json'
#         payload = common.read_json(json_file_path)
#         logger.info(payload)
#         json_payload = json.loads(payload)
#         if file == True:
#             pass
#         else:
#             for i, j in data.items():
#                 json_payload[context][i] = j
#         # expected_data_types = common.read_json(json_file_path)
#         # common.convert_data_types(json_payload, expected_data_types, context)
#
#         response = requests.post(endpoint + "/masterdata/transactions/expensecategories", json=json_payload, headers=headers)
#         status_code_check(response.status_code)
#         if status_code_check:
#             return response
#         else:
#             return False, response.json()
#
#     return _use_fixture_with_parameter


@pytest.fixture
def post_system_manager_data(define_env):
    '''
    Function to send post request to add all data to system manager
    '''
    def _use_fixture_with_parameter(data, context, file):
        # payload = None

        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing'  : "api-automation"
        }
        endpoint = define_env
        logger.info(data)
        if file == True:
            json_payload = common.read_json(data)
            #logger.info(json_payload)
            json_payload = json_payload[context]
            logger.info(json_payload)
            payload = {}
            payload.update(({context: json_payload}))
            logger.info(payload)
            if context == 'user_defined_field':
                common.update_name_field(payload,context,"name")
            logger.info(payload)
            # pass
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
            logger.info(payload)
            if context == 'user_defined_field':
                common.update_name_field(payload,context,"name")
            logger.info(payload)
        file_path = './jsons/create_new_systemmanager.json'
        # expected_data_types = common.read_json(file_path)
        # common.convert_data_types(payload, expected_data_types, context)

        if context == 'expense_category':
            response = requests.post(endpoint + "/masterdata/transactions/expensecategories", json=payload,
                                     headers=headers)
        elif context == 'income_category':
            response = requests.post(endpoint + "/masterdata/transactions/incomecategories", json=payload,
                                 headers=headers)
        elif context == 'attitude_to_risk_category':
            response = requests.post(endpoint + "/masterdata/attituderisk/categories", json=payload,
                                 headers=headers)
        elif context == 'attitude_to_risk_rating':
            response = requests.post(endpoint + "/masterdata/attituderisk/ratings", json=payload,
                                 headers=headers)
        elif context == 'objectives_detail':
            response = requests.post(endpoint + "/masterdata/objectives", json=payload,
                                 headers=headers)
        elif context == 'objectives_category':
            response = requests.post(endpoint + "/masterdata/objective/category", json=payload,
                                     headers=headers)
        elif context == 'provider':
            response = requests.post(endpoint + "/masterdata/providers", json=payload,
                                 headers=headers)
        elif context == 'tracking_case_actions':
            response = requests.post(endpoint + "/masterdata/standardtracking", json=payload,
                                 headers=headers)
        elif context == 'tracking_client_actions':
            response = requests.post(endpoint + "/masterdata/standardtracking", json=payload,
                                 headers=headers)
        elif context == 'user_defined_field':

            response = requests.post(endpoint + "/masterdata/userdefined/field", json=payload,
                                 headers=headers)
        else:
            logger.error("Context Not Implemented")
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_systemmanager_commissiontype_data(define_env):
    '''
    Function to send post request to add all data to system manager
    '''

    def _use_fixture_with_parameter(data, context, file):
        payload = None
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        logger.info(data)

        if file == True:
            json_payload = common.read_json(data)
            json_payload = json_payload[context]
            logger.info(json_payload)
            payload = {}
            payload.update(({context: json_payload}))


        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
            logger.info(payload)
            file_path = './jsons/create_new_systemmanager_commissiontype.json'
            expected_data_types = common.read_json(file_path)
            common.convert_data_types(payload, expected_data_types, context)
        if context == 'commission_types':
             response = requests.post(endpoint + "/masterdata/commission/commissiontypes", json=payload,
                                 headers=headers)
        elif context == 'commission_rule':
             response = requests.post(endpoint + "/masterdata/commission/commissionrule", json=payload,
                                 headers=headers)

        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_commission_type(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/commission/commissiontypes", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_invali_context_commission_type(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/commission/commissiont", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter


@pytest.fixture
def patch_systemmanager_commissiontype_data(define_env):
    '''
    Function to send post request to add all data to system manager
    '''

    def _use_fixture_with_parameter(commission_id,data, context, file):
        payload = None
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        logger.info(data)
        if file == True:
            json_payload = common.read_json(data)
            # logger.info(json_payload)
            json_payload = json_payload[context]
            logger.info(json_payload)
            payload = {}
            payload.update(({context: json_payload}))
            # logger.info(payload)
            # pass
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
            logger.info(payload)
            file_path = './jsons/create_new_systemmanager_commissiontype.json'
            expected_data_types = common.read_json(file_path)
            common.convert_data_types(payload, expected_data_types, context)
        if context == 'commission_types':
            response = requests.patch(endpoint + f"/masterdata/commission/commissiontypes/{commission_id}",json=payload,
                                      headers=headers)
        if context == 'commission_rule':
            response = requests.patch(endpoint + f"/masterdata/commission/commissionrule/{commission_id}", json=payload,
                                      headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter




@pytest.fixture
def patch_system_data(define_env):
    '''
    Function to send post request to add all data to system manager
    '''
    def _use_fixture_with_parameter(category_id, data, context, file):
        payload = None
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        if file == True:
            pass
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
            logger.info(payload)
        if context == 'expense_category':
            response = requests.patch(endpoint + f"/masterdata/transactions/expensecategories/{category_id}", json=payload,
                                     headers=headers)
        elif context == 'income_category':
            response = requests.patch(endpoint + f"/masterdata/transactions/incomecategories/{category_id}", json=payload,
                                 headers=headers)
        elif context == 'attitude_to_risk_category':
            response = requests.patch(endpoint + f"/masterdata/attituderisk/categories/{category_id}", json=payload,
                                 headers=headers)
        elif context == 'attitude_to_risk_rating':
            response = requests.patch(endpoint + f"/masterdata/attituderisk/ratings/{category_id}", json=payload,
                                 headers=headers)
        elif context == 'objectives_detail':
            response = requests.patch(endpoint + f"/masterdata/objectives/{category_id}", json=payload,
                                 headers=headers)
        elif context == 'objectives_category':
            response = requests.patch(endpoint + f"/masterdata/objective/category/{category_id}", json=payload,
                                 headers=headers)
        elif context == 'provider':
            response = requests.patch(endpoint + f"/masterdata/providers/{category_id}", json=payload,
                                      headers=headers)
        elif context == 'tracking_client_actions':
            response = requests.patch(endpoint + f"/masterdata/standardtracking/{category_id}", json=payload,
                                      headers=headers)
        elif context == 'tracking_case_actions':
            response = requests.patch(endpoint + f"/masterdata/standardtracking/{category_id}", json=payload,
                                      headers=headers)


        elif context == 'user_defined_field':

            common.update_name_field(payload, context, "name")
            logger.info(payload)
            response = requests.patch(endpoint + f"/masterdata/userdefined/field/{category_id}", json=payload,

                                      headers=headers)

        else:
            logger.error("Context Not Implemented")

        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_expense_category_details(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/transactions/expensecategories", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_income_details(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/transactions/incomecategories", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_attitude_category_details(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/attituderisk/categories", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_attitude_rating_details(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/attituderisk/ratings", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_objective_details(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/objectives", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_casesummary_liability_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch liability data
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/liability/casesummary/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/liability/liabilitybycustomer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_case_summary_policy_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch policy data
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/policy/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/policy/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_case_summary_asset_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch asset data using customer id
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/asset/casesummary/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/asset/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_payment_casesummary_data_with_case_id(define_env):
    '''
    Function to send get request to fetch asset data using customer id
    '''
    def _use_fixture_with_parameter(customer_id,case_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/payments/case/{case_id}/customer/{customer_id}", headers=headers)
        # get_client_data = requests.get(endpoint + f"/asset/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter

@pytest.fixture
def get_fund_casesummary_data_with_case_id(define_env):
    '''
    Function to send get request to fetch action data using business id
    '''
    def _use_fixture_with_parameter(case_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        response = requests.get(endpoint + f"/case/fund/customer/{customer_id}/case/{case_id}", headers=headers)
        # response = requests.get(endpoint + f"/business/business_action/{action_id}", headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_business_casesummary_data_with_case_id(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter(case_id,customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/business/customer/{customer_id}/case/{case_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_assetwithdrawal_casesummary_data_with_case_id(define_env):
    '''
    Function to send get request to fetch assetwithdrawal data
    '''

    def _use_fixture_with_parameter(case_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/withdrawal/case/{case_id}/customer/{customer_id}",
                                       headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_valuation_casesummary_data_with_case_id(define_env):
    '''
    Function to send get request to fetch assetwithdrawal data
    '''
    def _use_fixture_with_parameter(case_id, customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/valuation/case/{case_id}/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter





@pytest.fixture
def get_note_clientsummary_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch note of client summary
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud/secured/client"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        logger.info(customer_id)

        get_client_data = requests.get(endpoint + f"/client/note/notebycustomerid/{customer_id}", headers=headers)

        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter



@pytest.fixture
def get_note_client_history_with_customer_id(define_env):
    '''
    Function to send get request to fetch note of client summary
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        #endpoint = "https://qa-middleware.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        logger.info(customer_id)
        #logger.info(notes_id)
        get_client_data = requests.get(endpoint + f"/case/contact/customer/{customer_id}?hide=hide", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_contact_history_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/case/contact/customer/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_case_action_details(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/masterdata/standardtracking/case", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_client_action_details(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/masterdata/standardtracking/client", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_userdefined_details(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/masterdata/userdefined/field", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter




@pytest.fixture
def get_providers_details(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/providers", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_loard_standard_clientaction_details(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/loadstandard/client", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_standard_caseaction_details(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/standardtracking/case", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_load_standard_caseaction_details(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/loadstandard/case", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter



@pytest.fixture
def post_default_income_category(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(customer_id, income_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing' : "api-automation"
        }
        endpoint = define_env
        payload = common.update_default_income_category(customer_id, income_id)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        response = requests.post(endpoint + "/assystcashflow/income/default", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_default_expense_category(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(customer_id, expense_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_default_expense_category(customer_id, expense_id)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        response = requests.post(endpoint + "/assystcashflow/expense/default", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_default_client_action_category(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(customer_id, tracking_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_default_clientaction_category(customer_id, tracking_id)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        response = requests.post(endpoint + "/client/appointment/default", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def post_default_load_standard_case_action(define_env):
    '''
    Function to send post request to create default case action
    '''
    def _use_fixture_with_parameter(customer_id, case_id, tracking_id, context):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_default_load_standard_case_action(customer_id, case_id, tracking_id, context)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        response = requests.post(endpoint + "/case/business/default", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_default_attituderisk(define_env):
    '''
    Function to send post request to create default attitude risk
    '''
    def _use_fixture_with_parameter(customer_id, category_id, rating_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_default_attituderisk_category(customer_id, category_id, rating_id)
        json_payload = json.loads(payload)
        #logger.info(json_payload)
        response = requests.post(endpoint + "/client/default/attituderisk", json=json_payload, headers=headers)
        #logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_default_objective_category(define_env):
    '''
    Function to send post request to create default income category
    '''
    def _use_fixture_with_parameter(customer_id, objective_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_default_objective_category(customer_id, objective_id)
        json_payload = json.loads(payload)
        #logger.info(json_payload)
        response = requests.post(endpoint + "/client/defaultobjectivecategory", json=json_payload, headers=headers)
        #logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_with_user_id(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint +f"/case/actionlist/user/{user_id}?page=1&dateCondition=allDates&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_review(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint +f"/case/actionlist/user/{user_id}?page=1&dateCondition=allDates&category=client_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_action(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint +f"/case/actionlist/user/{user_id}?page=1&dateCondition=allDates&category=case_tracking_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_review(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint +f"/case/actionlist/user/{user_id}?page=1&dateCondition=allDates&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_action(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint +f"/case/actionlist/user/{user_id}?page=1&dateCondition=allDates&category=client_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_with_empty_user_id(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?allDates=allDates&category=client_action&category=asset_bank&category=asset_home&category=asset_investment&category=asset_shares&category=case_tracking_action&category=client_review&category=credit_review_date&category=loan_review_date&category=mortgage_review_date&category=policy_review_date&page=1&limit=100", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_invalid_bearertoken(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGcUpNZ3NsSkd4SE0xWUN2X003ZEJKeWdFeldfRFE2WkVwamg1Rml1c3RRIn0.eyJleHAiOjE3MTYxOTM2MjYsImlhdCI6MTcxNjE5MDAyNiwianRpIjoiYTMzMTY3ZDktNThjMy00OWI1LWIyNGUtNzZjNmFlZWNiMmI2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWRldi5hc3N5c3QuY2xvdWQvcmVhbG1zL3RlbmFudDItcmVhbG0iLCJhdWQiOiJyZWFsbS1tYW5hZ2VtZW50Iiwic3ViIjoiMzQ0ODUyM2MtY2YwNy00Zjc5LWFmZmQtNTUwY2M2NmY3NjU3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2Rldi5hc3N5c3QuY2xvdWQuczMtd2Vic2l0ZS11cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsImh0dHBzOi8vZGV2LWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwczovL3FhLWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwOi8vcWEuYXNzeXN0LmNsb3VkLnMzLXdlYnNpdGUtdXMtZWFzdC0xLmFtYXpvbmF3cy5jb20iLCJodHRwczovL3FhLW1pZGRsZXdhcmUuYXNzeXN0LmNsb3VkIiwiLyoiLCJodHRwOi8vbG9jYWxob3N0LmFzc3lzdC5jbG91ZDozMDAwIiwiaHR0cDovL2xvY2FsaG9zdDo0MDAwIiwiaHR0cHM6Ly9kZXYtbWlkZGxld2FyZS5hc3N5c3QuY2xvdWQiLCJodHRwczovL2Rldi5hc3N5c3QuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImFsbG93LWNyZWF0ZS11c2VyIiwiYWxsb3ctdXBkYXRlLW1hc3Rlci1kYXRhIiwiYWxsb3ctcmVhc3NpZ24tYWN0aW9ucyIsImFsbG93LXJlc3RyaWN0ZWQtY2xpZW50IiwiYWxsb3ctY2xpZW50LWV4cG9ydHMiLCJhbGxvdy12aWV3LWNsaWVudCIsImFsbG93LWNsaWVudC1yZXBvcnRzIiwiYWxsb3ctdXBkYXRlLWNsaWVudCIsImxpbWl0LWNsaWVudHMtZm9yLXVzZXIiLCJ2aWV3LWFsbC1jbGllbnQiLCJhbGxvdy1kZWxldGUtdXNlciIsImFsbG93LWJ1c2luZXNzLXJlcG9ydHMiLCJhbGxvdy1hZGQtY2xpZW50IiwiYWxsb3ctZGVsZXRlLWNsaWVudCIsImFsbG93LWFkZC11c2VyIiwiYWxsb3ctdmlldy11c2VyIiwiYWxsb3ctY2xpZW50LXVwbG9hZHMiLCJhbGxvdy11cGRhdGUtdXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1yZWFsbSIsInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfSwiY2xpZW50Ijp7InJvbGVzIjpbImFsbG93LWFkZC1jbGllbnQiLCJhbGxvdy12aWV3LWNsaWVudCJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsInNjaGVtYSI6InRlbmFudDIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkFtYXIgVHZtIiwicmVhbG0iOiJ0ZW5hbnQyLXJlYWxtIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYW1hcnR2bUB0ZWtrbm9sb2d5LmNvbSIsImdpdmVuX25hbWUiOiJBbWFyIiwiZmFtaWx5X25hbWUiOiJUdm0iLCJlbWFpbCI6ImFtYXJ0dm1AdGVra25vbG9neS5jb20ifQ.EJHQEAeyWtKLY6q_2OVsfj-tukoROQrIKvgXN8mIDiPyMXb6roPGND_ML_IDw7LRu7dJybcaYTevHUlh6ty-eTSQ5Q89Sh7qVYIJWRh90qvsH1O-Oh-AWB5jPla9VBBSZ-QauW7nbPgWvkBnzgA5fuiDTGgmAgwyRZs4SHGNdkz8nSK6VP2XgbwYp-k8g3r-tYbY78Qn2IEz7X-DlSvfU7BYOT2D3GdP7oyr9J8XOEBQz6QqBuFOuG_HeIpSbuTdjtEci1D68EpCWnD295l-w0C9vwjtoRkUA3qmh34snNO_2QqGm1syJO_pQ-VjF5-jMyUSOE03ZJJjew-qYJ9FFQ"}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?allDates=allDates&category=client_action&category=asset_bank&category=asset_home&category=asset_investment&category=asset_shares&category=case_tracking_action&category=client_review&category=credit_review_date&category=loan_review_date&category=mortgage_review_date&category=policy_review_date&page=1&limit=100", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter




@pytest.fixture
def get_actionlist_with_user_id_definedates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=defineDates&start_date=2020-01-01T00:00:00.000Z&end_date=2024-12-31T00:00:00.000Z&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_review_definedates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=defineDates&start_date=2023-01-01T00:00:00.000Z&end_date=2024-12-31T00:00:00.000Z&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,asset_bank_review,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_action_definedates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=defineDates&start_date=2023-01-01T00:00:00.000Z&end_date=2024-12-31T00:00:00.000Z&category=client_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_action_definedates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=defineDates&start_date=2023-01-01T00:00:00.000Z&end_date=2024-12-31T00:00:00.000Z&category=case_tracking_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_client_review_definedates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=defineDates&start_date=2023-01-01T00:00:00.000Z&end_date=2024-12-31T00:00:00.000Z&category=client_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def test_fetch_actionlist_case_review_define_date(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token_action()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=defineDates&start_date=2024-07-08T00:00:00.000Z&end_date=2024-12-31T00:00:00.000Z&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,asset_bank_review,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_user_id_definedates_empty_userid(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(
            endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=defineDates&start_date=2024-07-08T00:00:00.000Z&end_date=2024-12-31T00:00:00.000Z&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",
            headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_with_user_id_definedates_invalid_bearertoken(define_env):


    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGcUpNZ3NsSkd4SE0xWUN2X003ZEJKeWdFeldfRFE2WkVwamg1Rml1c3RRIn0.eyJleHAiOjE3MTYxOTM2MjYsImlhdCI6MTcxNjE5MDAyNiwianRpIjoiYTMzMTY3ZDktNThjMy00OWI1LWIyNGUtNzZjNmFlZWNiMmI2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWRldi5hc3N5c3QuY2xvdWQvcmVhbG1zL3RlbmFudDItcmVhbG0iLCJhdWQiOiJyZWFsbS1tYW5hZ2VtZW50Iiwic3ViIjoiMzQ0ODUyM2MtY2YwNy00Zjc5LWFmZmQtNTUwY2M2NmY3NjU3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2Rldi5hc3N5c3QuY2xvdWQuczMtd2Vic2l0ZS11cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsImh0dHBzOi8vZGV2LWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwczovL3FhLWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwOi8vcWEuYXNzeXN0LmNsb3VkLnMzLXdlYnNpdGUtdXMtZWFzdC0xLmFtYXpvbmF3cy5jb20iLCJodHRwczovL3FhLW1pZGRsZXdhcmUuYXNzeXN0LmNsb3VkIiwiLyoiLCJodHRwOi8vbG9jYWxob3N0LmFzc3lzdC5jbG91ZDozMDAwIiwiaHR0cDovL2xvY2FsaG9zdDo0MDAwIiwiaHR0cHM6Ly9kZXYtbWlkZGxld2FyZS5hc3N5c3QuY2xvdWQiLCJodHRwczovL2Rldi5hc3N5c3QuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImFsbG93LWNyZWF0ZS11c2VyIiwiYWxsb3ctdXBkYXRlLW1hc3Rlci1kYXRhIiwiYWxsb3ctcmVhc3NpZ24tYWN0aW9ucyIsImFsbG93LXJlc3RyaWN0ZWQtY2xpZW50IiwiYWxsb3ctY2xpZW50LWV4cG9ydHMiLCJhbGxvdy12aWV3LWNsaWVudCIsImFsbG93LWNsaWVudC1yZXBvcnRzIiwiYWxsb3ctdXBkYXRlLWNsaWVudCIsImxpbWl0LWNsaWVudHMtZm9yLXVzZXIiLCJ2aWV3LWFsbC1jbGllbnQiLCJhbGxvdy1kZWxldGUtdXNlciIsImFsbG93LWJ1c2luZXNzLXJlcG9ydHMiLCJhbGxvdy1hZGQtY2xpZW50IiwiYWxsb3ctZGVsZXRlLWNsaWVudCIsImFsbG93LWFkZC11c2VyIiwiYWxsb3ctdmlldy11c2VyIiwiYWxsb3ctY2xpZW50LXVwbG9hZHMiLCJhbGxvdy11cGRhdGUtdXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1yZWFsbSIsInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfSwiY2xpZW50Ijp7InJvbGVzIjpbImFsbG93LWFkZC1jbGllbnQiLCJhbGxvdy12aWV3LWNsaWVudCJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsInNjaGVtYSI6InRlbmFudDIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkFtYXIgVHZtIiwicmVhbG0iOiJ0ZW5hbnQyLXJlYWxtIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYW1hcnR2bUB0ZWtrbm9sb2d5LmNvbSIsImdpdmVuX25hbWUiOiJBbWFyIiwiZmFtaWx5X25hbWUiOiJUdm0iLCJlbWFpbCI6ImFtYXJ0dm1AdGVra25vbG9neS5jb20ifQ.EJHQEAeyWtKLY6q_2OVsfj-tukoROQrIKvgXN8mIDiPyMXb6roPGND_ML_IDw7LRu7dJybcaYTevHUlh6ty-eTSQ5Q89Sh7qVYIJWRh90qvsH1O-Oh-AWB5jPla9VBBSZ-QauW7nbPgWvkBnzgA5fuiDTGgmAgwyRZs4SHGNdkz8nSK6VP2XgbwYp-k8g3r-tYbY78Qn2IEz7X-DlSvfU7BYOT2D3GdP7oyr9J8XOEBQz6QqBuFOuG_HeIpSbuTdjtEci1D68EpCWnD295l-w0C9vwjtoRkUA3qmh34snNO_2QqGm1syJO_pQ-VjF5-jMyUSOE03ZJJjew-qYJ9FFQ"}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(
            endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=defineDates&start_date=2024-07-08T00:00:00.000Z&end_date=2024-12-31T00:00:00.000Z&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",
            headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_actionlist_with_user_id_pastdates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=pastDate&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_review_pastdates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=pastDate&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,asset_bank_review,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_action_pastdates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=pastDate&category=client_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_action_pastdates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=pastDate&category=case_tracking_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_all_category_past_date_invalid_user_id(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(
            endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=pastDate&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_review_pastdates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=pastDate&category=client_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_user_id_todaydates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=todayDateOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_all_category_today_date_invalid_user_id(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=todayDateOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter
@pytest.fixture
def get_actionlist_case_review_todaydates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=todayDateOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,asset_bank_review,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_review_todaydates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=todayDateOverdue&category=client_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_action_todaydates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=todayDateOverdue&category=case_tracking_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_action_todaydates(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=todayDateOverdue&category=client_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_user_id_next_7_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next7DaysOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",
            headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_action_next_7_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next7DaysOverdue&category=case_tracking_action&consultant=&assignee=",
            headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_action_next_7_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next7DaysOverdue&category=client_action&consultant=&assignee=",headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_review_next_7_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next7DaysOverdue&category=client_review&consultant=&assignee=",
            headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_review_next_7_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next7DaysOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,asset_bank_review,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",
            headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_with_user_id_next_7_days_overdue_empty_userid(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(
            endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next7DaysOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",
            headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_user_id_next_7_days_overdue_invalid_token(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGcUpNZ3NsSkd4SE0xWUN2X003ZEJKeWdFeldfRFE2WkVwamg1Rml1c3RRIn0"}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(
            endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next7DaysOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",
            headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_user_id_next_31_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next31DaysOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_action_next_31_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next31DaysOverdue&category=client_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_action_next_31_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next31DaysOverdue&category=case_tracking_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_case_review_next_31_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next31DaysOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,asset_bank_review,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_client_review_next_31_days_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next31DaysOverdue&category=client_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_with_user_id_next_31_days_overdue_empty_user_id(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(
            endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next31DaysOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",
            headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_user_id_next_31_days_overdue_invalid_token(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGcUpNZ3NsSkd4SE0xWUN2X003ZEJKeWdFeldfRFE2WkVwamg1Rml1c3RRIn0.eyJleHAiOjE3MTYxOTM2MjYsImlhdCI6MTcxNjE5MDAyNiwianRpIjoiYTMzMTY3ZDktNThjMy00OWI1LWIyNGUtNzZjNmFlZWNiMmI2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWRldi5hc3N5c3QuY2xvdWQvcmVhbG1zL3RlbmFudDItcmVhbG0iLCJhdWQiOiJyZWFsbS1tYW5hZ2VtZW50Iiwic3ViIjoiMzQ0ODUyM2MtY2YwNy00Zjc5LWFmZmQtNTUwY2M2NmY3NjU3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2Rldi5hc3N5c3QuY2xvdWQuczMtd2Vic2l0ZS11cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsImh0dHBzOi8vZGV2LWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwczovL3FhLWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwOi8vcWEuYXNzeXN0LmNsb3VkLnMzLXdlYnNpdGUtdXMtZWFzdC0xLmFtYXpvbmF3cy5jb20iLCJodHRwczovL3FhLW1pZGRsZXdhcmUuYXNzeXN0LmNsb3VkIiwiLyoiLCJodHRwOi8vbG9jYWxob3N0LmFzc3lzdC5jbG91ZDozMDAwIiwiaHR0cDovL2xvY2FsaG9zdDo0MDAwIiwiaHR0cHM6Ly9kZXYtbWlkZGxld2FyZS5hc3N5c3QuY2xvdWQiLCJodHRwczovL2Rldi5hc3N5c3QuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImFsbG93LWNyZWF0ZS11c2VyIiwiYWxsb3ctdXBkYXRlLW1hc3Rlci1kYXRhIiwiYWxsb3ctcmVhc3NpZ24tYWN0aW9ucyIsImFsbG93LXJlc3RyaWN0ZWQtY2xpZW50IiwiYWxsb3ctY2xpZW50LWV4cG9ydHMiLCJhbGxvdy12aWV3LWNsaWVudCIsImFsbG93LWNsaWVudC1yZXBvcnRzIiwiYWxsb3ctdXBkYXRlLWNsaWVudCIsImxpbWl0LWNsaWVudHMtZm9yLXVzZXIiLCJ2aWV3LWFsbC1jbGllbnQiLCJhbGxvdy1kZWxldGUtdXNlciIsImFsbG93LWJ1c2luZXNzLXJlcG9ydHMiLCJhbGxvdy1hZGQtY2xpZW50IiwiYWxsb3ctZGVsZXRlLWNsaWVudCIsImFsbG93LWFkZC11c2VyIiwiYWxsb3ctdmlldy11c2VyIiwiYWxsb3ctY2xpZW50LXVwbG9hZHMiLCJhbGxvdy11cGRhdGUtdXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1yZWFsbSIsInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfSwiY2xpZW50Ijp7InJvbGVzIjpbImFsbG93LWFkZC1jbGllbnQiLCJhbGxvdy12aWV3LWNsaWVudCJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6ImM1Yzc0ZjRjLTMyMTgtNDg5ZS04MDFmLThhMjczYzM0YmU4ZCIsInNjaGVtYSI6InRlbmFudDIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkFtYXIgVHZtIiwicmVhbG0iOiJ0ZW5hbnQyLXJlYWxtIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYW1hcnR2bUB0ZWtrbm9sb2d5LmNvbSIsImdpdmVuX25hbWUiOiJBbWFyIiwiZmFtaWx5X25hbWUiOiJUdm0iLCJlbWFpbCI6ImFtYXJ0dm1AdGVra25vbG9neS5jb20ifQ.EJHQEAeyWtKLY6q_2OVsfj-tukoROQrIKvgXN8mIDiPyMXb6roPGND_ML_IDw7LRu7dJybcaYTevHUlh6ty-eTSQ5Q89Sh7qVYIJWRh90qvsH1O-Oh-AWB5jPla9VBBSZ-QauW7nbPgWvkBnzgA5fuiDTGgmAgwyRZs4SHGNdkz8nSK6VP2XgbwYp-k8g3r-tYbY78Qn2IEz7X-DlSvfU7BYOT2D3GdP7oyr9J8XOEBQz6QqBuFOuG_HeIpSbuTdjtEci1D68EpCWnD295l-w0C9vwjtoRkUA3qmh34snNO_2QqGm1syJO_pQ-VjF5-jMyUSOE03ZJJjew-qYJ9FFQ"}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(
            endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=next31DaysOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=",
            headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_user_id_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_all_category_thisyear_date_invalid_user_id(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter
@pytest.fixture
def get_actionlist_with_case_review_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category==asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,asset_bank_review,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_client_review_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=client_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter
@pytest.fixture
def get_actionlist_with_case_action_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=case_tracking_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_client_action_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=client_action&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def gget_actionlist_all_category_thisyear_date_invalid_user_id(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token_action()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=&assignee=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_only_assignee_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&assignee=sundaram", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_invalid_assignee_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&assignee=Brian King", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_with_only_consultant_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=Amar Tvm", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_with_invalid_consultant_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&consultant=sundaram033", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_actionlist_with_only_search_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&search=api client", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_invalid_search_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&search=leena", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_actionlist_with_all_search_this_year_overdue(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter(user_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/actionlist/user/{user_id}?page=1&dateCondition=thisYearOverdue&category=asset_home_review,credit_review_date,mortgage_review_date,loan_review_date,policy_review_date,client_review,client_action,asset_bank_review,case_tracking_action,asset_investment_review,asset_shares_review,asset_bank_review&search=api client&assignee=Amar tvm&consultant=Amar Tvm", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_search_client(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter(first_name,last_name):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        # get_client_api = requests.get(endpoint + f"/client?limit=10&page=1&search={first_name}{last_name}", headers=headers)
        if first_name == 'STRINGG' and last_name == 'STRINGG':
            get_client_api = requests.get(endpoint + f"/client?limit=10&page=1&search={first_name}%20%20{last_name}",
                                     headers=headers)
        elif first_name == 'STRINGG,' and last_name == 'STRINGG':
            get_client_api = requests.get(endpoint + f"/client?limit=10&page=1&search={first_name},{last_name}",
                                    headers=headers)
        elif first_name == 'xyz' and last_name == 'klm':
            get_client_api = requests.get(endpoint + f"/client?limit=10&page=1&search={first_name}{last_name}",
                                    headers=headers)
        elif first_name == 'STRINGG' and last_name == 'STRINGG':
            get_client_api = requests.get(endpoint + f"/client?limit=10&page=1&search={first_name}{last_name}",
                                    headers=headers)

        else:
            logger.error("Context Not Implemented")
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_search_client_userid(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/user/user-info", headers=headers)



        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_clientaction_data(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''
    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env

        if file == True and not isinstance(data, dict):
            json_file = open(data)
            payload = json.load(json_file)

        elif (file == 'e2e' or isinstance(data, dict)) and context in data:
            data = data[context]
            data["customer_id"] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
        else:
            json_payload = {}
            json_payload.update(({context: data}))
            payload = json.dumps(json_payload)
            payload = json.loads(payload)
            logger.info(payload)
        file_path = './jsons/create_client_contexts.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(payload, expected_data_types, context)
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter



@pytest.fixture
def post_user_data(define_env):
    '''
    Function to send post request to add all data to system manager
    '''
    def _use_fixture_with_parameter(customer_id,datas, file):
        payload = None
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing'  : "api-automation"
        }
        endpoint = define_env
        payload = common.update_manage_user_read_json(customer_id,datas)
        payloads = json.loads(payload)
        logger.info(payloads)
        if file == True:
            pass

        response = requests.post(endpoint + "/user", json=payloads,
                                     headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_user_data_user_5(define_env):
    '''
    Function to send post request to add all data to system manager
    '''
    def _use_fixture_with_parameter(customer_id,datas, file):
        payload = None
        bearer_token = get_bearer_token_user_5()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing'  : "api-automation"
        }
        endpoint = define_env
        payload = common.update_manage_user_read_json(customer_id,datas)
        payloads = json.loads(payload)
        logger.info(payloads)
        if file == True:
            pass

        response = requests.post(endpoint + "/user", json=payloads,
                                     headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_user_data_for_business_assigned(define_env):
    '''
    Function to send post request to add all data to system manager
    '''
    def _use_fixture_with_parameter(customer_id,datas, file):
        payload = None
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing'  : "api-automation"
        }
        endpoint = define_env
        payload = common.update_manage_user_business_read_json(customer_id,datas)
        payloads = json.loads(payload)
        if file == True:
            pass

        response = requests.post(endpoint + "/user", json=payloads,
                                     headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def create_client_for_superadmin(define_env):
    '''
    Function to send post request to create a client
    '''
    def _use_fixture_with_parameter(data, context, file):
        bearer_token = get_bearer_token_superadmin()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing' : "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-middleware.assyst.cloud"
        if file == True:
            json_file = open(data)
            payload = json.load(json_file)
        elif file == 'e2e':
            data = data[context]
            payload = {}
            payload.update(({context: data}))
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

# @pytest.fixture
# def create_client_for_superadmin(define_env):
#     '''
#     Function to send post request to create a client
#     '''
#     def _use_fixture_with_parameter(data, context, file):
#         bearer_token = get_bearer_token_superadmin()
#         headers = {
#             'Authorization': f'Bearer {bearer_token}',
#             'Testing' : "api-automation"
#         }
#         endpoint = define_env
#         # endpoint = "https://qa-middleware.assyst.cloud"
#         if file == True:
#             json_file = open(data)
#             payload = json.load(json_file)
#         elif file == 'e2e':
#             data = data[context]
#             payload = {}
#             payload.update(({context: data}))
#         else:
#             json_data = json.dumps(data)
#             json_payload = json.loads(json_data)
#             payload = {}
#             payload.update(({context: json_payload}))
#         response = requests.post(endpoint + "/client", json=payload, headers=headers)
#         status_code_check(response.status_code)
#         if status_code_check:
#             return response
#         else:
#             return False, response.json()
#     return _use_fixture_with_parameter
#
#




@pytest.fixture
def create_client_for_user_2(define_env):
    '''
    Function to send post request to create a client
    '''

    def _use_fixture_with_parameter(data, context, file):
        bearer_token = get_bearer_token_user_2()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-middleware.assyst.cloud"
        if file == True:
            json_file = open(data)
            payload = json.load(json_file)
        elif file == 'e2e':
            data = data[context]
            payload = {}
            payload.update(({context: data}))
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check1(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def post_outgoing_data_user_2(define_env):
    '''
    Function to send post request to add all data to expense
    '''

    def _use_fixture_with_parameter(customer_id, data, context, file):
        bearer_token = get_bearer_token_user_2()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        payload = common.update_outgoing_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j
        file_path = './jsons/create_new_outgoing.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        logger.info(json_payload)
        response = requests.post(endpoint + "/assystcashflow/expense", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def patch_outgoing_data_user_2(define_env):
    '''
    Function to send post request to add all data to expense
    '''

    def _use_fixture_with_parameter(customer_id, expense_id, data, context, file):
        bearer_token = get_bearer_token_user_2()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        payload = common.update_outgoing_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j
        file_path = './jsons/create_new_outgoing.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.patch(endpoint + f"/assystcashflow/expense/{expense_id}", json=json_payload,
                                  headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_all_user_details(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/user", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_keycloak_user_details(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + "/user/auth", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_keycloak_user_details_invalid_url(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + "/user/au", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter



@pytest.fixture
def get_keycloak_user_details_invalid_bearer_token(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGcUpNZ3NsSkd4SE0xWUN2X003ZEJKeWdFeldfRFE2WkVwamg1Rml1c3RRIn0.eyJleHAiOjE3MTIyMzAzODUsImlhdCI6MTcxMjIyNjc4NSwianRpIjoiZTc1OTE4YmEtYjVmZS00YmFlLTg0YzMtZTA2YmQ2ZDE0Y2U2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWRldi5hc3N5c3QuY2xvdWQvcmVhbG1zL3RlbmFudDItcmVhbG0iLCJhdWQiOiJyZWFsbS1tYW5hZ2VtZW50Iiwic3ViIjoiMzQ0ODUyM2MtY2YwNy00Zjc5LWFmZmQtNTUwY2M2NmY3NjU3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6ImM3NWMyY2ExLTA0YTAtNDI5OC05NmE5LWVhZGFiODQxYWEwMyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2Rldi5hc3N5c3QuY2xvdWQuczMtd2Vic2l0ZS11cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsImh0dHA6Ly9xYS5hc3N5c3QuY2xvdWQuczMtd2Vic2l0ZS11cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsImh0dHBzOi8vcWEtbWlkZGxld2FyZS5hc3N5c3QuY2xvdWQiLCIvKiIsImh0dHA6Ly9sb2NhbGhvc3QuYXNzeXN0LmNsb3VkOjMwMDAiLCJodHRwOi8vbG9jYWxob3N0OjMwMDAiLCJodHRwczovL2Rldi1taWRkbGV3YXJlLmFzc3lzdC5jbG91ZCIsImh0dHBzOi8vZGV2LmFzc3lzdC5jbG91ZCJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiYWxsb3ctY3JlYXRlLXVzZXIiLCJhbGxvdy11cGRhdGUtbWFzdGVyLWRhdGEiLCJhbGxvdy1yZWFzc2lnbi1hY3Rpb25zIiwiYWxsb3ctY2xpZW50LWV4cG9ydHMiLCJhbGxvdy12aWV3LWNsaWVudCIsImFsbG93LWNsaWVudC1yZXBvcnRzIiwiYWxsb3ctdXBkYXRlLWNsaWVudCIsImxpbWl0LWNsaWVudHMtZm9yLXVzZXIiLCJ2aWV3LWFsbC1jbGllbnQiLCJhbGxvdy1kZWxldGUtdXNlciIsImFsbG93LWJ1c2luZXNzLXJlcG9ydHMiLCJhbGxvdy1hZGQtY2xpZW50IiwiYWxsb3ctZGVsZXRlLWNsaWVudCIsImFsbG93LWFkZC11c2VyIiwiYWxsb3ctdmlldy11c2VyIiwiYWxsb3ctY2xpZW50LXVwbG9hZHMiLCJhbGxvdy11cGRhdGUtdXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7InJlYWxtLW1hbmFnZW1lbnQiOnsicm9sZXMiOlsidmlldy1yZWFsbSIsInZpZXctaWRlbnRpdHktcHJvdmlkZXJzIiwibWFuYWdlLWlkZW50aXR5LXByb3ZpZGVycyIsImltcGVyc29uYXRpb24iLCJyZWFsbS1hZG1pbiIsImNyZWF0ZS1jbGllbnQiLCJtYW5hZ2UtdXNlcnMiLCJxdWVyeS1yZWFsbXMiLCJ2aWV3LWF1dGhvcml6YXRpb24iLCJxdWVyeS1jbGllbnRzIiwicXVlcnktdXNlcnMiLCJtYW5hZ2UtZXZlbnRzIiwibWFuYWdlLXJlYWxtIiwidmlldy1ldmVudHMiLCJ2aWV3LXVzZXJzIiwidmlldy1jbGllbnRzIiwibWFuYWdlLWF1dGhvcml6YXRpb24iLCJtYW5hZ2UtY2xpZW50cyIsInF1ZXJ5LWdyb3VwcyJdfX0sInNjb3BlIjoiZW1haWwgcHJvZmlsZSIsInNpZCI6ImM3NWMyY2ExLTA0YTAtNDI5OC05NmE5LWVhZGFiODQxYWEwMyIsInNjaGVtYSI6InRlbmFudDIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmFtZSI6IkFtYXIgVHZtIiwicmVhbG0iOiJ0ZW5hbnQyLXJlYWxtIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYW1hcnR2bUB0ZWtrbm9sb2d5LmNvbSIsImdpdmVuX25hbWUiOiJBbWFyIiwiZmFtaWx5X25hbWUiOiJUdm0iLCJlbWFpbCI6ImFtYXJ0dm1AdGVra25vbG9neS5jb20ifQ.rb7NOzaGXJm8jPxjeUUG-EiGJYUIqET8GC504mro5XSXJkPqDkLMeAxbah0vaFOMazL9UeSOw_xmlxnKau4kWhv9oY_dfVf07pnTeppZ4o8vMDvCo0OxwJ1bs6dgD4T1BRFaq9JrI4PgU0OTXQuVbD9_qgz1lvQlkfEu75-a4RoJ5yiUVrU4Esk_ant082JORQ5MKNPZfUTBN0_M8ndIyqQWt-tsHb3f8Ve5fEOrSlh2-bikM2lzfjj4t_XfcGsE8wCWQOxT8LUG__WAJQdVhnVIw5-cgYdnWa7ocVWpEm7IoioNyuF8GMWijkHD9NI2rdFEG9T-M46rPVsLWQXYSg"}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + "/user/auth", headers=headers)
        status_code_check1(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter




@pytest.fixture
def get_all_user_details_user_4(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token_user_4()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/user", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_all_user_details_user_5(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token_user_5()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/user", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_all_user_details_user_6(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token_user_6()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/user", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_role_details(define_env):
    '''
    Function to send get request to fetch contact history data without hide
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/user/auth/roles", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_liability_data_user_2(define_env):
    '''
    Function to send post request to add data to liability
    '''

    def _use_fixture_with_parameter(customer_id,provider_id, data, context, file):
        bearer_token = get_bearer_token_user_2()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_liability_json_data(customer_id,provider_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            data['provider_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j
        file_path = './jsons/create_new_liability.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.post(endpoint + "/case/liability", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/liability", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def patch_liability_data_user_2(define_env):
    '''
    Function to send patch request to update data to liability
    '''

    def _use_fixture_with_parameter(customer_id,provider_id, liability_id, data, context, file):
        bearer_token = get_bearer_token_user_2()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_liability_json_data(customer_id,provider_id, context)
        json_payload = json.loads(payload)
        if file == True:
            pass
        elif file == 'e2e':
            data = data[context]
            data['customer_id'] = customer_id
            data['provider_id'] = customer_id
            json_payload = {}
            json_payload.update(({context: data}))
        else:
            for i, j in data.items():
                json_payload[context][i] = j
        file_path = './jsons/create_new_liability.json'
        expected_data_types = common.read_json(file_path)
        common.convert_data_types(json_payload, expected_data_types, context)
        response = requests.patch(endpoint + f"/case/liability/{liability_id}", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/liability", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter

@pytest.fixture
def get_client_details_superadmin(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token_superadmin()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/client", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_client_details_user_2(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token_user_2()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/client", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter
@pytest.fixture
def get_client_details_user_3(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token_user_3()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/client", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def create_client_for_user_3(define_env):
    '''
    Function to send post request to create a client
    '''
    def _use_fixture_with_parameter(data, context, file):
        bearer_token = get_bearer_token_user_3()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing' : "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-middleware.assyst.cloud"
        if file == True:
            json_file = open(data)
            payload = json.load(json_file)
        elif file == 'e2e':
            data = data[context]
            payload = {}
            payload.update(({context: data}))
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check1(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_user_info(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env#"https://qa-middleware.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/user/user-info", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_address_phone_report(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env#"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/report?formatType=pdf&context=address-phone&limit=10", headers=headers)
        #logger.info(get_client_api)
        status_code_check(get_client_api.status_code)
        if status_code_check:
             if get_client_api.status_code == 200:
                 # Assuming the response content is the PDF file itself
                 with open("./Report_pdf/address_phone.pdf", "wb") as f:
                     f.write(get_client_api.content)
                 logger.info("PDF report downloaded successfully.")
             else:
                 logger.info("Failed to download PDF report. Status code:", get_client_api.status_code)
             return get_client_api

    return _use_fixture_with_parameter


@pytest.fixture
def get_address_phone_report_invalid_context(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env#"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/report?formatType=pdf&context=&limit=10", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_address_phone_report_invalid_limit(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter():
        endpoint =define_env# "https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/report?formatType=pdf&context=address-phone&limit=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def create_client_test(define_env):
    '''
    Function to send post request to create a client
    '''
    def _use_fixture_with_parameter(data, context, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJGcUpNZ3NsSkd4SE0xWUN2X003ZEJKeWdFeldfRFE2WkVwamg1Rml1c3RRIn0.eyJleHAiOjE3MTI1NjU5OTcsImlhdCI6MTcxMjU2MjM5NywianRpIjoiZmI4ZDJkNDctZGU0ZS00NGJlLThlM2EtMmJkYmY0MGJhZWI1IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWRldi5hc3N5c3QuY2xvdWQvcmVhbG1zL3RlbmFudDItcmVhbG0iLCJhdWQiOiJyZWFsbS1tYW5hZ2VtZW50Iiwic3ViIjoiMzQ0ODUyM2MtY2YwNy00Zjc5LWFmZmQtNTUwY2M2NmY3NjU3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY2xpZW50Iiwic2Vzc2lvbl9zdGF0ZSI6IjNiZjQ5MWQ4LWEzODQtNDJmYi05MzYyLWVlNTc5MGM1MDEzNyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2Rldi5hc3N5c3QuY2xvdWQuczMtd2Vic2l0ZS11cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsImh0dHBzOi8vZGV2LWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwczovL3FhLWFwcC5hc3N5c3QuY2xvdWQiLCJodHRwOi8vcWEuYXNzeXN0LmNsb3VkLnMzLXdlYnNpdGUtdXMtZWFzdC0xLmFtYXpvbmF3cy5jb20iLCJodHRwczovL3FhLW1pZGRsZXdhcmUuYXNzeXN0LmNsb3VkIiwiLyoiLCJodHRwOi8vbG9jYWxob3N0LmFzc3lzdC5jbG91ZDozMDAwIiwiaHR0cDovL2xvY2FsaG9zdDozMDAwIiwiaHR0cHM6Ly9kZXYtbWlkZGxld2FyZS5hc3N5c3QuY2xvdWQiLCJodHRwczovL2Rldi5hc3N5c3QuY2xvdWQiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImFsbG93LWNyZWF0ZS11c2VyIiwiYWxsb3ctdXBkYXRlLW1hc3Rlci1kYXRhIiwiYWxsb3ctcmVhc3NpZ24tYWN0aW9ucyIsImFsbG93LWNsaWVudC1leHBvcnRzIiwiYWxsb3ctdmlldy1jbGllbnQiLCJhbGxvdy1jbGllbnQtcmVwb3J0cyIsImFsbG93LXVwZGF0ZS1jbGllbnQiLCJsaW1pdC1jbGllbnRzLWZvci11c2VyIiwidmlldy1hbGwtY2xpZW50IiwiYWxsb3ctZGVsZXRlLXVzZXIiLCJhbGxvdy1idXNpbmVzcy1yZXBvcnRzIiwiYWxsb3ctYWRkLWNsaWVudCIsImFsbG93LWRlbGV0ZS1jbGllbnQiLCJhbGxvdy1hZGQtdXNlciIsImFsbG93LXZpZXctdXNlciIsImFsbG93LWNsaWVudC11cGxvYWRzIiwiYWxsb3ctdXBkYXRlLXVzZXIiXX0sInJlc291cmNlX2FjY2VzcyI6eyJyZWFsbS1tYW5hZ2VtZW50Ijp7InJvbGVzIjpbInZpZXctcmVhbG0iLCJ2aWV3LWlkZW50aXR5LXByb3ZpZGVycyIsIm1hbmFnZS1pZGVudGl0eS1wcm92aWRlcnMiLCJpbXBlcnNvbmF0aW9uIiwicmVhbG0tYWRtaW4iLCJjcmVhdGUtY2xpZW50IiwibWFuYWdlLXVzZXJzIiwicXVlcnktcmVhbG1zIiwidmlldy1hdXRob3JpemF0aW9uIiwicXVlcnktY2xpZW50cyIsInF1ZXJ5LXVzZXJzIiwibWFuYWdlLWV2ZW50cyIsIm1hbmFnZS1yZWFsbSIsInZpZXctZXZlbnRzIiwidmlldy11c2VycyIsInZpZXctY2xpZW50cyIsIm1hbmFnZS1hdXRob3JpemF0aW9uIiwibWFuYWdlLWNsaWVudHMiLCJxdWVyeS1ncm91cHMiXX19LCJzY29wZSI6ImVtYWlsIHByb2ZpbGUiLCJzaWQiOiIzYmY0OTFkOC1hMzg0LTQyZmItOTM2Mi1lZTU3OTBjNTAxMzciLCJzY2hlbWEiOiJ0ZW5hbnQyIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5hbWUiOiJBbWFyIFR2bSIsInJlYWxtIjoidGVuYW50Mi1yZWFsbSIsInByZWZlcnJlZF91c2VybmFtZSI6ImFtYXJ0dm1AdGVra25vbG9neS5jb20iLCJnaXZlbl9uYW1lIjoiQW1hciIsImZhbWlseV9uYW1lIjoiVHZtIiwiZW1haWwiOiJhbWFydHZtQHRla2tub2xvZ3kuY29tIn0.IVBYcrLLieeyrswuHFEsqdFMm0a50K7GlAQnaGm8FJD_ysJNhl8JmjqQWok_QrkC2vMLQcQtCOy2CXs0HJC11YVnrK0bIci6erzTxKX5l0vjX6rqc4hL_sDSRVWIy8gkAzyT28UKCLhjsQjmZVxMQigyjZ9Hx1lH6uZ-v-lId5CNMo1danTn4YwK2cW-PdzJ296Vx8mEHKmYhyC6hFyvi4s6CrTc-YizUJYYNuZHoZH5P4srwVqW6Ci72TcWZeJ25XW-hgwLoC3RpYYDjaQgF1nQXDcLUyuDtb6oI-jo7C99vyXW21mynKu3khhXt8BXorJMLBjtZ1JtioTxdusZ1w"}',
            'Testing' : "api-automation"
        }
        endpoint = define_env
        # endpoint = "https://qa-middleware.assyst.cloud"
        if file == True:
            json_file = open(data)
            payload = json.load(json_file)
        elif file == 'e2e':
            data = data[context]
            payload = {}
            payload.update(({context: data}))
        else:
            json_data = json.dumps(data)
            json_payload = json.loads(json_data)
            payload = {}
            payload.update(({context: json_payload}))
        response = requests.post(endpoint + "/client", json=payload, headers=headers)
        status_code_check1(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_factfind_summary_report(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()

        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint +f"/report/factfind/summary/{customer_id}?formatType=pdf&context=factfind-summary", headers=headers)
        #logger.info(get_client_api.json())
        status_code_check(get_client_api.status_code)
        if status_code_check:
             if get_client_api.status_code == 200:
                 # Assuming the response content is the PDF file itself
                 with open("./Report_pdf/factfind_summary.pdf", "wb") as f:
                     f.write(get_client_api.content)
                 logger.info("PDF report downloaded successfully.")
             else:
                 logger.info("Failed to download PDF report. Status code:", get_client_api.status_code)
             return get_client_api

    return _use_fixture_with_parameter

@pytest.fixture
def get_factfind_standard_report(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env#"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        #logger.info(customer_id)
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint +f"/report/factfind/standard/{customer_id}?formatType=pdf&context=factfind-standard", headers=headers)
        #logger.info(get_client_api.json())
        status_code_check(get_client_api.status_code)
        if status_code_check:
             if get_client_api.status_code == 200:
                 # Assuming the response content is the PDF file itself
                 with open("./Report_pdf/factfind_standard.pdf", "wb") as f:
                     f.write(get_client_api.content)
                 logger.info("PDF report downloaded successfully.")
             else:
                 logger.info("Failed to download PDF report. Status code:", get_client_api.status_code)
             return get_client_api

    return _use_fixture_with_parameter

@pytest.fixture
def get_fact_summary_invalid_context(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env#"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/report/factfind/summary/{customer_id}?formatType=pdf&context=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_fact_summary_empty_custid(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter():
        endpoint =define_env# "https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/report/factfind/summary/?formatType=pdf&context=factfind-summary", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_fact_standard_invalid_context(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env#"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/report/factfind/standard/{customer_id}?formatType=pdf&context=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_fact_standard_invalid_custid(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env#"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/report/factfind/standard/?formatType=pdf&context=factfind-standard", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_fact_summary_invalid_custid(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env#"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/report/factfind/summary/{customer_id}?formatType=pdf&context=", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_portfolio(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        #endpoint = "https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()

        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint +f"/report/portfolio/portrait/{customer_id}?formatType=pdf&context=portfolio-potrait", headers=headers)
        #logger.info(get_client_api.json())
        status_code_check(get_client_api.status_code)
        if status_code_check:
             if get_client_api.status_code == 200:
                 # Assuming the response content is the PDF file itself
                 with open("./Report_pdf/portfolio.pdf", "wb") as f:
                     f.write(get_client_api.content)
                 logger.info("PDF report downloaded successfully.")
             else:
                 logger.info("Failed to download PDF report. Status code:", get_client_api.status_code)
             return get_client_api

    return _use_fixture_with_parameter


@pytest.fixture
def post_networth_portfolio(define_env,request):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id,jointindicator,policyholder,partner_cust_id):
        endpoint = define_env
        #endpoint = "https://qa-middleware.assyst.cloud"
        bearer_token = get_bearer_token()

        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if jointindicator == 0 or policyholder ==0 :
            id=customer_id
        elif jointindicator == 1 or  policyholder == 1:
            id = partner_cust_id
        payload = common.update_portfolionetworth_data(id)
        payload = json.loads(payload)
        logger.info(payload)
        get_client_api = requests.post(endpoint +f"/report/new/global/portfolio-networth", json=payload, headers=headers)

        status_code_check(get_client_api.status_code)
        if status_code_check:
            if get_client_api.status_code == 200 or 201:
                if request.function.__name__ == "test_fetch_portfolio_summary":
                    if jointindicator == 0 or policyholder == 0:
                        file_path = "./Report_pdf/networth_portfolio_client.xlsx"
                    else:
                        file_path = "./Report_pdf/networth_portfolio_partner.xlsx"
                else:
                    file_path = "./Report_pdf/tenant_test_networth_portfolio.xlsx"

                with open(file_path, "wb") as f:
                    f.write(get_client_api.content)
                logger.info("Excel report downloaded successfully.")
            else:
                logger.info("Failed to download PDF report. Status code: %s", get_client_api.status_code)
            return get_client_api

    return _use_fixture_with_parameter
@pytest.fixture
def post_liability_listing(define_env,request):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id,jointindicator,partner_cust_id):
        endpoint = define_env

        bearer_token = get_bearer_token()

        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if jointindicator == 0 :
            id=customer_id
        elif jointindicator == 1:
            id = partner_cust_id
        payload = common.update_portfolionetworth_data(id)
        payload = json.loads(payload)
        logger.info(payload)
        get_client_api = requests.post(endpoint +f"/report/new/global/liability-listing", json=payload, headers=headers)

        status_code_check(get_client_api.status_code)
        if status_code_check:
             if get_client_api.status_code == 200 or 201:
                 if request.function.__name__ == "test_fetch_liability_listing":
                     if jointindicator == 0:
                        file_path = "./Report_pdf/liability_listing_client.xlsx"
                     else:
                         file_path = "./Report_pdf/liability_listing_partner.xlsx"
                 else:
                     file_path = "./Report_pdf/tenant_test_liability_listing.xlsx"



                 with open(file_path, "wb") as f:
                     f.write(get_client_api.content)
                 logger.info("Excel report downloaded successfully.")
             else:
                 logger.info("Failed to download PDF report. Status code: %s", get_client_api.status_code)
             return get_client_api

    return _use_fixture_with_parameter


@pytest.fixture
def post_replacement_register_report(define_env,request):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(policyholder,jointindicator):
        endpoint = define_env

        bearer_token = get_bearer_token()

        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }

        payload = common.update_all_client_report_data()
        payload = json.loads(payload)
        logger.info(payload)
        get_client_api = requests.post(endpoint +f"/report/new/global/ReplacementRegister", json=payload, headers=headers)

        status_code_check(get_client_api.status_code)
        if status_code_check:
             if get_client_api.status_code == 200 or 201:
                 if request.function.__name__ == "test_post_replacement_register":
                     if jointindicator == 0 or policyholder == 0:
                        file_path = "./Report_pdf/replacement_register_client.xlsx"
                     else:
                         file_path = "./Report_pdf/replacement_register_partner.xlsx"
                 else:
                     file_path = "./Report_pdf/tenant_test_replacement_register.xlsx"



                 with open(file_path, "wb") as f:
                     f.write(get_client_api.content)
                 logger.info("Excel report downloaded successfully.")
             else:
                 logger.info("Failed to download PDF report. Status code: %s", get_client_api.status_code)
             return get_client_api

    return _use_fixture_with_parameter



@pytest.fixture
def post_asset_listing(define_env,request):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id,jointindicator,partner_cust_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        if jointindicator == 0 :
            id=customer_id
        elif jointindicator == 1:
            id = partner_cust_id
        payload = common.update_portfolionetworth_data(id)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        response = requests.post(endpoint + f"/report/new/global/asset-listing", json=json_payload, headers=headers)

        status_code_check(response.status_code)
        if status_code_check:
            if response.status_code == 200 or 201:
                if request.function.__name__ == "test_fetch_asset_listing":
                    if jointindicator == 0 :
                        file_path = "./Report_pdf/asset_listing_client.xlsx"
                    else:
                        file_path = "./Report_pdf/asset_listing_partner.xlsx"
                else:
                    file_path = "./Report_pdf/tenant_test_asset_listing.xlsx"

                with open(file_path, "wb") as f:
                    f.write(response.content)
                logger.info("Excel report downloaded successfully.")
            else:
                logger.info("Failed to download PDF report. Status code: %s", response.status_code)
            return response

    return _use_fixture_with_parameter




@pytest.fixture
def post_contact_history(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter():
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_all_client_report_data()
        json_payload = json.loads(payload)
        logger.info(json_payload)

        response = requests.post(endpoint + f"/report/new/global/Contact-History", json=json_payload, headers=headers)

        status_code_check(response.status_code)
        if status_code_check:
             if response.status_code == 200 or 201:
                 # Assuming the response content is the PDF file itself
                 with open("./Report_pdf/contact_history.xlsx", "wb") as f:
                     f.write(response.content)
                 logger.info("Excel report downloaded successfully.")
             else:
                 logger.info("Failed to download Excel report. Status code:", response.status_code)
             return response

    return _use_fixture_with_parameter

@pytest.fixture
def post_addressphone(define_env):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter():
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_all_client_report_data()
        json_payload = json.loads(payload)
        logger.info(json_payload)

        response = requests.post(endpoint + f"/report/new/global/address-phone", json=json_payload, headers=headers)

        status_code_check(response.status_code)
        if status_code_check:
             if response.status_code == 200 or 201:
                 # Assuming the response content is the PDF file itself
                 with open("./Report_pdf/address_and_phone.xlsx", "wb") as f:
                     f.write(response.content)
                 logger.info("Excel report downloaded successfully.")
             else:
                 logger.info("Failed to download Excel report. Status code:", response.status_code)
             return response

    return _use_fixture_with_parameter



@pytest.fixture
def get_portfolio_invalid_context(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env #"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/report/portfolio/portrait/{customer_id}?formatType=pdf&context=", headers=headers)
        logger.info(get_client_api.json())
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_portfolio_invalid_custid(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env #"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/report/portfolio/portrait/?formatType=pdf&context=portfolio-potrait", headers=headers)
        logger.info(get_client_api.json())
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_case_summary_show_noncurrent(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env#"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/case-summary/customer/{customer_id}?show=show", headers=headers)
        logger.info(get_client_api.json())
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_case_summary_hide_noncurrent(define_env):
    '''
    Function to send get request to get user details
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env #"https://qa-api.assyst.cloud"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/case/case-summary/customer/{customer_id}?show=", headers=headers)
        logger.info(get_client_api.json())
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_client_note_data(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''
    def _use_fixture_with_parameter(customer_id,data,file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation",
            'userid': "82b8f31c-81b2-403c-87ff-176129d1b64f"

        }
        endpoint = define_env #"https://qa-api.assyst.cloud/secured/client"
        with open("C:/APITestAutomation/Screenshot.png", "rb") as File:
            file_content = File.read()
            files = {'file': file_content}
        logger.info(data)
        payload = common.update_notes_json_data(customer_id)
        #logger.info(payload)
        json_payload = json.loads(payload)
        if file == True:
           pass
        else:
            for i, j in data.items():
                json_payload[i] = j

        response = requests.post(endpoint+"/client/notes", data=json_payload, files=files, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def post_client_fact_note_data(define_env):
    '''
    Function to send post request to create different contexts for a client
    '''
    def _use_fixture_with_parameter(customer_id,data,file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation",
            'userid' : "8cfdb397-f8b4-4052-ab62-880b533988cb"

        }
        endpoint = define_env #"https://qa-api.assyst.cloud/secured/client"
        with open("C:/APITestAutomation/Screenshot.png", "rb") as File:
            file_content = File.read()
            files = {'file': file_content}
        logger.info(data)
        payload = common.update_fact_find_notes_json_data(customer_id)
        logger.info(payload)
        #logger.info(files)
        json_payload = json.loads(payload)
        if file == True:
           pass
        else:
            for i, j in data.items():
                json_payload[i] = j

        response = requests.post(endpoint+"/client/notes", data=json_payload, files=files, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter


@pytest.fixture
def post_userdefined_value(define_env):
    '''
    Function to send post request to create default attitude risk
    '''
    def _use_fixture_with_parameter(customer_id, category_id ,context):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_userdefined_value(customer_id, category_id,context)
        json_payload = json.loads(payload)

        response = requests.post(endpoint + "/client/userdefined/bulkinsert/value", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def post_userdefined_invalid_customer_id(define_env):
    '''
    Function to send post request to create default attitude risk
    '''
    def _use_fixture_with_parameter(customer_id, category_id ,context):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.update_userdefined_value(customer_id, category_id,context)
        json_payload = json.loads(payload)

        response = requests.post(endpoint + "/client/userdefined/bulkinsert/value", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_provider_casesummary_data_with_provider_id(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter(provider_correspondence_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/masterdata/providers/{provider_correspondence_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_userdefined_value_data_with_customer_id(define_env):
    '''
    Function to send get request to fetch contact note data using customer id
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env  # "https://qa-middleware.assyst.cloud"
        # endpoint = "https://qa-api.assyst.cloud/asc/api/v1.0"
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_data = requests.get(endpoint + f"/client/userdefined/value/{customer_id}", headers=headers)
        status_code_check(get_client_data.status_code)
        if status_code_check:
            return get_client_data
        else:
            return False, get_client_data.json()

    return _use_fixture_with_parameter


@pytest.fixture
def patch_user_defined_value_data(define_env):
    '''
    Function to send post request to add all data to expense
    '''
    def _use_fixture_with_parameter(customer_id,value_id, category_id ,context):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        payload = common.patch_userdefined_value(value_id, category_id, context)
        logger.info(category_id)
        json_payload = json.loads(payload)

        response = requests.patch(endpoint + f"/client/userdefined/bulkupdate/value/{customer_id}", json=json_payload, headers=headers)
        logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()

    return _use_fixture_with_parameter



@pytest.fixture
def get_commission_rule(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/commission/commissionrule", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter


@pytest.fixture
def get_attitude_with_partner_customer_id(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter(customer_id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + f"/client/attituderisk/customer/{customer_id}", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter

@pytest.fixture
def get_objective_category(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/objective/category", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter


@pytest.fixture
def get_invalid_context_commission_rule(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/masterdata/commission/commissionr", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter


@pytest.fixture
def post_policy_payment_withdrawal(define_env,request):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id,policyholder,partner_cust_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        if policyholder == 0 :
            id=customer_id
        elif policyholder == 1:
            id = partner_cust_id
        payload = common.update_portfolionetworth_data(id)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        response = requests.post(endpoint + f"/report/new/global/policy-payment-withdrawal", json=json_payload, headers=headers)
        #logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
             if response.status_code == 200 or 201:
                 if request.function.__name__ == "test_add_policy_payment_withdrawal":
                     if policyholder == 0:
                         file_path = "./Report_pdf/policy_payment_withdrawal_client.xlsx"
                     else:
                         file_path = "./Report_pdf/policy_payment_withdrawal_partner.xlsx"
                 else:
                    file_path = "./Report_pdf/tenant_test_payment_withdrawal.xlsx"

                 with open(file_path, "wb") as f:
                    f.write(response.content)
                 logger.info("Excel report downloaded successfully.")
             else:
                 logger.info("Failed to download Excel report. Status code:", response.status_code)
             return response

    return _use_fixture_with_parameter

@pytest.fixture
def post_policy_schedule(define_env,request):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id,policyholder,partner_cust_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        if policyholder == 0 :
            id=customer_id
        elif policyholder == 1:
            id = partner_cust_id
        payload = common.update_portfolionetworth_data(id)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        response = requests.post(endpoint + f"/report/new/global/policy-schedule", json=json_payload, headers=headers)
        #logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            if response.status_code == 200 or 201:
                if request.function.__name__ == "test_add_policy_schedule":
                    if policyholder == 0:
                        file_path = "./Report_pdf/policy_schedule_client.xlsx"
                    else:
                        file_path = "./Report_pdf/policy_schedule_partner.xlsx"
                else:
                    file_path = "./Report_pdf/tenant_test_investment_schedule.xlsx"

                with open(file_path, "wb") as f:
                    f.write(response.content)
                logger.info("Excel report downloaded successfully.")
            else:
                logger.info("Failed to download PDF report. Status code: %s", response.status_code)
            return response

    return _use_fixture_with_parameter

@pytest.fixture
def post_investment_schedule(define_env,request):
    '''
    Function to send get request to get user details
    '''
    def _use_fixture_with_parameter(customer_id,jointindicator,partner_cust_id):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        endpoint = define_env
        if jointindicator == 0 :
            id=customer_id
        elif jointindicator == 1:
            id = partner_cust_id
        payload = common.update_portfolionetworth_data(id)
        json_payload = json.loads(payload)
        logger.info(json_payload)
        response = requests.post(endpoint + f"/report/new/global/investment-schedule", json=json_payload, headers=headers)
        #logger.info(response.json())
        status_code_check(response.status_code)
        if status_code_check:
            if response.status_code == 200 or 201:
                if request.function.__name__ == "test_add_investment_schedule":
                    if jointindicator == 0:
                        file_path = "./Report_pdf/investment_schedule_client.xlsx"
                    else:
                        file_path = "./Report_pdf/investment_schedule_partner.xlsx"
                else:
                    file_path = "./Report_pdf/tenant_test_investment_schedule.xlsx"

                with open(file_path, "wb") as f:
                    f.write(response.content)
                logger.info("Excel report downloaded successfully.")
            else:
                logger.info("Failed to download PDF report. Status code: %s", response.status_code)
            return response

    return _use_fixture_with_parameter


test_start_times = {}
def pytest_runtest_setup(item):
    start_time = datetime.now()
    test_start_times[item.name] = start_time
    print(f"Test '{item.name}' started at: {start_time}")

    # Append the start time of each test to the file
    with open("test_report.txt", "a") as f:
        f.write(f"Test '{item.name}' started at: {start_time}\n")

def pytest_runtest_teardown(item):
    end_time = datetime.now()
    print(f"Test '{item.name}' finished at: {end_time}")

    # write this to a file
    with open("test_report.txt", "a") as f:
        f.write(f"Test '{item.name}' finished at: {end_time}\n")


@pytest.fixture
def get_template(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/notification/get-template", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter

@pytest.fixture
def get_template_invalid_url(define_env):
    '''
    Function to send get request to get all income details in the master library
    '''

    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/notification/get", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()

    return _use_fixture_with_parameter

@pytest.fixture
def get_client_data(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/client?limit=10&page=1", headers=headers)
        status_code_check(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def get_client_data_with_invalid_url(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter():
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        get_client_api = requests.get(endpoint + "/clie", headers=headers)
        status_code_check1(get_client_api.status_code)
        if status_code_check:
            return get_client_api
        else:
            return False, get_client_api.json()
    return _use_fixture_with_parameter

@pytest.fixture
def post_email_data(define_env):
    '''
    Function to send post request to add data to liability
    '''
    def _use_fixture_with_parameter(customer_id,data, file):
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation",
            'userid' : "370dd58e-0a23-491f-89ec-0958f724e772"
        }
        endpoint = define_env
        payload = common.update_email_json_data(customer_id)
        json_payload = json.loads(payload)
        if file == True:
            pass
        else:
            for i, j in data.items():
                json_payload[i] = j
        logger.info(json_payload)
        response = requests.post(endpoint + "/user/emailbulk", json=json_payload, headers=headers)
        # response = requests.post(endpoint + "/liability", json=json_payload, headers=headers)
        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter

@pytest.fixture
def delete_client_details(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter(context,id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if context == 'employment':
            response = requests.delete(endpoint + f"/client/delete/employment/{id}", headers=headers)
        elif context == 'attitude_to_risk':
            response = requests.delete(endpoint + f"/client/delete/attituderisk/{id}", headers=headers)
        elif context == 'identity':
            response = requests.delete(endpoint + f"/client/delete/identity/{id}", headers=headers)
        elif context == 'objectives':
            response = requests.delete(endpoint + f"/client/delete/objective/{id}", headers=headers)
        elif context == 'servicetype':
            response = requests.delete(endpoint + f"/client/delete/servicetype/{id}", headers=headers)
        elif context == 'income':
            response = requests.delete(endpoint + f"/assystcashflow/delete/income/{id}", headers=headers)
        elif context == 'expense':
            response = requests.delete(endpoint + f"/assystcashflow/delete/expense/{id}", headers=headers)
        elif context == 'dependent':
            response = requests.delete(endpoint + f"/client/delete/dependant/{id}", headers=headers)
        elif context == 'addressbook':
            response = requests.delete(endpoint + f"/client/delete/address/{id}", headers=headers)
        elif context == 'factfindnotes':
            response = requests.delete(endpoint + f"/client/delete/note/{id}?isforce=true", headers=headers)
        elif context == 'factfindnotesfile':
            response = requests.delete(endpoint + f"/client/delete/note/{id}?isforce=false", headers=headers)
        elif context == 'client_action':
            response = requests.delete(endpoint + f"/client/delete/appointment/{id}", headers=headers)
        elif context == 'contact_note':
            response = requests.delete(endpoint + f"/client/delete/note/{id}?isforce=true", headers=headers)
        elif context == 'contact_note_file':
            response = requests.delete(endpoint + f"/client/delete/note/{id}?isforce=false", headers=headers)


        else:
            logger.error("Context Not Implemented")

        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


@pytest.fixture
def delete_case_details(define_env):
    '''
    Function to send get request to get all client and client details
    '''
    def _use_fixture_with_parameter(context,id):
        endpoint = define_env
        bearer_token = get_bearer_token()
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Testing': "api-automation"
        }
        if context == 'asset':
            response = requests.delete(endpoint + f"/case/delete/asset/{id}", headers=headers)
        elif context == 'liability':
            response = requests.delete(endpoint + f"/case/delete/liability/{id}", headers=headers)
        elif context == 'policy':
            response = requests.delete(endpoint + f"/case/delete/policy/{id}", headers=headers)
        elif context == 'action':
            response = requests.delete(endpoint + f"/case/delete/business/{id}", headers=headers)


        else:
            logger.error("Context Not Implemented")

        status_code_check(response.status_code)
        if status_code_check:
            return response
        else:
            return False, response.json()
    return _use_fixture_with_parameter


STATIC_CUSTOMER_ID = "c7ff5f69-3b4c-4273-ab4b-87f20e0d8358"
@pytest.fixture
def customer_id():
    return STATIC_CUSTOMER_ID

STATIC_PARTNER_ID = "3233fb6f-eeb6-4b24-ad70-c28c06b3dee0"
@pytest.fixture
def partner_cust_id():
    return STATIC_PARTNER_ID

STATIC_PROVIDER_CORRESPONDENSE_ID = "66a9e663-1a9f-4645-9fcd-f8975623801b"
@pytest.fixture
def provider_correspondence_id():
    return STATIC_PROVIDER_CORRESPONDENSE_ID

STATIC_USER_ID = "46b6f4bb-50f3-4d9a-bebe-e8f92ec2d5e7"
@pytest.fixture
def user_id():
    return STATIC_USER_ID

def status_code_check(status_code):
    '''
    Function to check status code
    '''
    if status_code == 200 or status_code == 201:
        # logger.info("Status Code: %s" % status_code)
        return True
    elif int(status_code) == 500:
        assert False, "API call failed with message: 'Please Contact Administrator'"
    elif int(status_code) == 400:
        assert False, "Requested resource could not be found"
    elif int(status_code) == 403:
        assert False, "Forbidden resource"
    elif int(status_code) == 401:
        assert False, "Unauthorized"
    elif int(status_code) == 404:
        assert False, "Not Found"
    else:
        raise Exception(f"Unexpected Status Code: {status_code}")

def status_code_check1(status_code):
    '''
    Function to check status code
    '''
    if status_code == 500 or status_code == 404 or status_code == 403 or status_code == 401 :
        # logger.info("Status Code: %s" % status_code)
        return True

    else:
        raise Exception(f"Unexpected Status Code: {status_code}")


def pytest_addoption(parser):
    '''
    Function to give the environment in the command line
    '''
    parser.addoption(
        "--env", "--context",
        default="https://qa-api.assyst.cloud/asc/api/v1.0",
        help="Endpoint",
    )
    parser.addoption(
        "--test",
        default="field_values",
    )