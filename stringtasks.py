# Define String
str = """Python is an interpreted, object-oriented, high-level programming language with dynamic
semantics
"""

# 1. Count the number of characters in the string
print(len(str))
# print 0 - 2
print(str[0:1])
print(str[0:3])
print(str[-4: -1])
print(str[::-1])
print("       ")
print(str[1:-2])
print(str.upper())
list = list(str)
for index, char in enumerate(list):
    if char == "a":
        list[index] = "e"

print("".join(list))
x = list.index(",")
list2 = list[x:]
str2 = "".join(list2)
print(str2.upper())
