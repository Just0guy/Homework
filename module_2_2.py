first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите Третье число: "))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third and first != third:
    print(0)
else:
    print("Ой братка чет не шариш ты за матан")
