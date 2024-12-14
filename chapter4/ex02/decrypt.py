# Write your program here
encrypted_text = input("Enter text to decrypt: ")
distance = int(input("Enter a distance value: "))
plain_text = ""

for character in encrypted_text:
    encrypted_char = ord(character)
    encrypted_char = (encrypted_char - distance) % 128
    encrypted_char = chr(encrypted_char)
    plain_text = plain_text + encrypted_char

print(plain_text)