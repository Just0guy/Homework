my_fruits = ['Banana','Apple','Mango','Melon','Peach'] # Спиок с переменными
print(my_fruits) # вывожу
print(my_fruits[0]) # Вывожу первый элемент
print(my_fruits[-1]) # Вывожу последний элемент
print([my_fruits[2:5]]) # Вывожу с 3 до 5
my_fruits[2] = 'Cherry' # меняю 3 элемент
print(my_fruits) # Вывожу новый список с изменениями

my_translate = {'Banana':'Банан','Apple':'Яблоко','Mango':'Манго','Melon':'Дыня',
                'Peach':'Мой сладкий Пэрсссик'} #Присваиваю Словарь
print(my_translate) #Вывожу Словарь
print(my_translate['Peach']) #Значение от задоного ключа
my_translate['Peach'] = 'Персик' # Меняю значения для заданого ключа, убираю кавказкий акцент =(
print(my_translate) #Вывожу Словарь после редактирования