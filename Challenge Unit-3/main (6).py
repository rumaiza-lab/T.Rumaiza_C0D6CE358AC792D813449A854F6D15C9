class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(students):
    return sorted(students, key=lambda student: student.cgpa,reverse=True)
students = [
    Student("Ajay", "1", 3.9),
    Student("Banu", "2", 3.7),
    Student("Charu", "3", 3.8),
    Student("David", "4", 3.95),
  ]

sorted_students = sort_students(students)

for student in sorted_students:
  print(f"{student.name}, {student.roll_number}, {student.cgpa}")