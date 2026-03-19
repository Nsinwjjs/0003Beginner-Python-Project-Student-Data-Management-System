# Student Management System

total_students = []     # saare students ka data
student_ids = []        # student IDs
subjects = set()        # unique subjects

while True:
    print("\n------ MENU ------")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    match choice:

        # ---------- ADD STUDENT ----------
        case 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            student_id = int(input("Enter student ID: "))
            sub = input("Enter subject: ")

            student = {
                "id": student_id,
                "name": name,
                "age": age,
                "grade": grade,
                "subject": sub
            }

            total_students.append(student)
            student_ids.append(student_id)
            subjects.add(sub)

            print(f"\nHello {name}, welcome to Institute")
            print("Student added successfully ✅")

        # ---------- SHOW ALL STUDENTS ----------
        case 2:
            if not total_students:
                print("No students found ❌")
            else:
                print("\n--- All Students ---")
                for s in total_students:
                    print(s)

        # ---------- SEARCH STUDENT ----------
        case 3:
            key = input("Search by (name / grade / subject): ")
            value = input("Enter value: ")

            result = []
            for s in total_students:
                if key in s and str(s[key]).lower() == value.lower():
                    result.append(s)

            if result:
                print("\n--- Search Result ---")
                for r in result:
                    print(r)
            else:
                print("No matching student found ❌")

        # ---------- EXIT ----------
        case 4:
            print("Program exited ")
            break

        # ---------- INVALID ----------
        case _:
            print("Invalid choice ")
