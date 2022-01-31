'''
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
'''

'''
This method [ str.isalnum() ] checks if all the characters of a string are
alphanumeric (a-z, A-Z and 0-9)
'''

print('ab123'.isalnum())
#OUTPUT: True
print('ab123#'.isalnum())
#OUTPUT: False

'''
This method [ str.isalpha() ] checks if all the characters of a string are
alphabetical (a-z and A-Z)
'''

print('abcD'.isalpha())
#OUTPUT: True
print('abcd1'.isalpha())
#OUTPUT: False

'''
This method [ str.isdigit() ] checks if all the characters of a strings are
digits (0-9)
'''

print('1234'.isdigit())
#OUTPUT: True
print('123dgv'.isdigit())
#OUTPUT: False

