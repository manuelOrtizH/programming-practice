'''
When given an inmutable string, the only way to make changes to the string 
is through a list
'''

string = "guiltyparty"

print(string[5])
#OUTPUT: a

#string[5] = 'i'
#ERROR: 'str' object does not support item assignment

l = list(string)
l[5] = 'i'
string = ''.join(l)
print(string)
#OUTPUT: guiltiparty

#Anothere approach is to slice the string and join it back

string = string[:5] + "z" + string[6:]
print(string)
#OUTPUT: guiltzparty