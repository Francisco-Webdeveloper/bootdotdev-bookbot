def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

main()