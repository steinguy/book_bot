import sys

def check_argv(args):
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return args[1]
        

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

from stats import count_words, count_characters, sorted_list



def main():
    path = check_argv(sys.argv)
    text = get_book_text(path)

    num_words = count_words(text)
    char_count = count_characters(text)
    sorted_chars = sorted_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

    print("============= END ===============")
    
    # print(text)
    #print(f"Found {num_words} total words")
    #print(char_count)
    
if __name__ == "__main__":
    main()