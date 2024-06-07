
def average_mark(marks):
    sum_of_marks = sum(marks)
    total_subject = len(marks)
    average_of_mark = sum_of_marks/total_subject
    return average_of_mark

marks = [54,76,56,73]
n=average_mark(marks)
print(n)

def grade(n):
    if n >= 80:
        grade = "A"
    elif n >= 60:
        grade = "B"
    elif n >= 50:
        grade = "C"
    else:
        grade = "D"
    return grade
grade_received = grade(n)
print(grade_received)


