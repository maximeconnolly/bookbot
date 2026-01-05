import sys
from stats import get_num_words, get_character_from_text, sort_print_character_from_text
if len(sys.argv) <= 1: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]

print(filepath)
print(f"Found {get_num_words(filepath)} total words")
sort_print_character_from_text(filepath)