# -*- coding: utf-8 -*-
import csv
import tkinter as tk
from tkinter import messagebox, simpledialog

students = []

# 录入学生信息
def add_student():
    student_id = simpledialog.askstring("输入学号", "输入学号:")
    name = simpledialog.askstring("输入姓名", "输入姓名:")
    class_name = simpledialog.askstring("输入班级", "输入班级:")

    try:
        math_score = float(simpledialog.askstring("输入数学成绩", "输入数学成绩:"))
        english_score = float(simpledialog.askstring("输入英语成绩", "输入英语成绩:"))
        cs_score = float(simpledialog.askstring("输入计算机科学成绩", "输入计算机科学成绩:"))
    except ValueError:
        messagebox.showerror("错误", "成绩要是数字。")
        return

    student = {
        "student_id": student_id,
        "name": name,
        "class": class_name,
        "math": math_score,
        "english": english_score,
        "cs": cs_score
    }
    students.append(student)
    messagebox.showinfo("成功", "录入成功！")

# 计算各科目平均成绩
def calculate_averages():
    if not students:
        messagebox.showwarning("错误", "没有信息可计算。")
        return

    total_math = total_english = total_cs = 0
    for student in students:
        total_math += student["math"]
        total_english += student["english"]
        total_cs += student["cs"]

    avg_math = total_math / len(students)
    avg_english = total_english / len(students)
    avg_cs = total_cs / len(students)

    result = (f"数学平均成绩: {avg_math:.2f}\n"
              f"英语平均成绩: {avg_english:.2f}\n"
              f"计算机科学平均成绩: {avg_cs:.2f}")
    messagebox.showinfo("平均成绩", result)

# 查询某学生成绩
def query_student():
    student_id = simpledialog.askstring("查询成绩", "输入要查询的学号:")
    for student in students:
        if student["student_id"] == student_id:
            result = (f"学生姓名: {student['name']}\n"
                      f"班级: {student['class']}\n"
                      f"数学成绩: {student['math']}\n"
                      f"英语成绩: {student['english']}\n"
                      f"计算机科学成绩: {student['cs']}")
            messagebox.showinfo("学生成绩", result)
            return
    messagebox.showwarning("错误", "未找到该信息。")

# 按某科目进行排名
def rank_students():
    subject = simpledialog.askstring("科目排名", "输入要排名的课目（math, english, cs）:").strip().lower()
    if subject not in ["math", "english", "cs"]:
        messagebox.showerror("错误", "输入无效。")
        return

    ranked_students = sorted(students, key=lambda x: x[subject], reverse=True)
    result = f"按{subject}成绩排名：\n"
    for i, student in enumerate(ranked_students, start=1):
        result += f"{i}. {student['name']} - {student[subject]}\n"

    messagebox.showinfo("科目排名", result)

# 保存数据
def save_data(filename="students.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["student_id", "name", "class", "math", "english", "cs"])
        for student in students:
            writer.writerow(
                [student["student_id"], student["name"], student["class"], student["math"], student["english"],
                 student["cs"]])
    messagebox.showinfo("成功", "数据已保存")

# 读取数据
def load_data(filename="students.csv"):
    global students
    students = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "student_id": row["student_id"],
                    "name": row["name"],
                    "class": row["class"],
                    "math": float(row["math"]),
                    "english": float(row["english"]),
                    "cs": float(row["cs"])
                }
                students.append(student)
        messagebox.showinfo("成功", "数据已加载")
    except FileNotFoundError:
        messagebox.showerror("错误", "未找到。")

# 主窗口
def main():
    root = tk.Tk()
    root.title("学生成绩管理系统")

    # 创建按钮
    btn_add_student = tk.Button(root, text="录入学生信息", command=add_student)
    btn_calculate_averages = tk.Button(root, text="计算各科目平均成绩", command=calculate_averages)
    btn_query_student = tk.Button(root, text="查询某学生成绩", command=query_student)
    btn_rank_students = tk.Button(root, text="按科目成绩排名", command=rank_students)
    btn_save_data = tk.Button(root, text="保存数据", command=lambda: save_data("students.csv"))
    btn_load_data = tk.Button(root, text="加载数据", command=lambda: load_data("students.csv"))
    btn_exit = tk.Button(root, text="退出", command=root.quit)

    # 布局按钮
    btn_add_student.pack(fill=tk.X, pady=5)
    btn_calculate_averages.pack(fill=tk.X, pady=5)
    btn_query_student.pack(fill=tk.X, pady=5)
    btn_rank_students.pack(fill=tk.X, pady=5)
    btn_save_data.pack(fill=tk.X, pady=5)
    btn_load_data.pack(fill=tk.X, pady=5)
    btn_exit.pack(fill=tk.X, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
