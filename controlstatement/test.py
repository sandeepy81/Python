'''Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message'''

for i in range(5):
    print(f"You ran {i+1} miles")
    tired = input("Are you tired?: ")
    if tired == "yes":
        print("you did not finish the race")
        break
    if i == 4:
        print("You just finished 5Km race")




