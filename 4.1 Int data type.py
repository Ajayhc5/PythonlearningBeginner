# 1. int(): data type to represent whole numbers(integral values), the number without decimal points
# It can have positive and negative numbers as well
'''
* hold the integral values
* indexing not applicable
* slicing not applicable
* Immutable (value assignments is not possible or not able to change the value)
'''
# Ex:
a = 24
print(type(a))

# Types of whole number forms are (Decimal form, Binary form, Octal form, Hexadecimal form)
# *) Decimal: divided by 10 or base 10, allowed digits are: 0 to 9
b = 10

# *) Binary form: divided by 2 or base 2, allowed digits are: 0 & 1
c = 26
print("Binary form")
print(bin(c))
print(0b11010)

# *) Octal form: divided by 8 or base 8, allowed digits are: 0 & 7
d = 1650
print("Octal form")
print(oct(d))
print(0o3162)

# *) Hexadecimal form: divided by 16 or base 16, allowed digits are: 0 & 9, a-f
# a = 10, b=11, c=12, d=13, e=14, f=15
e = 5349
print("Hexadecimal form")
print(hex(e))
print(0x14e5)
