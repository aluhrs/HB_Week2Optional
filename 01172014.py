"""Write a function that returns true if 
passed a string with only unique characters"""

def unique(string):

for i in string:
	if string[i] = string[i + 1]:
		return False
	else:
		return True

	return True

unique("ashley")

""" possible options """


# if string[i] = string [i + 1]
# 1. lowercase the string and then check ascii characters
# 2. recursion similar to palindrome?
# 