grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #База оценок студентов по алфавиту
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'} #Список студентов не по алфавиту
Sorted_students = sorted(students) #Сортируем студентов
Average_score = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]), #Считаем средний балл
                 sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
Final_exam_results = {Sorted_students[0]:Average_score[0],Sorted_students[1]:Average_score[1], #Формируем списки студент + оценки
                      Sorted_students[2]:Average_score[2],Sorted_students[3]:Average_score[3],Sorted_students[4]:Average_score[4],}
print(Final_exam_results) #Выводим результат студентов

print('______________________Разделительный пробел между вариантами подсчёта______________________')

#Но реальноть она не такая, количество оценов у всех разное значит кто от не явилься либо не сдал придмет
# и средний балл болжен считаться на основание всех придметов, то есть надо вычеслить по максимальному количеству оценок
# сколько было предметов и разделить на него что бы вычеслить реальный средний баллv

grades_2 = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #База оценок студентов по алфавиту
students_2 = {'Johnny','Bilbo','Steve','Khendrik','Aaron'} #Список студентов не по алфавиту
Sorted_students_2 = sorted(students) #Сортируем студентов
Quantity_Grads = [len(grades_2[0]),len(grades_2[1]),
                  len(grades_2[2]),len(grades_2[3]),len(grades_2[4])] # формируем новый список где считаем длину какждого ученика
# для того что бы понять сколько предметов было
Max_Grads = max(Quantity_Grads) #Находим в списке Quantity_Grads максимальное значение
Average_score_2 = [sum(grades_2[0])/Max_Grads,sum(grades_2[1])/Max_Grads, #Считаем средний балл оценок на основание максимального значения
                 sum(grades_2[2])/Max_Grads,sum(grades_2[3])/Max_Grads,sum(grades_2[4])/Max_Grads]
Final_exam_results_2 = {Sorted_students_2[0]:Average_score_2[0],Sorted_students_2[1]:Average_score_2[1], #Формируем списки студент + оценки v2.0
                      Sorted_students_2[2]:Average_score_2[2],Sorted_students_2[3]:Average_score_2[3],Sorted_students_2[4]:Average_score_2[4],}
print(Final_exam_results_2) #Выводим результат студентов v2.0