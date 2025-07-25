matn = input("Matn kiriting: ")
sozlar = matn.split()  # So‘zlarni bo‘lib olish uchun split()
lugat = {}
for soz in sozlar:
    if soz in lugat:
        lugat[soz] += 1
    else:
        lugat[soz] = 1
print(lugat)




foydalanuvchi = {"ism": "Ali", "yosh": 20, "shahar": "Andijon"}
foydalanuvchi["yosh"] = 21
foydalanuvchi.pop("shahar")
print(foydalanuvchi)




royxat = [1, 2, 2, 3, 4, 4, 5]
noyob_qiymatlar = set(royxat)
print(noyob_qiymatlar)


