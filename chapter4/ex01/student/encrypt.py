# Write your program here
plain_text = input("Enter a message to encrypt: ")
distance = int(input("Enter a distance value: "))
encrypted_text = ""

for character in plain_text:
    new_character = ord(character)
    new_character = (new_character + distance) % 128
    new_character = chr(new_character)
    encrypted_text = encrypted_text + new_character
    
print(encrypted_text)