sonlar = list(map(int, input().split()))

juftlar = list(filter(lambda son: son % 2 == 0, sonlar))
kvadrati = list(map(lambda son: son ** 2, juftlar))

print("Juft sonlar:", juftlar)
print("Kvadratlari:", kvadrati)
