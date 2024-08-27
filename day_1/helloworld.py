# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Jomel'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Jomel'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# Euclidian distance
point_1 = (2, 3)
point_2 = (10, 8)
euclidian_dist = (((point_2[1] - point_1[1]) ** 2) + ((point_2[0] - point_1[0]) ** 2)) ** 0.5
print(euclidian_dist)