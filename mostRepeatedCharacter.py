from pprint import pprint
sentence = input("Enter the string : ")
letters = {}
most_frequency_char = []
for char in sentence.lower():
    letters[char] = letters.get(char, 0) + 1

letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
pprint(letters, width=12)
most_frequency = letters[0][1]
for letter, frequency in letters:
    if frequency == most_frequency:
        most_frequency_char.append(letter)
    else:
        break
print("The most repeated character is ", most_frequency_char)
