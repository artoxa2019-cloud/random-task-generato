import tkinter as tk
from tkinter import messagebox

def generate_table():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите положительное целое число.")
        return

    # Очистка предыдущей таблицы
    for widget in frame.winfo_children():
        widget.destroy()

    # Заголовки (верхняя строка)
    for i in range(n + 1):
        bg_color = 'lightgray' if i == 0 else 'white'
        label = tk.Label(frame, text=i if i > 0 else '', width=5, height=2, relief='ridge', bg=bg_color)
        label.grid(row=0, column=i, padx=1, pady=1)

    # Столбец слева и ячейки таблицы
    for row in range(1, n + 1):
        # Левый столбец (множители)
        label = tk.Label(frame, text=row, width=5, height=2, relief='ridge', bg='lightgray')
        label.grid(row=row, column=0, padx=1, pady=1)

        for col in range(1, n + 1):
            result = row * col
            bg_color = 'white'
            label = tk.Label(frame, text=result, width=5, height=2, relief='ridge', bg=bg_color)
            label.grid(row=row, column=col, padx=1, pady=1)

# Создание окна
root = tk.Tk()
root.title("Таблица умножения")

# Поле ввода и кнопка
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Введите N:").pack(side='left')
entry = tk.Entry(frame_input)
entry.pack(side='left', padx=5)

tk.Button(root, text="Построить таблицу", command=generate_table).pack(pady=5)

# Рамка для таблицы
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

root.mainloop()
