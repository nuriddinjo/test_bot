# Task 1
# import sqlite3
#
#
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()
#
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY,
#                     username TEXT,
#                     name TEXT,
#                     lastname TEXT,
#                     age INTEGER,
#                     address TEXT,
#                     email TEXT,
#                     phone TEXT
#                 )''')
#
#
# def add_user(username, name, lastname, age, address, email, phone):
#
#     cursor.execute('''INSERT INTO users (username, name, lastname, age, address, email, phone)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (username, name, lastname, age, address, email, phone))
#     conn.commit()
#
#
# def close_connection():
#     conn.close()
#
#
# def main():
#     users = []
#     while True:
#         username = input("Foydalanuvchi nomini kiriting: ")
#         name = input("Ismni kiriting: ")
#         lastname = input("Familiyani kiriting: ")
#         age = int(input("Yoshni kiriting: "))
#         address = input("Manzilni kiriting: ")
#         email = input("Elektron pochtani kiriting: ")
#         phone = input("Telefon raqamini kiriting: ")
#
#         add_user(username, name, lastname, age, address, email, phone)
#
#         stop = input("Foydalanuvchilarni qo'shishni to'xtatmoqchimisiz? (ha/yo'q): ")
#         if stop.lower() == 'ha':
#             break
#
#     close_connection()
#
# if __name__ == "__main__":
#     main()

#--------------------------------------------------------------------------------------------------

# import sqlite3
#
# def get_user_info(username):
#
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#
#     def get_user_from_db():
#
#         cursor.execute("SELECT * FROM users WHERE username=?", (username,))
#         user = cursor.fetchone()
#         return user
#
#
#
#
#     return get_user_from_db
#
#
# username = input("Foydalanuvchi nomini kiriting: ")
# get_user = get_user_info(username)
# user = get_user()
#
# if user:
#     print("Foydalanuvchi ma'lumotlari:")
#     print("Ism:", user[1])
#     print("Familiya:", user[2])
#     print("Yosh:", user[3])
#     print("Manzil:", user[4])
#     print("Email:", user[5])
#     print("Telefon:", user[6])
# else:
#     print("Bunday foydalanuvchi topilmadi.")
#

#--------------------------------------------------------------------------------------------------

# import time
#
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"\"{func.__name__}\" funksiyasi bajarildi vaqt: {execution_time} soniya")
#         return result
#     return wrapper
#
#
# @measure_time
# def qoshish(a, b):
#     return a + b
#
#
# @measure_time
# def ayirish(a, b):
#     return a - b
#
#
# @measure_time
# def kopaytirish(a, b):
#     return a * b
#
#
# @measure_time
# def bolish(a, b):
#     if b == 0:
#         raise ValueError("Nolga bo'lish mumkin emas")
#     return a / b
#
#
# def test():
#     a = 10
#     b = 5
#     print(f"{a} + {b} = {qoshish(a, b)}")
#     print(f"{a} - {b} = {ayirish(a, b)}")
#     print(f"{a} * {b} = {kopaytirish(a, b)}")
#     print(f"{a} / {b} = {bolish(a, b)}")
#
# if __name__ == "__main__":
#     test()
