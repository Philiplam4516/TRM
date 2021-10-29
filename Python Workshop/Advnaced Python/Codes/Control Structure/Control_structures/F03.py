'''
Write a python program to filter out the strings with captal lectters in a list 
'''

list_str = ["I", "am", "new", "to", "Python"]

# option 1: use list Comprehensions
print("use list Comprehensions")
newlist = [string for string in list_str for c in string if c>='A' and c<='Z']
print(newlist)

# option 2: use for loops
print("use for loops")
newlist = []
for string in list_str:
	for c in string:
		if c>='A' and c<='Z':
			newlist.append(string)
			break
print(newlist)








