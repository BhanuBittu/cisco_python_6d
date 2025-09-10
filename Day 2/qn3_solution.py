sentence = input('Enter a sentence: ')
words = sentence.split()
tuple_words = tuple(word.upper() for word in words)
print('List:', words)
print('Tuple:', tuple_words) 


filename = 'sentence_data.txt'
with open(filename, 'w') as writer:
    writer.write(f'List of words: {words}')
    writer.write(f'Tuple of words: {tuple_words}')

with open(filename, 'r') as reader:
    list_words = reader.readline()
    tuple_words = reader.readline()
    print(list_words)
    print(tuple_words)