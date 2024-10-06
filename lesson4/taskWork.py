# 2
# mystring = input("enter string: ")
# print(mystring[-1] + mystring[:-1])

# # 3
# mystring = input("enter string: ")
# print(mystring[1::2])

# #4
# word= input("enter string: ")
# print(word)
# print(word.upper())

# 5
myString = input("enter string: ")
if len(myString) >= 6:
    print(myString[:3].upper() + myString[3:-3].lower() + myString[-3:].upper())
else:
    print("A string should contain 6 char and more")
