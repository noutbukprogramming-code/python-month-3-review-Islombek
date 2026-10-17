words = input("So'zlarni kiriting: ").split()

count_words = {} 
for key in words:
    count_words[key] = count_words.get(key, 0) + 1

print(count_words)
