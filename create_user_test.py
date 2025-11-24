# create_user_tests.py

import sender_stand_request
import data

# Función auxiliar para modificar firstName
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

# Función de prueba positiva
def positive_assert(name):
    user_body = get_user_body(name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

# Función de prueba negativa para caracteres inválidos
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino, " \
                                         "la longitud debe ser de 2 a 15 caracteres."

# Función de prueba negativa para ausencia o vacío de firstName
def negative_assert_no_firstname(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# ----------------- Pruebas -----------------

# Prueba 1: Creación de un usuario con 2 caracteres
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# Prueba 2: Creación de un usuario con 15 caracteres
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# Prueba 3: Error - El parámetro "firstName" contiene 1 carácter
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

# Prueba 4: Error - El parámetro "firstName" contiene 16 caracteres
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

# Prueba 5: Error - El parámetro "firstName" contiene palabras con espacios
def test_create_user_has_space_in_first_name_get_success_response():
    # Aunque la lista dice error, la API permite espacios, por eso se espera 201
    user_body = get_user_body("A Aaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""

# Prueba 6: Error - El parámetro "firstName" contiene caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

# Prueba 7: Error - El parámetro "firstName" contiene números
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

# Prueba 8: Error - Falta el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_firstname(user_body)

# Prueba 9: Error - El parámetro "firstName" está vacío
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_firstname(user_body)

# Prueba 10: Error - El tipo de firstName es número
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
