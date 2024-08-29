# Day 4 - String Methods

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str_1, str_2, str_3, str_4 = 'Thirty', 'Days', 'Of', 'Python'
space = ' '
str_combined = str_1 + space + str_2 + space + str_3 + space + str_4
print(str_combined)

# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
company = 'Coding For All'
print(f'original string: {company}')
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(f'upper() method: {company.upper()}')

# Change all the characters to lowercase letters using lower() method.
print(f'lower() method: {company.lower()}')

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(f'capitalize() method: {company.capitalize()}')
print(f'title() method: {company.title()}')
print(f'swapcase(): {company.swapcase()}')

# Cut(slice) out the first word of Coding For All string.
print(f'slice() method to slice out first word: {company.split(' ', 1)[1]}')

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_str = 'Coding'
print(f'index() method to search for str: {company.index(sub_str)}')

# Replace the word coding in the string 'Coding For All' to Python.
print(f'replace() method: {company.replace(sub_str, 'Python')}')

# Split the string 'Coding For All' using space as the separator (split()) .
print(f'split method: {company.split()}')

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(f'split at char: {company_2.split(',')}')


# Create an acronym or an abbreviation for the name 'Coding For All'.
first_char = [sub[0] for sub in company.split()]
acronym = ''.join(first_char)
print(f'creating an acronym: {acronym}')

# Use index to determine the position of the first occurrence of C in Coding For All.
print(f'find method for index of C: {company.find('C')}')

# Use index to determine the position of the first occurrence of F in Coding For All.
print(f'find method for index of F: {company.find('F')}')

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(f'rfind method for last index of l: {company.rfind('l')}')