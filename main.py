import string


def book_bot():

    def main():
        with open("books/Frankenstein.txt") as f:
            file_contents = f.read()
        print(file_contents)

    def word_count(string):
        with open("books/Frankenstein.txt") as f:
            file_contents = f.read()
        words = file_contents.split()
        print(len(words))
    main()
    word_count('string')

book_bot()