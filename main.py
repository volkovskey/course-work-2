from matrix import MatrixResolve
from runge_kutta_merson import RKM
from menu import MainMenu, MethodMenu

if __name__ == "__main__":
    while True:
        MainMenu()
        choice = input("Ваш вибір: ")
        if choice == "1":
            MethodMenu()
            choice = input("Ваш вибір: ")
            if choice == "1":
                MatrixResolve()
            elif choice == "2":
                RKM()
            elif choice == "3":
                continue
            else:
                print("Невірний вибір. Спробуйте ще раз.")
                input("Натисніть Enter, щоб продовжити...")
        elif choice == "2":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            input("Натисніть Enter, щоб продовжити...")