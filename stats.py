def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    chars = list(text)
    for char in chars:
        if char.lower() in char_counts:
            char_counts[char.lower()] = char_counts[char.lower()] + 1
        else:
            char_counts[char.lower()] = 1
    return char_counts

def get_sorted_char_list(char_count_dict):
    char_list = []
    chars = list(char_count_dict.keys())
    for char in chars:
        char_list.append({"char": char, "count": char_count_dict[char]})
    def sort_on(items):
        return items["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list