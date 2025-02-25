import admin
import user

# Asosiy menyuni yaratish
def main_menu():
    while True:
        print("\n--- Asosiy Menyu ---")
        print("1. Admin sifatida kirish")
        print("2. Foydalanuvchi sifatida kirish")
        print("3. Dasturdan chiqish")
        choice = input("Tanlang: ")

        if choice == "1":
            print("\n--- Admin Tizimi ---")
            admin.admin_menu()
        elif choice == "2":
            print("\n--- Foydalanuvchi Tizimi ---")
            # Foydalanuvchi login qiladi va user_id olinadi
            user_id = user.login()
            if user_id:
                user.user_menu(user_id)  # user_id ni uzatamiz
        elif choice == "3":
            print("Dasturdan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov!")

# Asosiy funksiya
if __name__ == "__main__":
    main_menu()