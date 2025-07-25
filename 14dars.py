try:
    a = int(input("a = "))
    b = int(input("b = "))
    natija = a / b
    print("Natija:", natija)
except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas!")
except ValueError:
    print("Xatolik: Faqat son kiriting!")






# import math
#
# try:
#     x = int(input("Son kiriting: "))
#     if x < 0:
#         raise ValueError("Manfiy sonlar qabul qilinmaydi!")
#     print("Ildizi:", math.sqrt(x))
# except ValueError as e:
#     print("Xatolik:", e)








#
# def bolish_roxatdagi_sonlar(royxat):
#     try:
#         if not royxat:
#             raise ValueError("Bo‘sh ro‘yxat!")
#         for son in royxat:
#             if son == 0:
#                 raise ZeroDivisionError("Nolga bo‘lish mumkin emas!")
#             print(f"{son} => {100 / son}")
#     except ValueError as ve:
#         print("Xatolik:", ve)
#     except ZeroDivisionError as ze:
#         print("Xatolik:", ze)
#
# bolish_roxatdagi_sonlar([25, 0, 10])

