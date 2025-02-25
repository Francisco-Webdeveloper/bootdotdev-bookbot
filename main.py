import sys
from stats import count_total_words, count_each_char, chars_count_sorted_list

def main():
    cli_arguments = len(sys.argv)
    if cli_arguments < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number_of_words = count_total_words(text)
    number_of_chars_dict = count_each_char(text)
    list_of_chars = chars_count_sorted_list(number_of_chars_dict)
    print_report(number_of_words, list_of_chars)

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def print_report(number_of_words, list_of_chars):
    # Heder
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    # Word count section
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")

    # Character count section
    print("--------- Character Count -------")
    for char_dict in list_of_chars:
        for char in char_dict:
            print(f"{char}: {char_dict[char]}")

    # Footer
    print("============= END ===============")

main()