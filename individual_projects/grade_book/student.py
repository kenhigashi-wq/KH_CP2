#KH student

class Student:
    def __init__(self, name, student_id, grade_level):
        self.name = name
        self.student_id = student_id
        self.grade_level = grade_level
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        avg = self.calculate_average()
        if avg is None:
            return "N/A"
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def academic_standing(self):#Bonus
        
        avg = self.calculate_average()
        if avg is None:
            return "N/A"
        if avg >= 90:
            return "Honor Roll"
        elif avg >= 80:
            return "Good Standing"
        else:
            return "Needs Improvement"
        
    def display_info(self):
        
        avg = self.calculate_average()
        avg_display = f"{avg:.2f}" if avg is not None else "N/A"

        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Grade Level: {self.grade_level}")
        print(f"Grades: {self.grades if self.grades else 'None yet'}")
        print(f"Average: {avg_display}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"Academic Standing: {self.academic_standing()}")


        
