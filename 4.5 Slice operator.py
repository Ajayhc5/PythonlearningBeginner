#  Slice operator: mean piece of character , should be use [] to retrieve part of the string.
# n[begin:end]--- it returns substring from begin index to end -1 index
# Ex:
#    0123456789, h=12, a=13, r=14, a=15, c=16, t=17, e=18, r=19,
a = "piece of character"
print(a[0:4])

print("---with out begin value---")
print(a[
      :7])  # if we are not specified begin value then it will consider beginning of the string-- ie default value is '0'

print("---with out end value---")
print(a[3:])  # if we are not specified end value then it will consider until end of the string

print("---with out begin & end value---")
print(a[:])  # if we are not specified begin & end value then it will consider from beginning to until end of the string

# Back ward
# p=-18, i=-17, e=-16, c=-15, e=-14,' '=-13, o=-12, f=-11, ' '=-10,c=-9, h=-8, a=-7, r=-6, a=-5, c=-4, t=-3, e=-2, r=-1,
# a = "piece of character"
print("---backward---")
print(a[-8:-2])

# Convert the character to upper case
print("---character to upper case---")
print(a[0].upper() + a[1:])

# Convert the character to lower case
print("---character to lower case---")
print(a[0].lower() + a[1:])
