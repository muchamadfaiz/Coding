# Find the most repeated character in this text
# Percobaan 1
sentence = "This is a common interview question"
# unique = set(sentence)
# print(unique)

# sentence2 = []
# unique2 = list(sentence)
# print(unique2)
# len(unique2)

# Percobaan 2
# using data structure (Dict) because it has key and values, so use the character as key and repetition as values
char_frequency = {} # first we set an empty dictionary
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
char_frequency.items(),
key=lambda kv: kv[1], 
reverse=True)
print(char_frequency_sorted[0])





