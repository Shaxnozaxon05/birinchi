balance = 1000

print("Pul yechish tizimiga hush kelibsiz")

try:
    amount = float(input("Qancha pul yechmoqchisiz?"))
    if amount <= 0:
        raise ValueError("Pul miqdori manfiy yoki 0 bo'lmasligi kerak.")
    if amount > balance:
        raise ValueError("Hisobda yetarli mablag' yo'q")

    balance -= amount
    print(f"{amount} so'm hisobdan yechildi. Joriy balans: {balance} so'm.")

except ValueError as e:
    print(f"Xatolik: {e}")

finally:
    print(f"Jarayon tugadi. Joriy balans: {balance} so'm")