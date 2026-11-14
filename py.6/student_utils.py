import random
import statistics


def generate_grades(count):
    grades = []
    for i in range(count):
        grades.append(random.randint(1, 12))
    return grades


def average_grade(grades):
    return statistics.mean(grades)


def get_level(average):
    if average >= 10:
        return "високий"
    if average >= 7:
        return "достатній"
    if average >= 4:
        return "середній"
    return "початковий"
