def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import count_words, count_characters

def main():
    
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    char_count = count_characters(text)
    
    # print(text)
    print(f"Found {num_words} total words")
    print(char_count)
    
main()   