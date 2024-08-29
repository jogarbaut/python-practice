# Declare your age as integer variable
age = 100

# Declare your height as a float variable
user_height = 72.0

# Declare a variable that store a complex number
complex_num = 2j + 1

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input('Enter base: '))
height = float(input('Enter height: '))
tri_area = 0.5 * base * height
print(f"The area of the triangle is {tri_area}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') < len('dragon'))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
param_1 = 7 // 3
param_2 = int(2.7)
print(param_1 == param_2)