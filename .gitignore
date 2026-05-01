import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

DEFAULT_TASKS = [
    {"name": "Прочитать статью по Python", "type": "учёба"},
    {"name": "Сделать зарядку 15 минут", "type": "спорт"},
    {"name": "Написать отчёт", "type": "работа"},
    {"name": "Изучить новый модуль random", "type": "учёба"},
    {"name": "Пробежка 2 км", "type": "спорт"},
    {"name": "Созвониться с клиентом", "type": "работа"}
]

FILENAME = "tasks_history.json"

class RandomTaskGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Task Generator")
        self.root.geometry("550x550")

        self.history = self.load_history()
        self.tasks = DEFAULT_TASKS.copy()

        self.create_widgets()
        self.update_history_list()

    def load_history(self):
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_history(self):
        with open(FILENAME, "w", encoding="utf-8") as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def create_widgets(self):
        self.label_task = tk.Label(self.root, text="Нажмите 'Сгенерировать'", font=("Arial", 14), wraplength=500)
        self.label_task.pack(pady=20)

        btn_generate = tk.Button(self.root, text="Сгенерировать задачу", command=self.generate_task)
        btn_generate.pack(pady=5)

        filter_frame = tk.Frame(self.root)
        filter_frame.pack(pady=10)
        tk.Label(filter_frame, text="Фильтр по типу:").pack(side=tk.LEFT)
        self.filter_var = tk.StringVar(value="все")
        types = ["все", "учёба", "спорт", "работа"]
        self.filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var, values=types, state="readonly")
        self.filter_combo.pack(side=tk.LEFT, padx=5)
        self.filter_combo.bind("<<ComboboxSelected>>", lambda e: self.update_history_list())

        self.history_listbox = tk.Listbox(self.root, height=15)
        self.history_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=5, fill=tk.X, padx=10)
        tk.Label(add_frame, text="Новая задача:").pack(side=tk.LEFT)
        self.new_task_entry = tk.Entry(add_frame)
        self.new_task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.new_type_var = tk.StringVar(value="учёба")
        type_menu = ttk.Combobox(add_frame, textvariable=self.new_type_var, values=["учёба", "спорт", "работа"], state="readonly", width=8)
        type_menu.pack(side=tk.LEFT)
        btn_add = tk.Button(add_frame, text="Добавить", command=self.add_task)
        btn_add.pack(side=tk.LEFT, padx=5)

    def generate_task(self):
        if not self.tasks:
            messagebox.showwarning("Нет задач", "Список задач пуст. Добавьте новые задачи.")
            return
        chosen = random.choice(self.tasks)
        self.label_task.config(text=f"Текущая задача: {chosen['name']} (тип: {chosen['type']})")
        self.history.append(f"{chosen['name']} ({chosen['type']})")
        self.save_history()
        self.update_history_list()

    def update_history_list(self):
        self.history_listbox.delete(0, tk.END)
        filter_type = self.filter_var.get()
        for item in self.history:
            if filter_type == "все":
                self.history_listbox.insert(tk.END, item)
            elif f"({filter_type})" in item:
                self.history_listbox.insert(tk.END, item)

    def add_task(self):
        new_name = self.new_task_entry.get().strip()
        if not new_name:
            messagebox.showerror("Ошибка", "Название задачи не может быть пустым!")
            return
        self.tasks.append({"name": new_name, "type": self.new_type_var.get()})
        self.new_task_entry.delete(0, tk.END)
        messagebox.showinfo("Успех", f"Задача '{new_name}' добавлена!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomTaskGenerator(root)
    root.mainloop()
