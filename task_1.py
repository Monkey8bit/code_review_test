words = input("Enter words, separated by space: ").split()
print(*[(row, word[:10]) if len(word) > 10 else (row, word) for row, word in enumerate(words, start=1)], sep="\n")
