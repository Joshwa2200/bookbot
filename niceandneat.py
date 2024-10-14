def character_count (frankenstein_txt):
    character_count= {}
    for character in frankenstein_txt:
        if character in character_count:
            character_count[character] +=1
        else:
            character_count[character]=1
    return character_count

def wordcount (frankenstein_txt):
    word_count=0
    words= frankenstein_txt.split ()
    for word in words:
        word_count += 1
    return (word_count)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    character_counts=character_count(file_contents)

    word_count = wordcount(file_contents)

    characters= list (character_counts.keys())

    counts_of_characters= list (character_counts.values())

    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_characters:
        organized_characters=(f"The '{char}' character was found {count} times")
        return organized_characters   
    
    print(f" ---Begin Report of Frankenstein--- This book contains {word_count} words, and {organized_characters} ---End Report---")
if __name__ == "__main__":
    main()