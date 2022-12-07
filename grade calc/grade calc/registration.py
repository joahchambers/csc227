# ----------------------------------------------------------------
# Author: Simon Chaudhary
# Date: 2020
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

import student.student as student


def main():

    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, course list,
    # max class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity. Then
    # let student choose to add course, drop course or list courses.
    # This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]
    while True:
        sid = input("Enter ID to log in, or 0 to quit: ")
        if sid == '0':
            print()
            break
        else:
            success=login(sid, student_list)
            while success:
                choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
                if choice == 0:
                    print("Student session ended.")
                    print()
                    success=False
                if choice == 1:
                    student.add_course(sid, course_list, roster_list, max_size_list)
                    print()
                if choice == 2:
                    student.drop_course(sid, course_list, roster_list)
                    print()
                if choice == 3:
                    student.list_courses(sid, course_list, roster_list)
                    print()


def login(id, s_list):

    pin = input("Enter PIN: ")
    found = False
    for i  in s_list:
        if (i[0] == id and i[1] == pin):
            print("ID and PIN verified")
            print()
            return True
    if(found == False):
        print("ID or PIN incorrect")
        return False

    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------

    #pass # temporarily avoid empty function definition


main()



