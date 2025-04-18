def full_name(ism, familiya="Familiyasi yo‘q"):
    print(f"{ism} {familiya}")

full_name("Ali")
full_name("Ali", "Valiyev")








def shape_area(shape, **kwargs):
    if shape == "kvadrat":
        a = kwargs.get("a", 0)
        return a * a
    elif shape == "to'g'ri to'rtburchak":
        a = kwargs.get("a", 0)
        b = kwargs.get("b", 0)
        return a * b
    else:
        return "Bunday shakl qo'llab-quvvatlanmaydi"

print(shape_area("kvadrat", a=4))
print(shape_area("to'g'ri to'rtburchak", a=4, b=5))









def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

print(sum_to_n(5))

