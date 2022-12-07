class Course:

    def __init__(self, course_desc, course_code, credit, department):
        self.course_desc = course_desc
        self.course_code = course_code
        self.credit = credit
        self.department = department

    # def __str__(self):
    #     return "Course Information : Course Name = {}, Course Code = {} and Course Credit = {} and Department Name = {}".format(
    #         self.course_desc, self.course_code, self.credit, self.department.name)

    def __repr__(self):
        return "Course Information : Course Name = {}, Course Code = {} and Course Credit = {} and Department Name = {}".format(
            self.course_desc, self.course_code, self.credit, self.department.name)

    def setCourse_desc(self, name):
        self.name = name

    def getCourse_desc(self):
        return self.name

    def setCourse_code(self, courses):
        self.courses = courses

    def getCourse_code(self):
        return self.courses

    def getCredit(self):
        return self.department_code

    def setCredit(self, department_code):
        self.department_code = department_code

    def getDepartment(self):
        return self.department

    def setDepartment(self, department):
        self.department = department


# d1 = Department('Computer Science', 'CS', [])
# c1 = Course('Computer Networks', 'CS101', 4.0, d1)
# c2 = Course('Artificial Intelligence', 'CS102', 4.5, d1)
# courseList = []
# courseList.append(c1)
# courseList.append(c2)
# d1.setCourses(courseList)



class Department:
    def __init__(self, name, department_code, courses):
        self.name = name
        self.courses = courses
        self.department_code = department_code

    # def __str__(self):
    #     return "Department Information : Department Name = {}, Department Code = {}, Department Courses = {}".format(self.name, self.department_code, self.courses)

    def __repr__(self):
        return "Department Information : Department Name = {}, Department Code = {}, Department Courses = {}".format(self.name, self.department_code, self.courses )

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCourses(self, courses):
        self.courses = courses

    def getCourses(self):
        return self.courses

    def getDepartment_code(self):
        return self.department_code

    def setDepartment_code(self, department_code):
        self.department_code = department_code
    
    def add_course(self, course):
        self.courses.append(course)

# d1 = Department('Computer Science', 'CS',[])
# c1 = Course('Computer Networks', 'CS101', 4.0, d1)
# c2 = Course('Artificial Intelligence', 'CS102', 4.5, d1)
# courseList = []
# courseList.append(c1)
# courseList.append(c2)
# d1.setCourses(courseList)

# print(d1)

class Student:

    def __init__(self, name, student_number, courses):
        self.name = name
        self.courses = courses
        self.student_number = student_number

    # def __str__(self):
    #     return "Student Information : Student Name = {}, Student Number = {}, Courses Joined = {}".format(self.name, self.student_number, self.courses)

    def __repr__(self):
        return "Student Information : Student Name = {}, Student Number = {}, Courses Joined = {}".format(self.name, self.student_number, self.courses)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setCourses(self, courses):
            self.courses = courses

    def getCourses(self):
        return self.courses

    def getStudent_number(self):
        return self.student_number

    def setStudent_number(self, student_number):
        self.student_number = student_number

# d1 = Department('Computer Science', 'CS',[])
# c1 = Course('Computer Networks', 'CS101', 4.0, d1)
# c2 = Course('Artificial Intelligence', 'CS102', 4.5, d1)
# courseList = []
# courseList.append(c1)
# courseList.append(c2)
# s1 = Student('John Diggle',courseList, '001')
#
# print(s1)



# class Test :
#     d1 = Department('Computer Science', 'CS',[])
#     c1 = Course('Computer Networks', 'CS101', 4.0, d1)
#     c2 = Course('Artificial Intelligence', 'CS102', 4.5, d1)
#     courseList = []
#     courseList.append(c1)
#     courseList.append(c2)
#     s1 = Student('John Diggle',courseList, '001')

#     print(s1)
