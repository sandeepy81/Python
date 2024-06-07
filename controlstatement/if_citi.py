#Using following list of cities per country,
#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]
#Write a program that asks user to enter a city name and it should tell which country the city belongs to
#Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

citi1 = input("Enter a citi1 name: ")
citi2 = input("Enter a citi2 name: ")

if citi1 in india and citi2 in india:
    print(f"Both {citi1} and {citi2} are in india")
elif citi1 in pakistan and citi2 in pakistan:
    print(f"Both {citi1} and {citi2} ae are in pakistan")
elif citi1 in bangladesh and citi2 in bangladesh:
    print(f"Both {citi1} and {citi2} ae are in bangladesh")
else:
    print("They don't belong to same country")