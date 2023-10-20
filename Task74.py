def reverse_words(input_string):
    words = input_string.split('')
    reversed_words =  ' '.join(reversed_words)
    return reversed_words
input_string = "hello, how are you?"
reverse_string = reverse_words(input_string)
print(reverse_string)   # outputs: "you? are how hello"