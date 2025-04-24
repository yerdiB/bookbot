def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_chars(text):
    lowered_text = text.lower()
    char_count = {}
    words_list = lowered_text.split()
    for word in words_list:
        for char in word:
            if char not in char_count and char.isalpha():
                char_count[char] = 1
            elif char.isalpha():
                char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    sorted_list = []
    for char, num in dict.items():
        sorted_list.append({"char" : char, "num" : num})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list