
students = {}
subjects_offered = ["Math", "Science", "English", "History", "Computer Science"]

while True:
    print("\nWelcome to the Student Data Organizer!")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            print("\nEnter student details:")
            student_id = input("Student ID: ")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ").split(",")

            students[student_id] = {
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": dob,
                "Subjects": [s.strip() for s in subjects]
            }
            print("Student added successfully.")

        case "2":
            if not students:
                print("\nNo students available.")
            else:
                print("\n--- Display All Students ---")
                for sid, data in students.items():
                    print(f"Student ID: {sid} - Name: {data['Name']} - Age: {data['Age']}")
                    print(f"Grade: {data['Grade']}")
                    print("Subjects:", ", ".join(data["Subjects"]))

        case "3":
            student_id = input("\nEnter Student ID to update: ")

            if student_id in students:
                print("Leave blank to keep old value.")
                name = input("New Name: ")
                age = input("New Age: ")
                grade = input("New Grade: ")

                if name:
                    students[student_id]["Name"] = name
                if age:
                    students[student_id]["Age"] = age
                if grade:
                    students[student_id]["Grade"] = grade

                print("Student information updated.")
            else:
                print("Student not found.")

        case "4":
            student_id = input("\nEnter Student ID to delete: ")

            if student_id in students:
                del students[student_id]
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        case "5":
            print("Subjects Offered:")
            for subject in subjects_offered:
                print( subject)

        case "6":
            print("\nExiting program, thank you! ")
            break

        case _:
            print("\nInvalid choice. Please try again.")
