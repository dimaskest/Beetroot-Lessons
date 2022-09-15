string = input("Enter your sentence: ").lower()
counted_words = {}

for word in string.split():
    counted_words.setdefault(word, 0)
    counted_words[word] += 1

print(counted_words)