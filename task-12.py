sonlar = list(map(int, input().split()))

juft_sonlar = list(filter(lambda son: son % 2 == 0, sonlar))
kvadratlari = list(map(lambda son: son ** 2, juft_sonlar))

print("Juft sonlar:", juft_sonlar)
print("Kvadratlari:", kvadratlari)
