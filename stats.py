def count_total_words(text):
    words_list = text.split()
    return len(words_list)

def count_each_char(text):
    chars_count = {}
    words_list = text.split()

    for word in words_list:
         word_lowercased = word.lower()
         for char in word_lowercased:
            if char in chars_count:
                chars_count[char] += 1
            else: 
                chars_count[char] = 1  
    
    return chars_count

def sort_on(num_of_chars_dict):
    return list(num_of_chars_dict.values())[0]

def chars_count_sorted_list(num_of_chars_dict):
    list_char_dictionaries = []
    for char in num_of_chars_dict:
        dictionary = {char: num_of_chars_dict[char]}
        if char.isalpha(): # add only if char is alphabetical
            list_char_dictionaries.append(dictionary)
    
    list_char_dictionaries.sort(reverse=True, key=sort_on)
    return list_char_dictionaries