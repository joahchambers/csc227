class Course:
    
    def __init__(self, course_code, max_size):
        self._course_code = course_code
        self._max_size = max_size
        self._enrollment = 0

    def add_student(self):
        if (self._enrollment + 1 > self._max_size):
            print("Course already full")
        else:
            self._enrollment += 1
            print("One student added")

    def drop_student(self):
        if (self._enrollment - 1 < 0):
            print("Course is empty")
        else:
            self._enrollment -= 1
            print("One student dropped")

    def get_course_code(self):
        return self._course_code

    def get_max_size(self):
        return self._max_size

    def get_enrollment(self):
        return self._enrollment

    def set_max_size(self, new_size):
        if (new_size < 0):
            print("Maximum class size cannot be negative")
        elif (new_size < self._enrollment):
            print("Maximum class size cannot be lower than current enrollment")
        else:
            self._max_size = new_size
            print("Maximum class size changed")