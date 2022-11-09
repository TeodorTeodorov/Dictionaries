contest_passwords = {}
submissions = {}
while True:
    command1 = input()
    if command1 == "end of contests":
        break
    contest, password = command1.split(":")

    contest_passwords[contest] = password

print(contest_passwords)

while True:
    command2 = input()
    if command2 == "end of submissions":
        break
    contest2, password, username, points = command2.split("=>")
    if contest2 not in submissions:
        if contest2 in contest_passwords and password in contest_passwords.values():
            submissions[contest2] = []
            submissions[contest2].append(password)
            submissions[contest2].append(username)
            submissions[contest2].append(int(points))
    else:
        if int(points) > submissions[contest2][2]:
            submissions[contest2].append(int(points))
print(submissions)
total = 0
for name in submissions.values():
    total += submissions[command2][2]
    print(total)