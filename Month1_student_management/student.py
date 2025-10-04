
students = []

def add_student():
    first_name = input('enter first name: ')
    last_name = input('enter last name: ')
    age = int(input('enter age: '))
    student_id = input('enter student id: ')
    student_grade = int(input('enter student grade: '))
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'student_id': student_id,
        'student_grade': student_grade
        }
    students.append(student)
    return student


def view_students():
        for student in students:
            print(f"{student['first_name']} {student['last_name']}, Age: {student['age']}, ID: {student['student_id']}, Grade: {student['student_grade']}")


def get_average_grade():
    if not students:
        return 0
    total_grade = sum(student['student_grade'] for student in students)
    average_grade = total_grade / len(students)
    return average_grade