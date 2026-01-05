from collections import Counter

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(filepath):
    text = get_book_text(filepath)
    return len(text.split())

def get_character_from_text(filepath):
    text = get_book_text(filepath)
    text = text.lower()
    return dict(Counter(text))

def sort_print_character_from_text(filepath):
    text = get_book_text(filepath)
    text = text.lower()
    text_dict = dict(Counter(text).most_common())
    for text in text_dict:
        print(f"{text}: {text_dict[text]}")
