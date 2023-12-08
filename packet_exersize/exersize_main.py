from itertools import combinations

from packet_exersize.data_main import courses, durations, mentors

"""
1. Условие задачи
На лекции мы работали с преподавателями.
Давайте усложним задачу и поработаем только с их именами, без фамилий.
У нас есть 4 курса Нетологии, на которых преподают 4 группы преподавателей.
Ваша задача — отделить имена от фамилий и собрать все имена преподавателей со всех четырёх курсов.
Имена ни в коем случае не должны повторяться. А чтобы всё было красиво, отсортируйте их в алфавитном порядке.
"""


def collect_unique_names(mentors: list) -> set:
    unique_names = sorted({name.split()[0] for name in sum(mentors, [])})
    return unique_names


"""
2. Условие задачи
Отсортируйте список курсов courses_list по длительности: от самого короткого к самому длинному. 
Выведите на экран сообщения вида «название курса — длительность курса».
"""


def sort_courses_by_duration(courses: list, durations: list) -> list:
    result = sorted(zip(courses, durations), key=lambda x: x[1])
    return result


"""
3. Условие задачи
У нас всё так же 4 курса Нетологии и 4 группы преподавателей.
На лекции мы вручную искали суперпреподавателей, которые преподают более чем на одном курсе. 
В этом задании вам предстоит написать код, который сделает это автоматически. 
Искать предстоит снова только по именам.
Вам нужно сравнить списки преподавателей попарно и вывести совпавшие имена и пару курсов, 
где встречаются эти имена. 
Тренажёр любит порядок, поэтому не забудьте отсортировать списки преподавателей по алфавиту.
"""


def display_names(courses: list, mentors: list) -> dict:
    data_dict = {}
    for i, j in combinations(range(len(courses)), 2):
        mentors_names_i = [name.split()[0] for name in mentors[i]]
        mentors_names_j = [name.split()[0] for name in mentors[j]]
        set_mentors_names = set(mentors_names_i).intersection(set(mentors_names_j))
        data_dict.setdefault((courses[i], courses[j]), ", ".join(sorted(set_mentors_names)))
    return data_dict

if __name__ == "__main__":
    print(collect_unique_names(mentors))
    print(
        f"Уникальные имена преподавателей: {', '.join(collect_unique_names(mentors))}"
    )
    for course, duration in sort_courses_by_duration(courses, durations):
        print(f"{course} - {duration} месяца(ев)")

    for key, value in display_names(courses, mentors).items():
        print(f"На курсах '{key[0]}' и '{key[1]}' преподают: {value}")
