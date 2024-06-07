student={'john':['java','NodeJs'], 'bill':['python', 'react','AWS'], 'thomas':['python', 'spring']}
name=student.keys()
#course=student.values()

for i in name:
    print("course taken by", i, "are: ")
    for course in student[i]:
            print(course)




