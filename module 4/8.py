Python program to count the number of lines in a text file:


def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

print(count_lines('example.txt'))