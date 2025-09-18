class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress or course not in lecturer.courses_attached:
            return 'Ошибка'
        if grade < 1 or grade > 10:
            return 'Ошибка'

        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        return None

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else 'Нет завершенных курсов'

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0.0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() > other._calculate_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() >= other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() != other._calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade}")

    def _calculate_avg_grade(self):
        if not self.grades:
            return 0.0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() > other._calculate_avg_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() >= other._calculate_avg_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() != other._calculate_avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создаем объекты
some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_student = Student('Ruoy', 'Eman', 'your_gender')

# Добавляем данные для получения оценок 9.9
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_student.grades = {'Python': [10, 9.9, 10], 'Git': [9.9, 9.8]}

some_lecturer.courses_attached += ['Python']
some_lecturer.grades = {'Python': [9.9, 10, 9.8]}

# Создаем по 2 экземпляра каждого класса
student1 = Student('Иван', 'Иванов', 'male')
student2 = Student('Мария', 'Петрова', 'female')

lecturer1 = Lecturer('Алексей', 'Сидоров')
lecturer2 = Lecturer('Ольга', 'Кузнецова')

reviewer1 = Reviewer('Петр', 'Смирнов')
reviewer2 = Reviewer('Анна', 'Попова')

# Настраиваем курсы
student1.courses_in_progress = ['Python', 'Git']
student2.courses_in_progress = ['Python', 'JavaScript']

lecturer1.courses_attached = ['Python']
lecturer2.courses_attached = ['Git']

reviewer1.courses_attached = ['Python']
reviewer2.courses_attached = ['Git']

# Вызываем метод rate_lecture (студенты оценивают лекторов)
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer2, 'Git', 8)
student2.rate_lecture(lecturer1, 'Python', 10)

# Вызываем метод rate_hw (проверяющие оценивают студентов)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student1, 'Git', 7)

# Вызываем метод __str__ для всех объектов
print("=== СТУДЕНТЫ ===")
print(student1)
print("\n" + "-"*30)
print(student2)

print("\n=== ЛЕКТОРЫ ===")
print(lecturer1)
print("\n" + "-"*30)
print(lecturer2)

print("\n=== ПРОВЕРЯЮЩИЕ ===")
print(reviewer1)
print("\n" + "-"*30)
print(reviewer2)

# Вызываем методы сравнения
print("\n=== СРАВНЕНИЕ СТУДЕНТОВ ===")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 == student2: {student1 == student2}")

print("\n=== СРАВНЕНИЕ ЛЕКТОРОВ ===")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")

# Функция для подсчета средней оценки студентов по курсу
def avg_student_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

# Функция для подсчета средней оценки лекторов по курсу
def avg_lecturer_grade(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

# Вызываем функции для подсчета средних оценок
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("\n=== СРЕДНИЕ ОЦЕНКИ ПО КУРСАМ ===")
print(f"Средняя оценка студентов по Python: {avg_student_grade(students, 'Python')}")
print(f"Средняя оценка студентов по Git: {avg_student_grade(students, 'Git')}")
print(f"Средняя оценка лекторов по Python: {avg_lecturer_grade(lecturers, 'Python')}")
print(f"Средняя оценка лекторов по Git: {avg_lecturer_grade(lecturers, 'Git')}")