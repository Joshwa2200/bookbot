def wordcount (frankenstein_txt):
    word_count=0
    words= frankenstein_txt.split ()
    for word in words:
        word_count += 1
    return (word_count)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = wordcount(file_contents)
    print("The word count is:", word_count)

if __name__ == "__main__":
    main()