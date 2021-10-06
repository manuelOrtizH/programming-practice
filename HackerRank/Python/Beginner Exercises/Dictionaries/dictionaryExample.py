a_dict = {'one': 1} #Here 'one' is the key

#The key of a dictionary is immutable. 
#We cannot use a list as a key because a list is mutable. 
#But we can make a tuple of list and use as key.

a_dict['two'] = 2 # Adds key 'two' which points to 2
print (a_dict['one']) #Prints '1'

if 'three' in a_dict:
	#To check whether a certain string exist as a key in the dictionary
	print(a_dict['three'])
else:
	print("There is not three")

del a_dict['one'] #Deletes index 'one' and the value associated with it
print(a_dict) #prints {'two': 2}

#A dictionary is unordered. So, only use the keys to navigate through the dictionary