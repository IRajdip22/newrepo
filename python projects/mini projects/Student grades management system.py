students_grades = {}

def add_student(name, grade):
    students_grades[name] = grade
    print(f"{name} has been added to the system with a grade of {grade}")

def update_student(name, grade):
    if name in students_grades:
        students_grades[name] = grade
        print(f"{name} has been updated to a grade of {grade}")
    else:
        print(f"{name} not found in the system")

def delete_student(name):
    if name in students_grades:
        del students_grades[name]
        print(f"{name} has been deleted from the system")
    else:
        print(f"{name} not found in the system")

def view_student():
    if students_grades:
        for name,grade in students_grades.items():
            print(f"{name}: {grade}")
    else:
        print("Not found in the system  or not added yet")                             
def main():
    while True:
        print("Welcome to the student grades management system")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View student")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            update_student(name, grade)
        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)
        elif choice == 4:
            view_student()
        elif choice == 5:
            print("Thank you for using the student grades management system")
            break
        else:
            print("Invalid choice")

main()