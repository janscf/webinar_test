from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Student:
    """
    Класс
    студента
    с информацией
    об имени и возрасте
    """
    first_name: str
    last_name: str
    age: int

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Group:
    def __init__(self, group_number):
        self._students = []
        self._group_number = group_number

    def add_student(self, student: Student):
        self._students.append(student)

    def add_students(self, students: List[Student]):
        for student in students:
            self.add_student(student)

    """
    Добавить метод print_info(), который выводит текст:

    Когорта номер 60
    В когорте 3 студента:
    - Иван Демидов
    - Виктория Сикрет
    - Тимоти Шаламе
    """

if __name__ == '__main__':
    group = Group(60)
    group.add_students(
        [
            Student(
                first_name='Иван',
                last_name='Демидов',
                age=59,
            ),
            Student(
                first_name='Виктория',
                last_name='Сикрет',
                age=18,
            ),
            Student(
                first_name='Тимоти',
                last_name='Шаламе',
                age=26,
            ),
        ]
    )
    # group.print_info()
