from manage.course import Course
def main():
    course_code = str(input("Enter course code: "))
    max_size = int(input("Enter maximum class size: "))
    course = Course(course_code, max_size)
    user_input = 1

    while (user_input != 0):
        user_input = int(input("\nEnter 1 to add student, 2 to drop student, 3 for course info, 4 to change max class size, or 0 to exit: "))

        if (user_input == 0):
            break
        elif (user_input == 1):
            course.add_student()
            print("Enrollment:", course.get_enrollment())
        elif (user_input == 2):
            course.drop_student()
            print("Enrollment:", course.get_enrollment())
        elif (user_input == 3):
            print("Course code:", course.get_course_code())
            print("Maximum class size:", course.get_max_size())
            print("Enrollment:", course.get_enrollment())
        elif (user_input == 4):
            new_size = int(input("Enter new maximum class size: "))
            course.set_max_size(new_size)
        else:
            print("Invalid input")

main()