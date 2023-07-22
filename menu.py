import os

def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Курсова робота з дисципліни \"Методи обчислення\" студента 124-21-1 Волкова Андрія (5 варіант)\n")

def MainMenu():
    ClearConsole()
    print("Головне меню:")
    print("1. Вибрати метод")
    print("2. Вихід\n")

def MethodMenu():
    ClearConsole()
    print("Меню методів:")
    print("1. Метод фундаментальної матриці")
    print("2. Метод Рунге-Кутта-Мерсона")
    print("3. Повернутись до головного меню\n")

def PrintValues(E, L, C, R, t0, dt, t1, eps):
    ClearConsole()
    print("Введені значення:")
    print("E =", E, "| L =", L, "| C =", C, "| R =", R, "| t0 =", t0, "| dt =", dt, "| t1 =", t1, "| eps =", eps)

def FillValues():
    E = 3
    L = 0.5
    C = 0.02
    R = 30
    t0 = 0
    dt = 0.01
    t1 = 2
    eps = 0.001
    ClearConsole()
    print("Меню вибору параметрів:")
    print("1. Використати із програми")
    print("2. Ввести вручну\n")
    choice = input("Ваш вибір: ")
    if choice == "1":
        pass
    elif choice == "2":
        t0 = input("Введіть початковий час (t0): ")
        dt = input("Введіть крок часу (dt): ")
        t1 = input("Введіть кінцевий час (t1): ")
        eps = input("Введіть точність (eps): ")
        E = input("Введіть Е: ")
        L = input("Введіть L: ")
        C = input("Введіть C: ")
        R = input("Введіть R: ")
    else:
        print("Невірний вибір. Спробуйте ще раз.")
        input("Натисніть Enter, щоб продовжити...")
        FillValues()
    print("Введені значення:")
    print("E = ", E)
    print("L = ", L)
    print("C = ", C)
    print("R = ", R)
    print("t0 = ", t0)
    print("dt = ", dt)
    print("t1 = ", t1)
    print("eps = ", eps)
    input("Натисніть Enter, щоб продовжити...")
    return E, L, C, R, t0, dt, t1, eps