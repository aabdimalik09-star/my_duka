# list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# filter words by length
words = ["apple", "mango", "kiwi", "egg", "cherry", "bread", "me"]

long_words = [word for word in words if len(word) >= 5]
print(long_words)
# Output: ['apple', 'mango', 'cherry', 'bread']