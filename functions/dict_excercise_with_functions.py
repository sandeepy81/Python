
'''We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21
 1. Using above create a dictionary of countries and its population
2. Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21

add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.'''

population = {
    "china":143,
    "india":136,
    "usa":32,
    "pakistan":21
}

def add():
    country=input("Enter the country to add: ")
    country=country.lower()
    if country in population:
        print("Country already exist in the dict. Do nothing")
        return
    p=float(input(f"Enter the population of {country}"))
    population[country]=p    # add new key value pair in to dict
    print_all()

def remove():
    country=(input("Enter the country name you want to remove: "))
    country=country.lower()
    if country not in population:
        print("Country doesn't exist")
        return
    del population[country]

def query():
    country=input("Enter the country name which you want to query: ")
    country=country.lower()
    if country not in population:
        print("Country does not exist in database. Terminating")
        return
    print(f"Population of {country} is: ")

def print_all():
    for country, p in population.item():
        print(f"{country}=={p}")








    








