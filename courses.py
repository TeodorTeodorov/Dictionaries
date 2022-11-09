course_dicts = {}
while True:
    command = input()
    if command == "end":
        break

    course, name = command.split(" : ")
    if course not in course_dicts.keys():
        course_dicts[course] = []
        course_dicts[course].append(name)
    else:
        course_dicts[course].append(name)

for course in course_dicts:
    print(f"{course}: {len(course_dicts[course])}")
    for i in range(len(course_dicts[course])):
        print(f"-- {course_dicts[course][i]}")
