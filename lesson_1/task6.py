
# Задание 6

a = input('Введите число a (рассотояние в км, которое пробежал спорстмен в первый день)\n')
b = input('Введите число b (интересующее нас рассотояние в км)\n')

a = float(a)
b = float(b)

current_km = a
day = 1

while current_km < b:
    print(f"{day}'й день: {current_km:.2f}")
    current_km *= 1.1
    day += 1
else:
    print(f"{day}'й день: {current_km:.2f}")

print(f"На {day}'й день результат спортсмена достиг результата - не менее {b:.2f} км")
