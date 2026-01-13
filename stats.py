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

def sort_on(items):
    return items["num"]

def sorted_list(char_count):

    items_list = []

    for char, count in char_count.items():
        items = {"char": char, "num": count}
        items_list.append(items)
    
    items_list.sort(reverse=True, key=sort_on)
    return items_list



        