from stats import count_total_words, count_each_char, chars_count_sorted_list

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_total_words(text)
    number_of_chars_dict = count_each_char(text)
    list_of_chars = chars_count_sorted_list(number_of_chars_dict)

    # HeADER
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


def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

main()