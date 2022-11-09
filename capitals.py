country_names = input().split(", ")
capital_cities = input().split(", ")
output = {country_names[index]: capital_cities[index] for index in range(len(country_names))}
for country_names, capital_cities in output.items():
    print(f"{country_names} -> {capital_cities}")


# country_names = input().split(", ")
# capital_cities = input().split(", ")
# result = list(zip(country_names, capital_cities))