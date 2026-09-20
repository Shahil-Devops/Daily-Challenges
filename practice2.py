#write a program to accept marks of 6 students and display them in a sorted manner 

marks=[]
marks.append(input("Enter the mark of student1: "))
marks.append(input("Enter the mark of student2: "))
marks.append(input("Enter the mark of student3: "))
marks.append(input("Enter the mark of student4: "))
marks.append(input("Enter the mark of student5: "))
marks.append(input("Enter the mark of student6: "))

marks.sort()

print(marks)
print("Student1: \t"+ marks[0])