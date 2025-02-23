def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    return text

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def count_total_words():
    text = main()
    words_list = text.split()
    number_of_words = len(words_list)
    print(f"{number_of_words} words found in the document")

count_total_words()