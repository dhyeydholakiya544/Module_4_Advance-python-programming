Python program to append text to a file and display the text:


with open('example.txt', 'a') as file:
    file.write('This is a new line of text.\n')
    file.write('This is another new line of text.\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)