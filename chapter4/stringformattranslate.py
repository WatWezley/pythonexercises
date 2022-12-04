import string

user_input = input("Enter the word to decode:")
key = int(input("What key would you like to use:"))

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
decode_lower_letters = lower_letters[key:] + lower_letters[:key]
decode_upper_letters = upper_letters[key:] + upper_letters[:key]

letters = lower_letters + upper_letters + string.whitespace
decode_letters = decode_lower_letters + decode_upper_letters + string.whitespace
encoded = user_input.translate(str.maketrans(letters, decode_letters))
decoded = encoded.translate(str.maketrans(decode_letters, letters))

#print(user_input.translate(str.maketrans(lower_letters + " ", decoded_letters + " ")))
#print(user_input.translate(str.maketrans(decoded_letters + " ", lower_letters + " ")))

print(encoded)
print(decoded)
