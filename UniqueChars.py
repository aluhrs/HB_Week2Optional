"""Write a function that returns true if 
passed a string with only unique characters"""

def unique(string):

	# create an empty dictionary
    d = {}    
    
    # convert the string to a list
    letters = list(string)
    
    # go through each letter and check if it is NOT in the dictionary
    # if it is not, add it
    # if it is, exit the program because it is not a unique letter
    for i in letters:
        if not d.get(i):
            d[i] = 1
        elif d.get(i):
            return False
        
    return True

unique("mom")