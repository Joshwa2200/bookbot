def character_count (frankenstein_txt):
    character_count= {}
    for character in frankenstein_txt:
        if character in character_count:
            character_count[character] +=1
        else:
            character_count[character]=1
    return character_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    character_counts=character_count(file_contents)
    print (character_counts)

if __name__ == "__main__":
    main()