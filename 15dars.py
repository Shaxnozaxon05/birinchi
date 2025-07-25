with open("raqamlar.txt", "r") as file:
    sonlar = [int(line.strip()) for line in file]

eng_katta = max(sonlar)
eng_kichik = min(sonlar)
ortacha = sum(sonlar) / len(sonlar)


with open("results.txt", "w") as output:
    output.write(f"Eng katta son: {eng_katta}\n")
    output.write(f"Eng kichik son: {eng_kichik}\n")
    output.write(f"O'rtacha qiymat: {ortacha:.2f}\n")
