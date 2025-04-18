def numbers(a, b):
    return a + b

a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
print("Natija:", numbers(a, b))






def palindrome(matn):
    return matn == matn[::-1]

s = input("Matn kiriting: ")
print("Palindrome:", palindrome(s))






def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("n ni kiriting: "))
print(f"Natija: ", factorial(n))

