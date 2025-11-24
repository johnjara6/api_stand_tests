import configuration
import requests
import data

# Solicitud GET a la documentación
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# Solicitud GET para logs
def get_logs():
    response = requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
    print(response.status_code)
    print(response.headers)
    return response

# Solicitud GET para la tabla de usuarios
def get_users_table():
    response = requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
    print(response.status_code)
    return response

# Solicitud POST para crear un nuevo usuario
def post_new_user(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )
    print(response.status_code)
    print(response.json())
    return response

# Solicitud POST para buscar kits por productos
def post_products_kits(products_ids):
    response = requests.post(
        configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
        json=products_ids,
        headers=data.headers
    )
    print(response.status_code)
    print(response.json())
    return response
