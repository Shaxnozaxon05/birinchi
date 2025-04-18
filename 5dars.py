for son in range(10, 101, 2):
    print(son, end=", ")




son = 0
while son <= 0:
    son = int(input("Musbat son kiriting: "))
    if son <= 0:
        print("Xato! Musbat son kiriting.")
print(f"Musbat son kiritildi: {son}")







for i in range(1, 6):         # Tashqi sikl (qatorlar)
    for j in range(1, 6):     # Ichki sikl (ustunlar)
        print(i * j, end="\t")
    print()  # Har qatordan keyin yangi qator
