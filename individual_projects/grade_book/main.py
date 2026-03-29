from gradebook import GradeBook

def pause():
    input("\nPress Enter to continue...")

gradebook = GradeBook()

while True:
    print("SIMPLE GRADE BOOK")
    print("===================================")
    print("1. Add New Student")
    print("2. Add Grade to Student")
    print("3. View Student Record")
    print("4. View All Students")
    print("5. Class Statistics")
    print("6. Exit")

    choice = input("\nEnter your choiice (1-6): ")

    if choice == "1":
        print("\nAdd New Student")
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        grade_level = input("Enter grade level (9-12): ")

        if grade_level not in ["9", "10", "11", "12"]:
            print("Invalid")
            pause()
            continue

        if gradebook.add_student(name, student_id, grade_level):
            print("\nStudent added successfully")
            print(f"Name: {name}")
            print(f"ID: {student_id}")
            print("Grades: None yet")
        else:
            print("A student with that ID already exists")

        pause()

    elif choice == "2":
        print("\nAdd Grade")

        if not gradebook.students:
            print("No students available.")
            pause()
            continue

        for student in gradebook.students:
            print(f"{student.name} (ID: {student.student_id})")

        student_id = input("\nEnter student ID: ")
        student = gradebook.find_student_by_id(student_id)

        if not student:
            print("Student not found")
            pause()
            continue

        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                student.add_grade(grade)
                avg = student.calculate_average()
                print("Grade added successfully!.")
                print(f"Current average: {avg:.1f} ({student.get_letter_grade()})")
            else:
                print("Grade must be between 0 and 100")
        except ValueError:
            print("Invalid")

        pause()

    elif choice == "3":
        print("\nView Student Record")
        student_id = input("Enter student ID: ")
        student = gradebook.find_student_by_id(student_id)

        if student:
            student.display_info()
        else:
            print("Invalid")

        pause()

    elif choice == "4":
        print("\nAll Students")
        gradebook.display_all_students()
        pause()

    elif choice == "5":
        print("\nClass Statistics")
        print(f"Total Students: {len(gradebook.students)}")

        avg = gradebook.class_average()
        if avg is not None:
            print(f"Class Average: {avg:.1f}")
        else:
            print("Class Average: N/A")

        highest = gradebook.highest_grade()
        lowest = gradebook.lowest_grade()

        print(f"Highest Grade: {highest if highest is not None else 'N/A'}")
        print(f"Lowest Grade: {lowest if lowest is not None else 'N/A'}")

        pause()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalidd")
        pause()