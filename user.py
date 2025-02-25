from database import add_user, get_users, update_user_balance

# Ro'yxatdan o'tish
def register():
    login = input("Login: ")
    password = input("Parol: ")
    add_user(login, password)
    print(f"Foydalanuvchi '{login}' muvaffaqiyatli ro'yxatdan o'tdi!")

# Tizimga kirish
def login():
    login = input("Login: ")
    password = input("Parol: ")
    users = get_users()
    user = next((u for u in users if u[1] == login and u[2] == password), None)
    if user:
        print(f"Xush kelibsiz, {login}!")
        return user[0]  # Foydalanuvchi ID-sini qaytaradi
    else:
        print("Login yoki parol noto'g'ri!")
        return None

# Balansni tekshirish
def check_balance(user_id):
    users = get_users()
    user = next((u for u in users if u[0] == user_id), None)
    if user:
        print(f"Sizning balansingiz: {user[3]}")
    else:
        print("Foydalanuvchi topilmadi!")

# Balansni to'ldirish
def add_balance(user_id):
    amount = float(input("Qancha miqdorda to'ldirmoqchisiz? "))
    users = get_users()
    user = next((u for u in users if u[0] == user_id), None)
    if user:
        new_balance = user[3] + amount
        update_user_balance(user_id, new_balance)
        print(f"Balansingiz muvaffaqiyatli yangilandi! Joriy balans: {new_balance}")
    else:
        print("Foydalanuvchi topilmadi!")

# Buyurtmalar tarixini ko'rish
def view_order_history(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT orders.id, products.name, orders.quantity, orders.total_price, orders.status
        FROM orders
        JOIN products ON orders.product_id = products.id
        WHERE orders.user_id = ?
    ''', (user_id,))
    orders = cursor.fetchall()
    conn.close()

    if orders:
        print("\nBuyurtmalar tarixi:")
        for order in orders:
            print(f"ID: {order[0]}, Mahsulot: {order[1]}, Soni: {order[2]}, Narxi: {order[3]}, Holati: {order[4]}")
    else:
        print("Sizda hali buyurtmalar mavjud emas.")

# Foydalanuvchi menyusi
def user_menu(user_id):
    while True:
        print("\n--- Foydalanuvchi Panel ---")
        print("1. Balansni tekshirish")
        print("2. Balansni to'ldirish")
        print("3. Buyurtmalar tarixini ko'rish")
        print("4. Chiqish")
        choice = input("Tanlang: ")

        if choice == "1":
            check_balance(user_id)
        elif choice == "2":
            add_balance(user_id)
        elif choice == "3":
            view_order_history(user_id)
        elif choice == "4":
            print("Foydalanuvchi panelidan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov!")

# Asosiy funksiya
if __name__ == "__main__":
    print("--- Foydalanuvchi Tizimi ---")
    print("1. Ro'yxatdan o'tish")
    print("2. Tizimga kirish")
    choice = input("Tanlang: ")

    if choice == "1":
        register()
    elif choice == "2":
        user_id = login()
        if user_id:
            user_menu(user_id)
    else:
        print("Noto'g'ri tanlov!")