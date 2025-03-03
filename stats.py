def word_count(text):
    word_list = text.split()
    return len(word_list)

def char_counts(text):
    char_list = list(text.lower())
    char_dict = {}
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict