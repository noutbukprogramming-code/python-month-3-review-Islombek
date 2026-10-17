print("sonlarni kiriting: ")
sonlar=list(map(int,input().split()))

musbat =[]
manfiy=[]
nollar =0

for son in sonlar:
    if son>0:
        musbat.append(son)
    elif son<0:
        manfiy.append(son)
    else:
        nollar+=1

print(f"musbat soni: {musbat}")
print(f"manfiy soni: {manfiy}")
print(f"nollar soni: {nollar}")
