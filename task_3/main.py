day = int(input("Введите день: ")) #  Заправшиваем день
months = int(input("Введите месяц: ")) # Запрашиваем месяц

if months >= 3 and months <= 5 and day >= 1 and day <= 31: # Проверяем число и дату на весну
    print("Весна") 
elif months >= 6 and months <= 8 and day >= 1 and day <= 31: # Проверяем число и дату на лето
    print("Лето")
elif months >= 9 and months <= 11 and day >= 1 and day <= 30: # Проверяем число и дату на осень
    print("Осень")
elif months == 12 or months == 1 and day >= 1 and day <= 31: # Проверяем число и дату на зиму(декабрь, январь)
    print("Зима")
elif months == 2 and day >= 1 and day <= 28: # Проверяем на ферваль
    print("Зима")
else:
    print("Нет такой даты") # Если введена неверная дата