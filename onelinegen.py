def calculate_bonus(names, salary, bonus):
    result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}

    return result

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

"""
# Возможность добавления новых записей
    while True:
        add_new = input("Хотите добавить новые данные? (да/нет): ").strip().lower()
        if add_new == 'да':
            name = input("Введите имя: ").strip()
            try:
                sal = float(input("Введите зарплату: ").strip())
                bon = input("Введите бонус (например, 15%): ").strip()
                
                # Проверка формата бонуса
                if not bon.endswith('%') or not bon[:-1].isdigit():
                    print("Некорректный формат бонуса! Пример корректного формата: 10%")
                    continue
                
                # Добавляем данные
                names.append(name)
                salary.append(sal)
                bonus.append(bon)
                print("Данные добавлены.")
            except ValueError:
                print("Некорректный ввод. Убедитесь, что зарплата — число.")
        elif add_new == 'нет':
            break
        else:
            print("Введите 'да' или 'нет'.")
"""

result = calculate_bonus(names, salary, bonus)
print(result)
