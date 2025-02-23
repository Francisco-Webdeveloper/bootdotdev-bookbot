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