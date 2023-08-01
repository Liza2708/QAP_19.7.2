from api import PetFriends
from settings import valid_password, valid_email
import pytest
import os

pf = PetFriends()

#_________________________Практическое задание 19.7.2______________________________
#__ Часть тестов не прошли проверку, намеренно оставила их с ожидаемым результатом -> необходимо завести баг-репорт
# 1)
def test_add_new_pet_with_valid_data_without_photo(name='Барбоскин', animal_type='двортерьер', age=4):
    """Проверяем что можно добавить питомца с корректными данными без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

# 2)
def test_successful_add_photo_of_pet(pet_photo ='images\yasherka.jpg'):
    """Проверяем возможность добавления фото питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert result['pet_photo'] != ''
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

# 3)
def test_add_photo_of_pet_format_bmp(pet_photo ='images\cherepashka.bmp'):
    """Проверяем возможность добавления фото питомца в формате bmp (файл потяжелее jpeg)"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
        assert result['pet_photo'] != ''
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

# 4)
def test_not_get_api_key_for_unregistered_user(email="trye@inbox.ru",password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403
    и не содержит значения 'key' в случае авторизации незарегистрированным пользователем"""
    status,result=pf.get_api_key(email,password)
    assert status == 403
    assert 'key' not in result

# 5)
def test_not_get_api_key_for_user_with_not_valid_password(email=valid_email,password="56784"):
    """ Проверяем что запрос api ключа возвращает статус 403
    и не содержит значения 'key' в случае авторизации пользователя с неверным паролем"""
    status,result=pf.get_api_key(email,password)
    assert status == 403
    assert 'key' not in result

# 6)
def test_not_get_list_of_my_pets_with_not_valid_key(filter='my_pets', auth_key={'key':'456'}):
    """ Проверяем, что запрос не возвращает список питомцев в случае неавторизованного пользователя.
        Для этого сначала задаем невалидный api ключ. Далее, используя этот ключ,
        запрашиваем список всех питомцев и проверяем, что список не был возвращен в ответе (статус 403).
        Проверяем, что полученный результат является строкой (в случае позитивного теста результат возвращается словарем)
         """
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403
    assert type(result) == str

# 7)
def test_not_add_new_pet_with_valid_key_and_empty_values(name='', animal_type='', age=''):
    """Проверяем, что нельзя добавить питомца с пустыми значеними полей имени, возраста и типа.
    Возвращает код 200 - баг. -> Добавить в баг-репорт"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert type(result) == str

# 8)
def test_not_add_new_pet_with_valid_key_and_age_as_not_digit(name='Ириска', animal_type='кот', age='кот'):
    """Проверяем, что нельзя добавить питомца с кириллицей в поле возраста.
    Возвращает код 200 - баг. -> Добавить в баг-репорт"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert type(result) == str

# 9)
def test_not_add_new_pet_with_valid_key_and_ladge_name(name='ИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИрискаИриска', animal_type='кот', age='кот'):
    """Проверяем, что нельзя добавить питомца с очень длинным именем.
    Возвращает код 200 - баг. -> Добавить в баг-репорт"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert type(result) == str

# 10)
def test_not_add_new_pet_with_valid_key_and_spesial_symbols(name='&', animal_type='&', age='&'):
    """Проверяем, что нельзя добавить питомца со спец символами в полях имени, типа и возраста.
    Возвращает код 200 - баг. -> Добавить в баг-репорт"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert type(result) == str









