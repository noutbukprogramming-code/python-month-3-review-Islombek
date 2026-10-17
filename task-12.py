sonlar = list(map(int, input("Sonlar: ").split()))

juftlar = list(filter(lambda son: son % 2 == 0, sonlar))
kvadrati = list(map(lambda son: son ** 2, juftlar))

print(f"Juft sonlar: {juftlar}")
print(f"Kvadratlari: {kvadrati}")
