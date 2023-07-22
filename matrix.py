import numpy as np
import matplotlib.pyplot as plt
from menu import FillValues, PrintValues
import pandas as pd

def matrix_exponential(A, t):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    D = np.diag(np.exp(eigenvalues * t))
    P = eigenvectors
    P_inv = np.linalg.inv(P)
    return np.dot(np.dot(P, D), P_inv)

def MatrixResolve():
    E, L, C, R, t0, dt, t1, eps = FillValues()
    y1 = 0
    y2 = E / (R * C)
    a11 = 0
    a12 = 1
    a21 = -1 / (L * C)
    a22 = -R / L
    A = np.array([[a11, a12],
                  [a21, a22]])
    
    y0 = np.array([y1, y2])

    y_values = []
    t_points = np.linspace(t0, t1, round((t1 - t0) / dt))
    for t in t_points:
        solution = matrix_exponential(A, t)
        y_values.append(np.dot(solution, y0))

    y1_values = [y[0] for y in y_values]
    y2_values = [y[1] for y in y_values]

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
            MatrixResolve()
        plt.legend()
        plt.show()
    elif choice1 == "3":
        pass
    else:
        print("Невірний вибір. Спробуйте ще раз.")

    input("Натисніть Enter, щоб продовжити...")