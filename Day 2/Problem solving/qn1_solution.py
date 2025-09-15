words_str = input("Enter words separated by spaces: ")
words_list = words_str.split()
words_tuple = tuple(words_list)
print("List:", words_list)
print("Tuple:", words_tuple)

filename = "words.txt"
with open(filename, 'w') as writer:
    writer.write(f'List: {words_list}\n')
    writer.write(f'Tuple: {words_tuple}')

with open(filename, 'r') as reader:
    line_list = reader.readlines()
    line_tuple = reader.readline()
    print(line_list)
    print(line_tuple)