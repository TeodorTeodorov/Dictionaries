company_dict = {}
while True:
    command = input()
    if command == "End":
        break
    company, id = command.split(" -> ")

    if company not in company_dict:
        company_dict[company] = []
        company_dict[company].append(id)
    else:
        if id in company_dict[company]:
            continue

        company_dict[company].append(id)



for company in company_dict:
    print(f'{company}')
    for i in range(len(company_dict[company])):
        print(f"-- {company_dict[company][i]}")