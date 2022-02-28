student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

student_grades1 = {}
for a in range(0, 101):
  if a < 100 and a > 90 :
    student_grades1[a] = "Outstanding"
  elif a < 91 and a > 80 :
    student_grades1[a] = "Exceeds Expectations"
  elif a < 81 and a > 70:
    student_grades1[a] = "Acceptable"
  else :
    student_grades1[a] = "Fail"
for i in student_scores:
    student_grades[i] = student_grades1[student_scores[i]]


print(student_grades)