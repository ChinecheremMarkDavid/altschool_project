import student_data


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Get Average Grade")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            student = student_data.add_student()
            print(f"Added student: {student['first_name']} {student['last_name']}")
        elif choice == '2':
            student_data.view_students()
        elif choice == '3':
            avg_grade = student_data.get_average_grade()
            print(f"Average Grade: {avg_grade:.2f}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")