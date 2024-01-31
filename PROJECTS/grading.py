student_score ={
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

Student_grade = {}

for keys in student_score:
    score = student_score[keys]
    if score > 90:
        Student_grade[keys] = "Outstanding"
    elif score > 80:
        Student_grade[keys] = "Exceed Exceptions"
    elif score > 70:
        Student_grade[keys] = "Acceptable"
    else:
        Student_grade[keys] = "Fails"
    
print(Student_grade)