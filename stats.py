def count_words(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = len(words)
        return total_words

def count_characters(path):
    with open(path) as f:
        file_contents = f.read()
        