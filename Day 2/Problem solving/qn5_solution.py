list_number = input("Enter numbers separated by space:")
numbers = list_number.split(' ')
maximum = max(numbers)
minimum = min(numbers)

filename = "list of numbers.txt"
with open (filename, 'w') as writer:
    writer.write(f'List of numbers: {numbers}\n')
    writer.write(f'Maximum number: {maximum}\n')
    writer.write(f'Minimum number: {minimum}')

with open (filename, 'r') as reader:
    content = reader.read()
    print(content)

