from stats import count_total_words, count_each_char

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_total_words(text)
    number_of_chars = count_each_char(text)
    print(f"{number_of_words} words found in the document")
    print(number_of_chars)

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

main()