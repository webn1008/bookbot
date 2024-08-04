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

    def character_count(text):
        
        with open("books/Frankenstein.txt") as f:
            char_dict = {}
            file_contents = f.read()
            character_string = file_contents
            lower_case_string = character_string.lower()
            if lower_case_string in char_dict:
                char_dict[lower_case_string] += 1
            else:
                char_dict[lower_case_string] = 1
        return char_dict

    book_bot()
    word_count('string')
    character_count('text')

main()