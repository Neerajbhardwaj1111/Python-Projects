'''
1. Student Report Card Generator
Concepts: Input/output, lists, dictionaries, loops, conditionals, functions

Features:

Take student name, subjects, and marks

Store in dictionary

Calculate average, grade, pass/fail

Print formatted report card
'''

data = {}
n = int(input(" number of students : "))
for i in range(n):
    stu={}
    name = input("Enter Student Name : ")
    stu['English'] = int(input("Enter English Marks : "))
    stu['Math'] = int(input("Enter Math Marks : "))
    stu['Hindi'] = int(input("Enter Hindi Marks : "))
    stu['SST'] = int(input("Enter SST Marks : "))
    stu['Sci'] = int(input("Enter Science Marks : "))
    

    stu['total_marks'] = stu['English']+stu['Hindi']+stu['Math']+stu['Sci']+stu['SST']
    stu['avg'] =stu['total_marks']/5
    if stu['avg']==100:
        stu['grade'] = "A+"
    elif stu['avg']<100 and stu['avg']>=90:
        stu['grade']="A"
    elif stu['avg']<90 and stu['avg']>=80:
        stu['grade']="B"
    elif stu['avg']<80 and stu['avg']>=70:
        stu['grade']="C"
    elif stu['avg']<70 and stu['avg']>=60:
        stu['grade']="D"
    elif stu['avg']<60 and stu['avg']>=50:
        stu['grade']="E"
    else:
        stu['grade'] ="F"

    stu['final_status'] = "PASS" if stu['avg']>=33.33 else "FAIL"

    data[name] =stu

for ele, details in data.items():
    print("-"*25)
    print(f"REPORT CARD : {ele}")
    print("-"*25)
    for sub,marks in details.items():
        if sub not in ['total_marks', 'avg', 'grade', 'final_status']:
            print(f"{sub:<10}: {marks}")

    print("-"*25)
    print(f"AVG MARKS : {data[ele]['avg']}")
    print(f"GRADE : {data[ele]['grade']}")
    print(f"STATUS : {data[ele]['final_status']}")
    print("-"*10)

