# Looping over list
letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)


# for letter in enumerate(letters):
#     print(letter[0])

# for letter in enumerate(letters):
#     print(letter[1])

for index, letters in enumerate(letters):
    print(index, letters)