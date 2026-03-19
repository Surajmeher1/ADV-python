students = []

def add_student():
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        m = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    avg = sum(marks) / len(marks)

    # GPA Calculation
    if avg >= 90:
        gpa = 4.0
    elif avg >= 80:
        gpa = 3.5
    elif avg >= 70:
        gpa = 3.0
    elif avg >= 60:
        gpa = 2.5
    elif avg >= 50:
        gpa = 2.0
    else:
        gpa = 0.0

    student = {
        "name": name,
        "marks": marks,
        "average": avg,
        "gpa": gpa
    }

    students.append(student)
    print("Student result added successfully!\n")


def show_results():
    if len(students) == 0:
        print("No student records found.\n")
        return

    for s in students:
        print("Name:", s["name"])
        print("Marks:", s["marks"])
        print("Average:", s["average"])
        print("GPA:", s["gpa"])
        print("----------------------")


while True:
    print("\n===== COLLEGE RESULT MANAGEMENT =====")
    print("1. Add Student Marks")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_results()
    elif choice == "3":
        print("Program closed.")
        break
    else:
        print("Invalid choice.")