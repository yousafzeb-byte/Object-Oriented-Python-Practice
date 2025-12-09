import re   # For email validation (Bonus Part)


# ---------------------------------------------
# PART 1: CLASS DEFINITION
# ---------------------------------------------
class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades  # list of integers

    # Add a grade to the list
    def add_grade(self, grade):
        self.grades.append(grade)

    # Return average grade
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    # Display student info
    def display_info(self):
        print(f"\n--- Student Info ---")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")

    # Part 4: Return grades as a tuple
    def grades_tuple(self):
        return tuple(self.grades)

    # Bonus: Validate email format
    def is_valid_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.com$'
        return re.match(pattern, self.email) is not None


# ---------------------------------------------
# PART 2: WORKING WITH OBJECTS
# ---------------------------------------------
student1 = Student("Alice", "alice@example.com", [85, 90, 95])
student2 = Student("Bob", "bob@example.com", [70, 88, 92])
student3 = Student("Charlie", "charlie@example.com", [100, 78, 89])

# Add 2 new grades for each
for student in (student1, student2, student3):
    student.add_grade(87)
    student.add_grade(93)


# ---------------------------------------------
# PART 3: DICTIONARY & SET INTEGRATION
# ---------------------------------------------
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Safely get a student by email
def get_student_by_email(email):
    return student_dict.get(email, None)

# Create a set of all unique grades
all_grades_set = set()
for student in student_dict.values():
    all_grades_set.update(student.grades)

print("\nUnique Grades Across All Students:", all_grades_set)


# ---------------------------------------------
# PART 4: TUPLE PRACTICE + IMMUTABILITY DEMO
# ---------------------------------------------
print("\n--- Tuple Immutability Test ---")

tuple_example = student1.grades_tuple()
print("Original Tuple:", tuple_example)

try:
    tuple_example[0] = 999  # ERROR!
except TypeError:
    print("❌ Tuples are immutable — cannot modify values.\n")


# ---------------------------------------------
# PART 5: LIST OPERATIONS
# ---------------------------------------------
for student in student_dict.values():
    print(f"\n--- List Operations for {student.name} ---")

    # Remove last grade
    removed = student.grades.pop()
    print(f"Removed Last Grade: {removed}")

    # First and last grade
    print(f"First Grade: {student.grades[0]}")
    print(f"Last Grade: {student.grades[-1]}")

    # Number of grades
    print(f"Number of Grades Now: {len(student.grades)}")

# Display each student’s final info
for student in student_dict.values():
    student.display_info()


# ---------------------------------------------
# PART 6: BONUS
# ---------------------------------------------
print("\n--- BONUS ---")

# Check email validity
for student in student_dict.values():
    print(f"{student.email} valid? --> {student.is_valid_email()}")

# Count grades above 90
grades_above_90 = sum(
    1 for student in student_dict.values()
    for grade in student.grades
    if grade > 90
)

print(f"\nTotal Grades Above 90: {grades_above_90}")
