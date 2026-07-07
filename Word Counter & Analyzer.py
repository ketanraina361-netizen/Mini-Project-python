# Word Counter & Analyzer
paragraph = input("Enter a paragraph:  ")

words = paragraph.split()       # Split paragraph into words
word_count = len(words)         # Count total words

longest_word = ""
for word in words:
    # Remove punctuation from beginning/end
    clean_word = word.strip(".,!?;:'\"()[]{}")
    if len(clean_word) > len(longest_word):
        longest_word = clean_word

vowels = "aeiouAEIOU"         #Count vowels
vowel_count = 0

for char in paragraph:
    if char in vowels:
        vowel_count += 1

print("\n---- Analysis ----")
print("Total Words :", word_count)
print("Longest Word :", longest_word)
print("Length of Longest Word :", len(longest_word))
print("Total Vowels :", vowel_count)