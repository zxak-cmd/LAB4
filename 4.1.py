number=int(input('Введите число:'))
if number%2==0:
    print(f'Число {number}-четное')
else:
    print(f'Число {number}-нечетное')

number = int(input("Введите число: "))

if number % 3 == 0:
    print(f"Число {number} делится на 3")
else:
    print(f"Число {number} не делится на 3")

number = int(input("Введите число: "))

if number > 0:
    print(f"Число {number} — положительное")
elif number < 0:
    print(f"Число {number} — отрицательное")
else:
    print("Число равно нулю")