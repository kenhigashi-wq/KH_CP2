#KH gradebook
from student import Student

class GradeBook:

    def __init__(self):
        self.students = []

    def add_student(self, name, student_id, grade_level):

        if self.find_student_by_id(student_id):
            return False
        self.students.append(Student(name, student_id, grade_level))
        return True

    def find_student_by_id(self, student_id):

        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_all_students(self):

        if not self.students:
            print("No students in the grade book.")
            return

        print("\nAll Students:")
        print("-" * 40)

        for student in self.students:
            avg = student.calculate_average()
            avg_display = f"{avg:.1f}" if avg is not None else "N/A"

            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Grade Level: {student.grade_level}")
            print(f"Average: {avg_display}")
            print(f"Letter Grade: {student.get_letter_grade()}")
            print("-" * 40)

        print(f"Total Students: {len(self.students)}")

    # bonus , Class Statistics
    def class_average(self):

        averages = [
            student.calculate_average()
            for student in self.students
            if student.calculate_average() is not None
        ]

        if not averages:
            return None
        return sum(averages) / len(averages)

    def highest_grade(self):

        all_grades = [grade for student in self.students for grade in student.grades]
        if not all_grades:
            return None
        return max(all_grades)

    def lowest_grade(self):

        all_grades = [grade for student in self.students for grade in student.grades]
        if not all_grades:
            return None
        return min(all_grades)
    