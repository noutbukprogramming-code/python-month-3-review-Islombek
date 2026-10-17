words = input("So'zlarni kiriting: ").split()

count_words = {} 
for soz in words:
    count_words[soz] = count_words.get(soz, 0) + 1
for key, value in count_words.items():
    print(key , value)

