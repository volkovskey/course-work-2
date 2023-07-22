import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from menu import FillValues, PrintValues

def f(t, y):
    y1, y2 = y
    dy1_dt = y2
    dy2_dt = -100 * y1 - 60 * y2
    return np.array([dy1_dt, dy2_dt])

def runge_kutta_merson(y0, t0, t_end, h_init, epsilon):
    t_points = [t0]
    y_points = [y0]
    h = h_init

    while t_points[-1] < t_end:
        t_n = t_points[-1]
        y_n = y_points[-1]

        k0 = h * f(t_n, y_n)
        k1 = h * f(t_n + 1/3 * h, y_n + 1/3 * k0)
        k2 = h * f(t_n + 1/3 * h, y_n + 1/6 * k0 + 1/6 * k1)
        k3 = h * f(t_n + 0.5 * h, y_n + 1/8 * k0 + 3/8 * k2)
        k4 = h * f(t_n + h, y_n + 1/2 * k0 - 3/2 * k2 + 2 * k3)

        y_next = y_n + (k0 + 4 * k3 + k4) / 6

        # Compute the error estimate
        R = (-2 * k0 + 9 * k2 - 8 * k3 + k4) / 30

        # Adjust the step size based on the error estimate and epsilon
        if np.linalg.norm(R) > epsilon:
            h *= 0.5
        elif epsilon / 30 <= np.linalg.norm(R) <= epsilon:
            t_points.append(t_n + h)
            y_points.append(y_next)
            h *= 2
        else:
            t_points.append(t_n + h)
            y_points.append(y_next)

    return t_points, y_points

def RKM():
    E, L, C, R, t0, dt, t1, eps = FillValues()
    y1 = 0
    y2 = E / (R * C)
    a11 = 0
    a12 = 1
    a21 = -1 / (L * C)
    a22 = -R / L
    h_init = 0.1
    A = np.array([[a11, a12],
                  [a21, a22]])
    
    y0 = np.array([y1, y2])

    t_points, y_points = runge_kutta_merson(y0, t0, t1, h_init, eps)
        
    y1_values = [y[0] for y in y_points]
    y2_values = [y[1] for y in y_points]

    PrintValues(E, L, C, R, t0, dt, t1, eps)
    print("Меню вибору виводу:")
    print("1. Вивести в консоль")
    print("2. Вивести в графік")
    print("3. Повернутись до головного меню\n")
    choice1 = input("Ваш вибір: ")
    choice2 = 1

    if choice1 == "2":
        print("Оберіть функцію:")
        print("1. Напруга на конденсаторі")
        print("2. Зміна напруги на конденсаторі")
        print("3. Обидві функції\n")
        choice2 = input("Ваш вибір: ")

    if choice1 == "1":
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        df = pd.DataFrame({'Час, c': t_points, 'y1, Напруга на конденсаторі, В': y1_values, 'y2, Зміна напруги на конденсаторі, В/с': y2_values})
        print(df)
    elif choice1 == "2":
        plt.figure(figsize=(20, 10))
        plt.title("Графік залежності напруги від часу")
        plt.xlabel("Час, c")
        plt.ylabel("Напруга, В або зміна напруги, В/с")
        plt.grid()
        if choice2 == "1" or choice2 == "3":
            plt.plot(t_points, y1_values, label='y1, Напруга на конденсаторі, В')
        if choice2 == "2" or choice2 == "3":
            plt.plot(t_points, y2_values, label='y2, Зміна напруги на конденсаторі, В/с')
        if choice2 != "1" and choice2 != "2" and choice2 != "3":
            print("Невірний вибір. Спробуйте ще раз.")
            input("Натисніть Enter, щоб продовжити...")
            RKM()
        plt.legend()
        plt.show()
    elif choice1 == "3":
        pass
    else:
        print("Невірний вибір. Спробуйте ще раз.")

    input("Натисніть Enter, щоб продовжити...")