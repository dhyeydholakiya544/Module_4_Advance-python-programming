Python program to read last n lines of a file:

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()[-n:]
        return lines

print(read_last_n_lines('example.txt', 5))