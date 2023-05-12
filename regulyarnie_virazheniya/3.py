import re

def find_time(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    pattern = r"\b[01]\d:[0-5]\d\b|2[0-3]:[0-5]\d\b" # шаблон для поиска времени
    times = re.findall(pattern, text)
    return times

# пример использования функции
file_path = "reg_task_3.txt"
times = find_time(file_path)
print(times)