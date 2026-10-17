print("Son kiriting: ")
sonlar = list(map(int,input().split()))

juft = 0
toq = 0

for son in sonlar:
    if son % 2 == 0:
        juft += 1
    else:
        toq += 1

print(f"Juft sonlar: {juft}")
print(f"Toq sonlar: {toq}")
