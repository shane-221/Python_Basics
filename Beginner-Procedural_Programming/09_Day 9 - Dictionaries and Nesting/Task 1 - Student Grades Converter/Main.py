student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
for i in student_scores:
    if student_scores[i]<=70:
        student_grades[i]="Fail"
    elif 71<=student_scores[i]<=80:
        student_grades[i]="Acceptable"
    elif 81<=student_scores[i]<=90:
        student_grades[i]="Exceeded Expectations"
    elif 91<=student_scores[i]<=100:
        student_grades[i]="Outstanding"
print(student_grades)