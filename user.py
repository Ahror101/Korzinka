from database import add_item, get_item, update_item, search_items, get_all_items


def register_user(name, login, password):
    """
    Yangi foydalanuvchi ro'yxatdan o'tkazish

    Args:
        name (str): Foydalanuvchi ismi
        login (str): Login
        password (str): Parol

    Returns:
        int: Yangi foydalanuvchi ID si yoki None
    """
    # Login band emasligini tekshirish
    existing_users = search_items("users", "login", login)
    if existing_users:
        print(f"'{login}' logini band. Boshqa login tanlang.")
        return None

    user_data = {
        "name": name,
        "login": login,
        "password": password,
        "balance": 0  # Boshlang'ich balans 0
    }

    return add_item("users", user_data)


def login_user(login, password):
    """
    Foydalanuvchi tizimga kirishi

    Args:
        login (str): Login
        password (str): Parol

    Returns:
        dict: Foydalanuvchi ma'lumotlari yoki None
    """
    users = search_items("users", "login", login)
    if not users:
        print(f"'{login}' logini topilmadi")
        return None

    user = users[0]
    if user["password"] != password:
        print("Noto'g'ri parol")
        return None

    return user


def add_balance(user_id, amount):
    """
    Foydalanuvchi balansini to'ldirish

    Args:
        user_id (int): Foydalanuvchi ID si
        amount (float): Qo'shiladigan summa

    Returns:
        bool: Muvaffaqiyatli to'ldirilgan bo'lsa True
    """
    user = get_item("users", user_id)
    if not user:
        print(f"ID: {user_id} bo'lgan foydalanuvchi topilmadi")
        return False

    user["balance"] += amount
    return update_item("users", user_id, user)


def get_user_orders(user_id):
    """
    Foydalanuvchi buyurtmalarini olish

    Args:
        user_id (int): Foydalanuvchi ID si

    Returns:
        list: Buyurtmalar ro'yxati
    """
    all_orders = get_all_items("orders")
    return [order for order in all_orders if order["user_id"] == user_id]


def user_menu(user):
    """
    Foydalanuvchi menyusi

    Args:
        user (dict): Foydalanuvchi ma'lumotlari
    """
    from shop import shop_menu

    while True:
        print(f"\n===== FOYDALANUVCHI MENYUSI =====")
        print(f"Salom, {user['name']}! Balans: {user['balance']}")
        print("1. Do'konga kirish")
        print("2. Balansni to'ldirish")
        print("3. Buyurtmalar tarixini ko'rish")
        print("0. Chiqish")

        choice = input("Tanlang: ")

        if choice == "1":
            shop_menu(user["id"])

        elif choice == "2":
            try:
                amount = float(input("Summa: "))
                if amount <= 0:
                    print("Summa musbat bo'lishi kerak")
                    continue

                if add_balance(user["id"], amount):
                    user["balance"] += amount
                    print(f"Balans to'ldirildi. Yangi balans: {user['balance']}")
                else:
                    print("Balansni to'ldirishda xatolik")
            except ValueError:
                print("Noto'g'ri summa")

        elif choice == "3":
            orders = get_user_orders(user["id"])
            if orders:
                print("\nBUYURTMALAR TARIXI:")
                for order in orders:
                    print(f"Buyurtma ID: {order['id']}, Umumiy narx: {order['total_price']}, Holati: {order['status']}")
                    print("Mahsulotlar:")
                    for product_item in order["products"]:
                        product = get_item("products", product_item["product_id"])
                        if product:
                            print(f"  {product['name']}, Miqdori: {product_item['quantity']}")
                        else:
                            print(f"  Mahsulot ID: {product_item['product_id']}, Miqdori: {product_item['quantity']}")
                    print()
            else:
                print("Buyurtmalar yo'q")

        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov!")