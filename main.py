from user import register_user, login_user
from admin import admin_panel

def main():
    while True:
        print("\n1. Ro‘yxatdan o‘tish")
        print("2. Tizimga kirish")
        print("3. Chiqish")
        choice = input("Tanlovingiz: ")

        if choice == "1":
            name = input("Ism: ")
            login = input("Login: ")
            password = input("Parol: ")
            register_user(name, login, password)

        elif choice == "2":
            login = input("Login: ")
            password = input("Parol: ")
            user = login_user(login, password)
            if user:
                if user[1] == "admin":  # Agar admin bo‘lsa
                    admin_panel()
                else:
                    print("Foydalanuvchilar paneli hali qo‘shilmagan.")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
