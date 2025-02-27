from user import register_user, login_user, user_menu
from admin import admin_login, admin_menu
from security import security_menu


def main():
    """
    Asosiy dastur
    """
    print("===== KARZINKA DO'KONI =====")

    while True:
        print("\nASSOSIY MENYU:")
        print("1. Tizimga kirish")
        print("2. Ro'yxatdan o'tish")
        print("3. Admin sifatida kirish")
        print("4. Xavfsizlik bo'limi")
        print("0. Chiqish")

        choice = input("Tanlang: ")

        if choice == "1":
            login = input("Login: ")
            password = input("Parol: ")

            user = login_user(login, password)
            if user:
                user_menu(user)

        elif choice == "2":
            name = input("Ismingiz: ")
            login = input("Login: ")
            password = input("Parol: ")

            user_id = register_user(name, login, password)
            if user_id:
                print(f"Ro'yxatdan o'tdingiz. Foydalanuvchi ID: {user_id}")
                print("Endi tizimga kirishingiz mumkin.")

        elif choice == "3":
            login = input("Admin login: ")
            password = input("Admin parol: ")

            if admin_login(login, password):
                admin_menu()
            else:
                print("Noto'g'ri login yoki parol")

        elif choice == "4":
            security_menu()

        elif choice == "0":
            print("Dastur yakunlandi. Xayr!")
            break

        else:
            print("Noto'g'ri tanlov!")


if __name__ == "__main__":
    main()