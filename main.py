from stats import (
    count_words, 
    count_chars, 
    dict_to_sorted_list
)

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    word_count = count_words(content)
    char_count = count_chars(content)
    sorted_char_count = dict_to_sorted_list(char_count)
    print_report(book_path, word_count, sorted_char_count)



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sorted_char_count):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for i in range(0, len(sorted_char_count)):
        print(f"{sorted_char_count[i]['char']}: {sorted_char_count[i]['num']}")
    print(f"============= END ===============")

main()