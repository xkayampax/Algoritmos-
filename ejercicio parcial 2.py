phrases = [
    "Hola todos",
    "HOLA AMIGO",
    "todos en grupo",
    "python es facil",
    "Hola mundo"
]

word_count = {}

for phrase in phrases:
    words = phrase.lower().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

top_words = []
for word, count in word_count.items():
    if len(top_words) < 3:
        top_words.append((word, count))
    else:
        for i in range(len(top_words)):
            if count > top_words[i][1]:
                top_words.insert(i, (word, count))
                if len(top_words) > 3:
                    top_words.pop()
                break

print("Top 3 most frequent words:")
for word, count in top_words:
    print(word, count)