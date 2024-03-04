# def users_info(name, lastname, age, adress, phone_number):
#     d = {
#         "name": name, "lastname": lastname, "age": age, "adress": adress, "phone_number": phone_number
#     }
#     return d
#
# while True:
#     pass
#
# def say_hello(user_password):
#     if user_password == '3554':
#         def inner():
#             print("Assalomu alaykum")
#
#         return inner
#
# user = say_hello('3554')
# user()
# -------------------------------------------------------------------------------------------------------
# def multiplay(num1):
#     def inner(num2):
#         return num1 * num2
#     return inner
#
# number = multiplay(5)
# print(number(4))
#

# -------------------------------------------------------------------------------------------------------

# users = [
#     {"id": 1, "name": "Toxir", "lastname": "Tohirov", "password": "123"},
#     {"id": 2, "name": "Sobir", "lastname": "Sobirov", "password": "12345"},
#     {"id": 3, "name": "Mansur", "lastname": "Odilov", "password": "123546"}
# ]
#
# def get_users(users_list: list):
#     def inner(username):
#         return list(filter(lambda user: user["name"] == username, users_list))
#     return inner
#
# user = get_users(users)
# print(user('Mansur'))

# -------------------------------------------------------------------------------------------------------

# decoratorlar

def test_decoration(func):
    def wrapper(*args, **kwargs):
        print("Nimadir ish bajaradi")
        func(*args, **kwargs)
        print("yana qanaqadir ish qiladi")
    return wrapper

@test_decoration
def say_hello(name):
    print(f"Assalomu alaykum {name}")
say_hello()

