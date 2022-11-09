info = input().split(":")
output = {}
while len(info) > 1:
    name, id, course = info[0], info[1], info[2]
    if course not in output.keys():
        output[course] = []
    output[course].append(f"{name} - {id}")
    info = input().split(":")
searched_cours = info[0].replace("_"," ")
for student in output[searched_cours]:
    print(student)