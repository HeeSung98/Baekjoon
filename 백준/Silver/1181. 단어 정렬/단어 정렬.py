n = int(input())
words = [input().strip() for _ in range(n)]

sorted_words = sorted(set(words), key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)