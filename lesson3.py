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

# Выводим информацию с помощью __str__
print("\n--- Проверяющий (Reviewer) ---")
print(some_reviewer)

print("\n--- Лектор (Lecturer) ---")
print(some_lecturer)

print("\n--- Студент (Student) ---")
print(some_student)