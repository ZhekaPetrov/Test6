# Write a program that reads one number from the keyboard and outputs the opposite to it. If the number entered from the keyboard is zero,
# then print "There is no inverse number" (without quotes).

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль,
# то вывести «Обратного числа не существует» (без кавычек).

a = float(input())
if a == 0:
    print("Обратного числа не существует")
else:
    print(1 / a)
    
# The famous American writer Ray Bradbury has a novel "Fahrenheit 451". Write a program that defines,
# which temperature on the Celsius scale corresponds to the specified value on the Fahrenheit scale.
    
# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу, которая определяет,
# какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

F = float(input())
c = 5 / 9 * (F - 32)
print(c)

# The input to the program is the number nn – the number of dog years. Write a program that calculates the age of a dog in human years.
# На вход программе подается число nn – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.

n = float(input())
if n == 1:
    print("10.5")
elif n == 2:
    print("21")
elif n > 2:
    print(21 + (n - 2) * 4)
    
# Given a positive real number. Print its first digit after the decimal point.
# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
a = float(input())
n = a * 10
m = int(n)
c = m % 10 
print(c)

# or (или)
    
x = float(input())
print(int(x * 10) % 10)

# Given a positive real number. Output its fractional part.
# Дано положительное действительное число. Выведите его дробную часть.

a = float(input())
print(a - (int(a)))

# Write a program that finds the smallest and largest of the five numbers.
# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.

a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
x = min(a, b, c, d, e)
y = max(a, b, c, d, e)
print("Наименьшее число =", (int(x)))
print("Наибольшее число =", (int(y)))

# Write a program that orders three numbers from larger to smaller.
# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())
x = max(a, b, c)
z = min(a, b, c)
y = (a + b + c) - (x + z)
print(x)
print(y)
print(z)
