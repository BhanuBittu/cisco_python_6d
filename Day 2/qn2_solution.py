int_list = list(map(int, input("Enter the number separated by the space:").split()))
sum_of_list = sum(int_list)
average_of_list = sum_of_list / len(int_list)
print(f'Sum of the lsit: {sum_of_list}')
print(f'Average of the list: {average_of_list}')

filename = "numbers.txt"
with open(filename, 'w') as writer:
    writer.write(f'Sum of the list: {sum_of_list}\n')
    writer.write(f'Average of the list: {average_of_list}')

with open(filename, 'r') as reader:
    sum_list = reader.readline()
    avg_list = reader.readline()
    print(sum_list)
    print(avg_list)