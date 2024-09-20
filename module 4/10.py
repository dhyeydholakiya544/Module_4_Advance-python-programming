Python program to write a list to a file:


def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

write_list_to_file('example.txt', [1, 2, 3, 4, 5])