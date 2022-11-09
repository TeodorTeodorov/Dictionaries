name_score = {}
submissions_count = {}
while True:
    lines = input()
    if lines == "exam finished":
        break
    if "banned" in lines:
        username, command = lines.split("-")
        if username in name_score:
            del name_score[username]

    else:
        username, language, points = lines.split("-")

        if username not in name_score:
            name_score[username] = []
            name_score[username].append(language)
            name_score[username].append(int(points))
        else:
            if int(points) > name_score[username][1]:
                name_score[username].append(int(points))

        if language not in submissions_count:
            submissions_count[language] = []
            submissions_count[language].append(points)
        else:
            submissions_count[language].append(points)

print(f"Results:")
for username in name_score:
    print(f"{username} | {name_score[username][1]}")
print("Submissions:")
for language in submissions_count:
    print(f"{language} - {len(submissions_count[language])}")