def count_words(text):
    words = text.split()
    total_words = len(words)
    return total_words



def count_characters(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else: 
            char_count[lowercase_char] = 1
    return char_count



        