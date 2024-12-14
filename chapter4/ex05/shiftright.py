# Write your program here
bit_string = input("Enter a bit string: ")
shift_right = ""
shift_right = bit_string[-1]
shift_right = shift_right + bit_string[:-1]
print(shift_right)