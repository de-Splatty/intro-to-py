# strings
sentence = "The quick brown fox jumps over the lazy dog."
# builtin functionality
#funnctions
print(sentence)
print(sentence.upper()) # call a function
print(sentence.lower())
print(sentence.title())
print(sentence.count('dog'))
print(sentence.isspace())

sentence = " "
if sentence.isspace() or sentence.isdigit() or sentence.isnumeric():
    print("Invalid name")
else:
    print("Valid name")