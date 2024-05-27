# Lab Assignment: Lab 3
# Program Name: DataSerialization
# Developer: Arseniy Reshetnev
# Date: 2024-04-13
from tasks.task1 import task1
from tasks.task2 import task2
from tasks.task3 import task3
from tasks.task4 import task4
from tasks.task5 import task5


def print_menu():
    print("Меню:")
    print("1. Задание 1")
    print("2. Задание 2")
    print("3. Задание 3")
    print("4. Задание 4")
    print("5. Задание 5")


def main():
    while True:
        print_menu()
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "0":
            print("Программа завершена.")
            exit(0)
        else:
            print("Некорректный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()