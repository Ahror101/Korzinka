from database import (
    add_product,
    delete_product,
    get_products,
    add_employee,
    create_connection,
    update_user_balance
)

# Admin ma'lumotlari (real loyihada bu bazadan olinishi kerak)
ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "admin123"


# Admin kirishni tekshirish
def admin_login():
    login = input("Login: ")
    password = input("Parol: ")
    if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:
        print("Admin sifatida tizimga kirdingiz!")
        return True
    else:
        print("Login yoki parol noto'g'ri!")
        return False


# Mahsulot qo'shish
def add_new_product():
    name = input("Mahsulot nomi: ")
    price = float(input("Narxi: "))
    quantity = int(input("Soni: "))
    add_product(name, price, quantity)
    print(f"Mahsulot '{name}' muvaffaqiyatli qo'shildi!")


# Mahsulotni o'chirish
def remove_product():
    products = get_products()
    print("Mavjud mahsulotlar:")
    for product in products:
        print(f"ID: {product[0]}, Nomi: {product[1]}, Narxi: {product[2]}, Soni: {product[3]}")

    product_id = int(input("O'chirmoqchi bo'lgan mahsulot ID-sini kiriting: "))
    delete_product(product_id)
    print(f"Mahsulot ID {product_id} muvaffaqiyatli o'chirildi!")


# Xodim qo'shish
def add_new_employee():
    name = input("Xodim ismi: ")
    position = input("Lavozimi: ")
    check_in = input("Kelish vaqti (masalan, 09:00): ")
    check_out = input("Ketish vaqti (masalan, 18:00): ")
    add_employee(name, position, check_in, check_out)
    print(f"Xodim '{name}' muvaffaqiyatli qo'shildi!")


# Xodimlar ro'yxatini ko'rish
def view_employees():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()

    print("Xodimlar ro'yxati:")
    for employee in employees:
        print(
            f"ID: {employee[0]}, Ismi: {employee[1]}, Lavozimi: {employee[2]}, Kelish: {employee[3]}, Ketish: {employee[4]}")


# Admin menyusi
def admin_menu():
    while True:
        print("\n--- Admin Panel ---")
        print("1. Mahsulot qo'shish")
        print("2. Mahsulot o'chirish")
        print("3. Xodim qo'shish")
        print("4. Xodimlar ro'yxatini ko'rish")
        print("5. Chiqish")
        choice = input("Tanlang: ")

        if choice == "1":
            add_new_product()
        elif choice == "2":
            remove_product()
        elif choice == "3":
            add_new_employee()
        elif choice == "4":
            view_employees()
        elif choice == "5":
            print("Admin panelidan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov!")


# Asosiy funksiya
if __name__ == "__main__":
    if admin_login():
        admin_menu()