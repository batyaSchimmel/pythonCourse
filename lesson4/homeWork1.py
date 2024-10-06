message = input("Enter a message: ")

print("First character: " + message[0])

print("Last character: "  + message[-1])

len = int(len(message) / 2)
print("Middle character: " + message[len])
# len=int(len(message)/2)
# print(message[len-1])

print("Even index character: " + message[::2])

print("Odd index character: " + message[1::2])

print("Reversed message: " +message[::-1])
