Python program to copy the contents of a file to another file:

def copy_file_contents(src_filename, dst_filename):
    with open(src_filename, 'r') as src_file:
        with open(dst_filename, 'w') as dst_file:
            dst_file.write(src_file.read())

copy_file_contents('example.txt', 'copy.txt')
