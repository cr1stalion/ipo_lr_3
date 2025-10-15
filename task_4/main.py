import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

D = b * b - 4 * a * c

if D > 0:
    print("У данного уравнения два корня")
    result_1 =( -b - math.sqrt(D)) / 2 * a
    print(f"Первый корень {result_1}")
    result_2 =( -b + math.sqrt(D)) / 2 * a
    print(f"Второй корень {result_2}")

elif D == 0:
    print("У данного уравнения один корень")
    result = -b / 2 * a
    print(f"Корень {result}")
else:
    print("У данного уравнения нет корней")