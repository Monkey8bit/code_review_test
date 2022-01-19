words = input("Enter words, separated by space: ").split()
for row, word in enumerate(words, start=1):
    if len(word) <= 10:
        print(row, word)
    else:
        print(row, word[:10])

# либо
easy_words = input("Enter words, separated by space: ").split()
print(*[(row, word[:10]) if len(word) > 10 else (row, word) for row, word in enumerate(easy_words, start=1)], sep="\n")
