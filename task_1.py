words = input("Enter words, separated by space: ").split()
print(*[word[:10] if len(word) > 2 else word for word in enumerate(words, start=1)], sep="\n")