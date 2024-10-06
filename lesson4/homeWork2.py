message = input("Enter a message: ")

print("Lowercase: " + message.lower())
print("Uppercase: " +message.upper())

print("Capitalized: " +message[0].upper() + message[1:].lower())

print("Title case: " +message.title())

words = message.split(" ")
print(f'Words: {words}')
