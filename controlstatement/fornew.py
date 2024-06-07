# Print square of number between 1 to 5 except even number
'''for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)'''

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
print("\nExercise 3\n")
month_list = ["January", "February", "March", "April", "May"]
exp = [2340, 2500, 2100, 3100, 2980]
n = int(input("Enter expense amount: "))

month = -1
for i in range(len(exp)):
    if n == exp[i]:
        month = i
        break

if month != -1:
    print(f'You spent {n} in {month_list[month]}')
else:
    print(f'You didn\'t spend {n} in any month')
