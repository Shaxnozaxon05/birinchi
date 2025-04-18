matn = str(input("Matn kiriting:"))
print(len(matn))
print(matn.upper())
print(matn.lower())



ism = (input("Ismingiz:"))
familya = (input("Familyangiz:"))
yil = int(input("Tug'ilgan yilingiz:"))
print(f"Sizning shaxsiy profilingiz: \n Ism: {ism} \n Familya: {familya} \n Tug'ilgan yil: {yil} \n Yosh: {2025-yil}")



matn = input("Matnni kiriting: ")
sozlar = matn.split()
sozlar_soni = len(sozlar)
eng_uzun_soz = max(sozlar, key=len)
uzunlik = len(eng_uzun_soz)

print("So‘zlar soni:", sozlar_soni)
print(f"Eng uzun so‘z: {eng_uzun_soz} ({uzunlik} ta harf)")






