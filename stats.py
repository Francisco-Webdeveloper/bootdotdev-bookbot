
def count_total_words(main):
    text = main()
    words_list = text.split()
    number_of_words = len(words_list)
    print(f"{number_of_words} words found in the document")