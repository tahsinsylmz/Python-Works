
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

b = len(student_scores)
i = sum(student_scores)/b
while b != 1:
  for j in student_scores:
    b = len(student_scores)
    i = sum(student_scores)/b
    if j <= i and b > 1 :
      student_scores.remove(j)
    else: a = 1
print("The highest score in the class is: " + str(student_scores[0]))
highest_score = 0
for score in student_scores:
  if score > highest_score : 
      score = highest_score
print(highest_score)
