# Build a simple console-based student management system that uses Python dictionaries to store
# and manage data about students, their courses, and grades.
# Store student data in a dictionary, where:
# • Each key is a student ID (or name).
# • Each value is another dictionary containing:
# o 'name': full name
# o 'courses': a dictionary of courses and grades.
# Example structure:
# students = {
# 'S001': {
# 'name': 'Alice',
# 'courses': {'Math': 90, 'English': 85}
# },
# 'S002': {
# 'name': 'Bob',
# 'courses': {'Math': 75, 'Science': 80}
# }
# }
# • Feature to implement
# 1. Add a new student.
# 2. Add or update a course & grade for a student.
# 3. Remove a student by ID.
# 4. Display all students with their courses and grades.
# 5. Display the average grade for a given student.
# 6. Find the student(s) with the highest average grade.

def add_new_student(students, student_id, name, courses):
    # modify students dictionary internally (dangerous)
    # student_id is a str (also, can't really assign student_id simply so manually do it)
    # name is a str
    # courses is a list of dictionary representing courses

    student_dictionary = {
        "name":name,
        "courses": courses
    }
    
    students[student_id] = student_dictionary

def update_student_data(students, student_id, new_course_data):
    # uses student ID to get the location of the student and  modify their courses or grades
    # simply replace the dictionary with a new given dictionary (since it's hard to modify or change course name etc)
    
    student_data = students[student_id]

    student_data["courses"] = new_course_data

def remove_student_by_id(students, student_id):
    # removes the student from the dictionary
    students.pop(student_id)

def display_all_students_details(students):
    for student_id, student_data in students.items():
        print(f"{student_data['name']}'s grades: {student_data['courses']}")

def get_average_grade(students, student_id):
    student_details = students[student_id]
    sum_of_grade = 0
    for grade in student_details["courses"].values():
        sum_of_grade += grade

    average_grade = sum_of_grade/len(student_details)
    return average_grade

def find_top_student(students):
    # in case of duplicates, store scores as a key to a list of names
    average_score = {}

    for student_id, student_details in students.items():
        student_average_grade = get_average_grade(students, student_id)

        # round the grade to the nearest integer
        if (rounded_avg_grade:=round(student_average_grade)) in average_score:
            average_score[rounded_avg_grade].append((student_details['name'], student_average_grade))
        else:
            average_score[rounded_avg_grade] = [(student_details['name'], student_average_grade)]    

    # not very efficient, both for time and memory
    return average_score[max(average_score.keys())]
        
if __name__ == "__main__":
    students = {
        'S001': {
            'name': 'Alice',
            'courses': {'Math': 90, 'English': 85}
    },
        'S002': {
            'name': 'Bob',
            'courses': {'Math': 75, 'Science': 80}
        }
    }
    add_new_student(students, "S003", "Penny", {"Math": 10, "English": 100})
    update_student_data(students, "S003", {"Math": 100, "English": 100})
    remove_student_by_id(students, "S001")
    display_all_students_details(students)
    print(get_average_grade(students, "S002"))       
    add_new_student(students, "S004", "Johnathan Joestar", {"Math": 70, "English":60})
    add_new_student(students, "S005", "Walter White", {"Chemistry":100, "PE":40})
    add_new_student(students, "S006", "Shelly", {"Math":90, "Science":80})
    add_new_student(students, "S007", "Ted", {"Math":100, "Science":100})
    print(find_top_student(students))
    
