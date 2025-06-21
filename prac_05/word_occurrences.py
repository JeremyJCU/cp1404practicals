"""
CP1404/CP5632 Practical
A program to count the occurrences of words in a string
"""
WORD_TO_COUNT = {'a': 0, 'collection': 0, 'fun': 0, 'is': 0, 'it': 0, 'nice': 0, 'of': 0, 'thing': 0, 'this': 0,
                 'words': 0}


def main():
    """Count the occurrences of words in a string"""
    sentence = input("Text: ")
    words = sentence.split()
    word_to_count_total = calculate_word_total(WORD_TO_COUNT, words)
    max_word_length = determine_word_length(word_to_count_total)
    print_word_count(word_to_count_total, max_word_length)


def calculate_word_total(word_to_count, words):
    """Total each occurrence of a word in a string"""
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count


def determine_word_length(word_to_count):
    """"Determine the max length of a word key from a dictionary"""
    max_word_length = max(len(word) for word in word_to_count)
    return max_word_length


def print_word_count(word_to_count, max_word_length):
    """Print the occurrences of a words from input string"""
    for word, count in word_to_count.items():
        print(f'{word:{max_word_length}} : {count}')


main()
