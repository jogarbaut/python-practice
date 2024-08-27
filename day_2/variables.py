# Day 2: 30 Days of python programming
import math

# Variable declaration practice
first_name = 'Jomel'
last_name = 'Bautista'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'Cupertino'
age = 30
year = 2024
is_married = False
is_true = True
is_light_on = False
pet_name_1, pet_name_2 = 'Koko', 'Elle'

# Variable declaration checks
print(type(first_name))
print(len(first_name))
print(len(first_name) > len(last_name))

# Math practice
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Geometry practice
radius = int(input('Enter radius of circle: '))
area_of_circle = math.pi * radius ** 2
circum_of_cirle = 2 * math.pi * radius
print(f"Area: {area_of_circle:.2f}")
print(f"Circumference: {circum_of_cirle:.2f}")

