def main():
    book_path = "books/Frankenstein.txt"
    file_contents = book_bot(book_path)
    num_words = word_count(file_contents)
    chars_dict = get_chars_dict(file_contents)
    chars_list_sorted = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_list_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- end report ---")



def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    char_list = []
    for ch in num_chars_dict:
        char_list.append({"char":ch, "num": num_chars_dict[ch]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def get_chars_dict(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def book_bot(path):
    with open(path) as f:
        return f.read()

main()