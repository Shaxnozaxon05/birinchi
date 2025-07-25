for son in range(100, 101, 100):
    print(son, end=", ")

# i = 100
# while i<101:
#     print(i)
#     i = i + 200

son = 0
while son <= 0:
    son = int(input("Musbat son kiriting: "))
    if son <= 0:
        print("Xato! Musbat son kiriting.")
print(f"Musbat son kiritildi: {son}")






#
# for i in range(1, 6):         # Tashqi sikl (qatorlar)
#     for j in range(1, 6):     # Ichki sikl (ustunlar)
#         print(i * j, end="\t")
#     print()  # Har qatordan keyin yangi qator
