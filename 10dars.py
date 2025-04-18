with open("imtihon.txt", "w") as file:
    n = int(input("Nechta talaba? "))
    for _ in range(n):
        ism = input("Ism: ")
        baho = int(input("Baho: "))
        file.write(f"{ism} {baho}\n")

with open("imtihon.txt", "r") as file:
    lines = file.readlines()

with open("alochilar.txt", "w") as alo_file:
    for line in lines:
        ism, baho = line.strip().split()
        if int(baho) >= 90:
            alo_file.write(f"{ism} - {baho}\n")













import os
from collections import Counter

if not os.path.exists("matn.txt"):
    with open("matn.txt", "w", encoding="utf-8") as f:
        f.write("Salom dunyo. Dasturlash oson. Salom Python. Python yaxshi.")

with open("matn.txt", "r", encoding="utf-8") as file:
    matn = file.read().lower()

sozlar = matn.replace(".", "").split()
jami = len(sozlar)
noyob = len(set(sozlar))
hisob = Counter(sozlar)
eng_kop = hisob.most_common(1)[0]

print(f"Jami so‘zlar soni: {jami}")
print(f"Takrorlanmas so‘zlar: {noyob}")
print(f"Eng ko‘p uchragan so‘z: {eng_kop[0]} ({eng_kop[1]} marta)")









# import os
# import random
#
#
# if not os.path.exists("raqamlar.txt"):
#     with open("raqamlar.txt", "w") as f:
#         for _ in range(100):
#             f.write(str(random.randint(1, 100)) + "\n")
#
#
# with open("raqamlar.txt", "r") as file:
#     sonlar = [int(line.strip()) for line in file]
#
# eng_katta = max(sonlar)
# eng_kichik = min(sonlar)
# ortalacha = sum(sonlar) / len(sonlar)
# juft_yigindi = sum(x for x in sonlar if x % 2 == 0)
#
#
# print(f"Eng katta son: {eng_katta}")
# print(f"Eng kichik son: {eng_kichik}")
# print(f"O‘rtacha: {ortalacha:.2f}")
# print(f"Juft sonlar yig'indisi: {juft_yigindi}")
