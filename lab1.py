a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

sum_ = a + b
print("Сумма чисел:", sum_)

diff = a - b
print("Разность чисел:", diff)

product = a * b
print("Произведение чисел:", product)

average = (a + b) / 2
print("Среднее арифметическое чисел:", average)

max_abs = max(abs(a), abs(b))
min_abs = min(abs(a), abs(b))
abs_diff = max_abs - min_abs

print("Разность максимального и минимального по модулю:", abs_diff)

quotient = round(a / b, 2)
print("Частное чисел:", quotient)
