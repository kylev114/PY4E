student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

def gradeCheck(student,score):
    if score > 90: return (student,'Outstanding') 
    elif score >= 80: return (student, 'Exceeds Expectations')
    elif score >= 70: return (student, 'Acceptable')
    elif score < 70: return (student, 'Fail')

for (key, val) in list(student_scores.items()):
   student_grades[gradeCheck(key,val)[0]] = gradeCheck(key,val)[1]

   

# 🚨 Don't change the code below 👇
print(student_grades)