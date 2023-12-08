def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def find_value(text_file, num_value):
    try:
        with open(text_file, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    time_str, value = parts
                    value = float(value)

                    if value > num_value:
                        print(f"Час: {time_str}, Значення: {value}")

    except FileNotFoundError:
        print("Файл не знайдено")
    except ValueError:
        print("Помилка у форматі файлу")

while True:
    text_file = "text.txt"
    num_value = input("Введіть значення у вигляді AAA або введіть 'exit' для виходу: ")

    if num_value.lower() == 'exit':
        break
    elif not is_number(num_value):
        print("Введено не число. Спробуйте ще раз.")
        continue

    num_value = float(num_value)
    find_value(text_file, num_value)
