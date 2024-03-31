def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_of_words = get_num_words(file_contents)
    char_freq = get_char_count(file_contents)
    char_list = char_dict_to_list(char_freq)
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document")
    print()

    for char in char_list:
        print(f"The '{char["char"]}' character was found {char["freq"]} times")


def sort_on(dict):
    return dict["freq"]


def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    dict = {}
    for char in text:
        if char.isalpha():
            if char.lower() in dict:
                dict[char.lower()] += 1
            else:
                dict[char.lower()] = 1
    return dict


def char_dict_to_list(char_dict):
    result = []
    for key in char_dict:
        result.append({"char": key, "freq": char_dict[key]})
    return result


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
