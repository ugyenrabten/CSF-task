def count_chars(string, character):
    count = string.count(character)
    return count

#example
string = "hello world"
character = "o"
char_count = count_chars(string, character)
print("the character", character,"appears",char_count, "times in the string.")