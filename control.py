'''
1. If statements- An if statement consists of a Boolean expression followed by one or more statements.
2. Elif Statements
'''

# If statement : An if statement consists of a Boolean expression followed by one or more statements
# If the condition is True, python will run the code present in If block otherwise it will skipp the If block

# Ex:
a = 50
b = 30
print("If condition")
print(">when condition is true<")
if a > b:
    print("50 is greater than 30 ")
    print("--If block executed")

print(">when condition is false<")
if a < b:
    print("50 is less than 30 ")
    print(b)
print("--If block Skipp or not executed")

# Else Statement : When 'If' condition is False, python will run the code present in Else block otherwise
# it will skipp the Else block

print("Else condition")
print(">when condition is false<")
if a < b:
    print("50 is less than 30 ")

else:
    print("30 is less than 50")
    print("--Else block executed")

# Elif Statement: To validate multiple condition is true, python will run the code present in Elif block
# otherwise it will skipp the Else block
