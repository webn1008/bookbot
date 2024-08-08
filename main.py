def main():

    def book_bot():
        with open("books/Frankenstein.txt") as f:
            file_contents = f.read()
        print(file_contents)

    def word_count(string):
        with open("books/Frankenstein.txt") as f:
            file_contents = f.read()
        words = file_contents.split()
        print(len(words))

    def character_count():
        char_dict = {}

        with open("books/Frankenstein.txt") as f:
            file_contents = f.read()

        for char in file_contents:
            lower_case_char = char.lower()
            if lower_case_char.isalpha():
                if lower_case_char in char_dict:
                    char_dict[lower_case_char] += 1
                else:
                    char_dict[lower_case_char] = 1
        return char_dict

    char_list = []
    char_list.append(character_count())
    char_list.sort(reverse=True)
    print(char_list)
    # book_bot()
    word_count('string')
    character_count()

main()