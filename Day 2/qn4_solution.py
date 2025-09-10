list_of_names = input("Enter names seperated by commas:")
names = list_of_names.split(',')
names.sort()
tuple_of_names = tuple(names)
print('List of names', names)
print('Tuple of names', tuple_of_names)


filename = "names_data.txt"
with open(filename, 'w') as writer:
    writer.write(f'List of names: {names}\n')
    writer.write(f'Tuple of names: {tuple_of_names}')

with open(filename, 'r') as reader:
    list_names = reader.readline()
    tuple_names = reader.readline()
    print(list_names)
    print(tuple_names)