def yasash_invoice():
    mahsulotlar = []
    jami = 0

    print("Hisob-faktura tuzish dasturiga xush kelibsiz!")
    while True:
        nomi = input("Mahsulot nomi (yoki 'exit' tugatish uchun): ")
        if nomi.lower() == 'exit':
            break
        try:
            narxi = float(input(f"{nomi} narxi (so'm): "))
            miqdori = int(input(f"{nomi} miqdori (dona): "))
        except ValueError:
            print("Iltimos, sonda kiriting.")
            continue

        summa = narxi * miqdori
        mahsulotlar.append((nomi, narxi, miqdori, summa))
        jami += summa

    print("\n====== HISOB-FAKTURA ======")
    print(f"{'Mahsulot':<20} {'Narxi':<10} {'Miqdori':<10} {'Summa':<10}")
    print("-" * 60)
    for nomi, narxi, miqdori, summa in mahsulotlar:
        print(f"{nomi:<20} {narxi:<10.2f} {miqdori:<10} {summa:<10.2f}")
    print("-" * 60)
    print(f"{'Jami':<42} {jami:.2f} so'm")
    print("===========================\n")


# Dastur ishga tushuriladi
yasash_invoice()




