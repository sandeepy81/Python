#Handle employee details

n = int(input("Enter a number of employee: "))
employee = {}
for i in range(n):
    name = input("Enter the employee name:")
    salary = input("Enter the employee salary:")
    employee[name]=salary
while True:
    name = input("Enter the emp name:")
    salary = employee.get(name, -1)
    if salary == -1:
        print("Employee does not exist")
    else:
        print("The salary of the employee is:", salary)
    choice = input("Do you want to know the salary of other emp [Yes|No]:")
    if choice == 'No':
        break
