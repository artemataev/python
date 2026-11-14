import tkinter as tk
from tkinter import messagebox

import student_utils

STUDENTS = ["Anna", "Ivan", "Olha"]


def build_report(count):
    lines = []
    for name in STUDENTS:
        grades = student_utils.generate_grades(count)
        average = student_utils.average_grade(grades)
        level = student_utils.get_level(average)
        lines.append(f"{name}: {grades} → {round(average, 1)} → {level}")
    return "\n".join(lines)


def on_generate():
    value = count_entry.get().strip()

    if not value.isdecimal() or int(value) < 1 or int(value) > 20:
        messagebox.showerror("Помилка", "Введіть ціле число від 1 до 20.")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Помилка: введіть ціле число від 1 до 20.")
        return

    report = build_report(int(value))
    print(report)
    print()

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, report)


def main():
    global count_entry, result_text

    root = tk.Tk()
    root.title("Статистика учнів")

    label = tk.Label(root, text="Кількість оцінок (1–20):")
    label.pack()

    count_entry = tk.Entry(root)
    count_entry.pack()

    button = tk.Button(root, text="Сформувати звіт", command=on_generate)
    button.pack()

    result_text = tk.Text(root, width=60, height=8)
    result_text.pack()

    root.mainloop()


main()
