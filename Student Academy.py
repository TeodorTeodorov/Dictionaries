students_grades = {}
number = int(input())
for num in range(number):
    name = input()
    grades = float(input())
    if name not in students_grades:
        students_grades[name] = []
        students_grades[name].append(grades)
    else:

        students_grades[name].append(grades)

for name in students_grades:
    sum_grades = sum(students_grades[name]) / len(students_grades[name])
    if sum_grades >= 4.5:
        print(f"{name} -> {sum_grades:.2f}")