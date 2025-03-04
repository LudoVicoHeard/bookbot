def word_count(text):
    word_list = text.split()
    return len(word_list)

def char_counts(text):
    char_list = list(text.lower())
    char_dict = {}
    for char in char_list:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sorted_alpha_chars(input):
    sorted_chars = sorted(input.items(), key=lambda x: x[1], reverse=True)
    return sorted_chars