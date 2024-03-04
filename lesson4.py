# namedtuple


# class Employee:
#     def __init__(self, id, name, lastname, age, email ):
#         self.id = id
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
# employees = [
#     (1, "Tohir", "Tohirov", 25, "tohir@gmail.com"),
#     (2, "Sobir", "Sobirov", 30, "sobir@gmail.com"),
#     (3, "Malik", "Malikov", 32, "malik@gmail.com")
# ]
#
# for employee in employees:
#     em = Employee(*employee)
#     print(em.id, em.name, em.lastname, em.age, em.email)

# -------------------------------------------------------------------------------------------------

# from collections import namedtuple
# Employee = namedtuple('Employee', 'id name lastname age email')
#
# employees = [
#     (1, "Tohir", "Tohirov", 25, "tohir@gmail.com"),
#     (2, "Sobir", "Sobirov", 30, "sobir@gmail.com"),
#     (3, "Malik", "Malikov", 32, "malik@gmail.com")
# ]
#
# for employee in employees:
#     em = Employee(*employee)
#     print(em.id, em.name, em.lastname, em.age, em.email)

# -------------------------------------------------------------------------------------------------

# from collections import namedtuple
# Car = namedtuple('Car', 'id model color speed price')
#
# cars = [
#     (1, "Gentra", "Black", 220, "18000"),
#     (1, "Malibu", "White", 270, "35000"),
#     (1, "Damas", "White", 140, "16000"),
# ]
#
# for car in cars:
#     mashina = Car(*car)
#     print(mashina.id, mashina.model, mashina.color, mashina.speed, mashina.price)

# -------------------------------------------------------------------------------------------------

