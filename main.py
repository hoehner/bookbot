import sys
from stats import get_word_count, get_char_counts, get_sorted_char_list

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
    
def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(path)
    count = get_word_count(text)
    char_dict = get_char_counts(text)
    sorted_char_dict = get_sorted_char_list(char_dict)        
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}...')
    print("----------- Word Count ----------")
    print(f'Found {count} total words')
    print("--------- Character Count -------")
    for element in sorted_char_dict:
        if element["char"].isalpha():
            print(element["char"] + ": " + str(element["count"]))


main()