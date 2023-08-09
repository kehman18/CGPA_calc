def calculate_cgpa(credits, grades):
  """Calculates the CGPA for a given set of credits and grades.

  Args:
    credits: A list of credits for each course.
    grades: A list of grades for each course.

  Returns:
    The CGPA for the given set of credits and grades.
  """

  total_credits = sum(credits)
  total_points = 0
  for credit, grade in zip(credits, grades):
    if grade == "A":
      points = 5.0 * credit
    elif grade == "B":
      points = 4.0 * credit
    elif grade == "C":
      points = 3.0 * credit
    elif grade == "D":
      points = 2.0 * credit
    elif grade == "E":
      points = 1.0 * credit
    else:
      points = 0.0 * credit
    total_points += points
  cgpa = total_points / total_credits
  return cgpa

def main():
  credits = []
  grades = []
  number_of_courses = int(input("Enter the number of courses: "))
  for i in range(number_of_courses):
    credit = int(input("Enter the credits for course {}: ".format(i + 1)))
    grade = input("Enter the grade for course {}: ".format(i + 1))
    credits.append(credit)
    grades.append(grade)
  cgpa = calculate_cgpa(credits, grades)
  print("The CGPA is:", cgpa)

if __name__ == "__main__":
  main()
