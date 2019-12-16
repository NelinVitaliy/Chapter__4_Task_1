class Student:
    def __init__(self, name, last_name, department, year_of_entrance):
        self.name = name
        self.last_name = last_name
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        print(f"{self.name} {self.last_name} поступил в {self.year_of_entrance}г. на факультет: {self.department}")


vasya = Student('Вася', 'Иванов', 'Програмирование', 2017)
vasya.get_student_info()

petya = Student('Петя', 'Иванов', 'История', 2015)
petya.get_student_info()
