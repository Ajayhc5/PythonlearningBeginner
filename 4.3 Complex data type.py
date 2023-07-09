# 3. Complex(): data type to represent complex values, in the (a+bj) a= Real part, b = Imaginary part
# In the real part we can use only int values like Whole number, Decimal, Octal, Binary, Hexa decimal
# In the Imaginary part should accept only Decimal and Whole number
'''
* hold the complex values
* indexing not applicable
* slicing not applicable
* Immutable (value assignments is not possible or not able to change the value)
'''

# Ex:
a = 5 + 12.34j
print("complex: whole number used in Real part")
print(type(a))
print(a)

b = 5.25 + 12j
print("complex: Decimal value used in Real part + whole number used in Imaginary part")
print(type(b))
print(b)
