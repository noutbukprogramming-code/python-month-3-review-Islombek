try:
    with open("matn.txt", "r") as f:
        matn = f.read()
    
    sozlar = matn.split()
    print(f"So'zlar soni: {len(sozlar)}")

except FileNotFoundError:
    print("Xatolik: matn.txt fayli topilmadi!")
