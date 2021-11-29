

students_grades=[]

for _ in range(4):
    name = ['a', 'b', 'c', 'd']
    score =[50, 2000, 35, 3]
    students_grades.append([name[_],score[_]])

print(students_grades)

# sorted: deixa em ordem
# list: transforma em lista
# set: tira elementos repitidos
# [x[1]]: score
sorted_scores = sorted(list(set([x[1] for x in students_grades])))
print(sorted_scores)

print("-----------------------------------------------------")

second_lowest = sorted_scores[1]


low_final_list = []
for student in students_grades:
    if second_lowest == student[1]:
        low_final_list.append(student[0])
        

for student in sorted(low_final_list):
    print(student)




