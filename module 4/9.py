Python program to count the frequency of words in a file:


def count_word_frequency(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        return frequency

print(count_word_frequency('example.txt'))