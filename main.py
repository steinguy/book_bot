def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import count_words

def main():
    
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(path)
    
    # print(text)
    print(f"Found {num_words} total words")
    
main()   