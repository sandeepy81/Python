## Exercise: Python If Condition
# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

level=int(input("Enter your fasting suger level:"))

if level<80:
    print("Your suger level is low, eat some sweet")

elif level>100:
    print("Your suger level is high, stop eating sweet and do excercise")

else:
    print("Your suger level is in control, enjoy life")





