def show_menu():
    print("\n=== TODO LIST CLI ===")
    print("1. Посмотреть список задач")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выйти")

def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("\nВыберите действие (1-4): ").strip()
        
        if choice == "1":
            if not tasks:
                print("\nСписок задач пуст.")
            else:
                print("\nВаши задачи:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    
        elif choice == "2":
            task = input("Введите название задачи: ").strip()
            if task:
                tasks.append(task)
                print(f"Задача '{task}' добавлена!")
            else:
                print("Задача не может быть пустой.")
                
        elif choice == "3":
            if not tasks:
                print("\nСписок задач пуст, нечего удалять.")
                continue
            
            try:
                num = int(input("Введите номер задачи для удаления: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Задача '{removed}' удалена!")
                else:
                    print("Некорректный номер задачи.")
            except ValueError:
                print("Пожалуйста, введите число.")
                
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()