Python program to find the longest words:

def find_longest_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        longest_words = [word for word in words if len(word) == max(len(w) for w in words)]
        return longest_words

print(find_longest_words('example.txt'))