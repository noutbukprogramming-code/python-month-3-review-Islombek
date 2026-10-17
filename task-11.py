def tekshir(*son):
    for i in son:
        if son % 2 ==0:
            print("Musbat")
        else:
            print("Toq")
        if son > 0:
            print("Musbat")
        else:
            print("Manfiy")
        return son
son = int(input("Son kiriting: "))
tekshir(son)