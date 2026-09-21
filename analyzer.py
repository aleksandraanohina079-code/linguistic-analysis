from collections import Counter

with open("data/example.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.lower().split()

word_count = len(words)
unique_words = len(set(words))

word_lengths = [len(word.strip(".,!?")) for word in words]
average_word_length = sum(word_lengths) / len(word_lengths)

frequency = Counter(
    word.strip(".,!?")
    for word in words
)

print("=== NLP TEXT ANALYZER ===")
print()
print("Number of words:", word_count)
print("Number of unique words:", unique_words)
print("Average word length:", round(average_word_length, 2))

print()
print("Most frequent words:")

for word, count in frequency.most_common(10):
    print(word, "-", count)
with open("results/analysis.txt", "w", encoding="utf-8") as file:
    file.write("=== NLP TEXT ANALYZER ===\n\n")
    file.write(f"Number of words: {word_count}\n")
    file.write(f"Number of unique words: {unique_words}\n")
    file.write(f"Average word length: {average_word_length:.2f}\n\n")

    file.write("Most frequent words:\n")

    for word, count in frequency.most_common(10):
        file.write(f"{word} - {count}\n")
