# Write your program here
original_file = input("Enter name of original file: ")
file_copy = input("Enter name of file to copy to: ")

read_file = open(original_file, 'r')
contents = read_file.read()

write_file = open(file_copy, 'w')
write_file.write(contents)

read_file.close()
write_file.close()