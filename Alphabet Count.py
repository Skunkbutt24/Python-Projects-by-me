import string
print("Welcome to the Alphabet Frequency Counter!")
print("Enter a passage, and the program will count the occurrences of each letter (A-Z).")
passage = input("Please enter a passage:\n ")
upper_passage=passage.upper()
letters=string.ascii_uppercase
char_counts = {}
words=passage.split()
longest_word = max(words, key=len)
shortest_word = min(words, key=len) 
word_count=len(words)
uppercase=0
lowercase=0
numbers=0
symbols=0
vowels="AEIOU"
vowels_count=0
consonants_count=0
for char in letters:
    char_counts[char] = 0
for char in upper_passage:
    if char in char_counts:
        char_counts[char] += 1
        if char.isalpha():
            if char in vowels:
                vowels_count+=1
            else:
                consonants_count+=1
print("Character Frequency Count:")
for char in letters:
    print(f"{char} = {char_counts[char]}")
print(f"Total Words: {word_count}")
for char in passage:
    if char.isupper():
        uppercase+=1
    elif char.islower():
        lowercase+=1
    elif char.isdigit():
        numbers+=1
    elif char in string.punctuation:
        symbols+=1
print(f"Total Uppercase: {uppercase}")
print(f"Total Lowercase: {lowercase}")
print(f"Total Numbers: {numbers}")
print(f"Total Symbols: {symbols}")
print(f"Total Vowels: {vowels_count}")
print(f"Total Consonants: {consonants_count}")
print(f"The longest word is: {longest_word}")
print(f"The shortest word is: {shortest_word}")
