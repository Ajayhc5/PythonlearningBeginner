# 5. Str(): string is collection of characters, enclosed within single quotes or double quotes.
'''
* hold the Characters
* indexing applicable
* slicing applicable
* Immutable (value assignments is not possible or not able to change the value)
'''

# Ex:
first_name = 'Ram'
last_name = 'Kumar'
print("string")
print(type(first_name))
print(first_name)

first_name[2] = 'n'
print(first_name)

# slicing of string : slice mean a piece
# [] operator is called slice operator, R=0, a=1, m=2, / m=-1, a=-2, R=-3
print("Index, Slice")
print(first_name[0])
print(first_name[0:2])
print(first_name[-2:])

# concatenate
print("Concatenate")
print(first_name + last_name)
full_name = first_name + " " + last_name
print(full_name)

# characters enclosed within single quotes or double quotes.
learn = "I don't no any programming languages"
learn1 = 'I started to learn the Python language'
learn2 = ''' I started
to learn
the Python language'''

print(learn)
print(learn1)
print(learn2)
