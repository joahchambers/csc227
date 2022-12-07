import student.student as student
import manage.class_info_code as Course

# Lists to store objects
Courses = []
Students = []

"""
        Main function.
"""
def main():
    while True:
        sid = str(input("Enter ID to log in, or 0 to quit: "))
        if sid == '0':
            break
        else:
            validate(sid)

"""
        Validate user as a student or a teacher. 
        Use login funciton to login a user
"""
def validate(sid: int):
    val=input("Are you a student or teacher? ").lower()
    if val == "student" or val == "teacher":
        login(sid, val)
    else:
        print("Invalid input. Try again.")
        validate(sid)


"""
        Login user based on type of user
        Send to appropriate view function to start main process
"""
def login(sid: int, login_type: str):
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    teacher_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    if login_type == 'student':
        pin = input("Enter PIN: ")
        found = False
        for i in student_list:
            if (i[0] == sid and i[1] == pin):
                print("ID and PIN verified\n")
                found = True
                break
        if found:
            student_view()
        else:
            print("ID or PIN incorrect")
    else:
        pin = input("Enter PIN: ")
        found = False
        for i in teacher_list:
            if (i[0] == sid and i[1] == pin):
                print("ID and PIN verified\n")
                found = True
                break
        if found:
            teacher_view()
        else:
            print("ID or PIN incorrect")



def teacher_view():
    # Initiate main value
    main_input = 0

    # Main menu loop
    while main_input != 4:
        main_input = int(input("Main Menu\n1 - Courses\n2 - Students\n3 - Departments\nEnter 1, 2, 3, or 4 to logout: "))

        # Check input to see which menu to display
        match main_input:
            case 1:
                # Course Menu
                course_input = 0
                while course_input != 4:
                    course_input = int(input("Courses Menu\n1 - Create Course\n2 - View Courses\n3 - View Course Information\nEnter 1, 2, 3, or 4 to return to main menu: "))

                    match course_input:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            pass
                        case 4:
                            break
                        case _:
                            print("Invalid input. Try again.")
            case 2:
                # Student Menu
                student_input = 0
                while student_input != 3:
                    student_input = int(input("Students Menu\n1 - Create new student\n2 - Add student to course\n3 - Drop student from course\n4 - Return to main menu\n"))

                    match student_input:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            break
                        case _:
                            print("Invalid input. Try again.")
            
            case 3:
                break
            case _:
                print('Incorrect input. Try again.')


def student_view():
    pass


if __name__ == "__main__":
    main()
