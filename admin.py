from database import add_item, get_item, update_item, delete_item, get_all_items
import datetime


def admin_login(login, password):
    """
    Admin tizimga kirishi
    """
    # Admin uchun oddiy autentifikatsiya (amaliy loyihada bu xavfsizroq bo'lishi kerak)
    if login == "admin" and password == "admin123":
        return True
    return False


def add_product(name, price, quantity):
    """
    Yangi mahsulot qo'shish

    Args:
        name (str): Mahsulot nomi
        price (float): Narxi
        quantity (int): Miqdori

    Returns:
        int: Yangi mahsulot ID si
    """
    product_data = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return add_item("products", product_data)


def update_product(product_id, name=None, price=None, quantity=None):
    """
    Mahsulotni yangilash

    Args:
        product_id (int): Mahsulot ID si
        name (str, optional): Yangi nom
        price (float, optional): Yangi narx
        quantity (int, optional): Yangi miqdor

    Returns:
        bool: Muvaffaqiyatli yangilangan bo'lsa True
    """
    product = get_item("products", product_id)
    if not product:
        print(f"ID: {product_id} bo'lgan mahsulot topilmadi")
        return False

    # Faqat berilgan parametrlarni yangilash
    if name:
        product["name"] = name
    if price is not None:
        product["price"] = price
    if quantity is not None:
        product["quantity"] = quantity

    return update_item("products", product_id, product)


def delete_product(product_id):
    """
    Mahsulotni o'chirish

    Args:
        product_id (int): Mahsulot ID si

    Returns:
        bool: Muvaffaqiyatli o'chirilgan bo'lsa True
    """
    return delete_item("products", product_id)


def view_all_products():
    """
    Barcha mahsulotlarni ko'rish

    Returns:
        list: Mahsulotlar ro'yxati
    """
    return get_all_items("products")


def add_employee(name, role, check_in="09:00", check_out="18:00"):
    """
    Yangi xodim qo'shish

    Args:
        name (str): Xodim ismi
        role (str): Lavozimi
        check_in (str): Ish boshlash vaqti
        check_out (str): Ish tugash vaqti

    Returns:
        int: Yangi xodim ID si
    """
    employee_data = {
        "name": name,
        "role": role,
        "check_in": check_in,
        "check_out": check_out
    }
    return add_item("employees", employee_data)


def update_employee(employee_id, name=None, role=None, check_in=None, check_out=None):
    """
    Xodim ma'lumotlarini yangilash

    Args:
        employee_id (int): Xodim ID si
        name (str, optional): Yangi ism
        role (str, optional): Yangi lavozim
        check_in (str, optional): Yangi ish boshlash vaqti
        check_out (str, optional): Yangi ish tugash vaqti

    Returns:
        bool: Muvaffaqiyatli yangilangan bo'lsa True
    """
    employee = get_item("employees", employee_id)
    if not employee:
        print(f"ID: {employee_id} bo'lgan xodim topilmadi")
        return False

    # Faqat berilgan parametrlarni yangilash
    if name:
        employee["name"] = name
    if role:
        employee["role"] = role
    if check_in:
        employee["check_in"] = check_in
    if check_out:
        employee["check_out"] = check_out

    return update_item("employees", employee_id, employee)


def delete_employee(employee_id):
    """
    Xodimni o'chirish

    Args:
        employee_id (int): Xodim ID si

    Returns:
        bool: Muvaffaqiyatli o'chirilgan bo'lsa True
    """
    return delete_item("employees", employee_id)


def view_all_employees():
    """
    Barcha xodimlarni ko'rish

    Returns:
        list: Xodimlar ro'yxati
    """
    return get_all_items("employees")


def add_camera(location):
    """
    Yangi kamera qo'shish

    Args:
        location (str): Kamera joylashuvi

    Returns:
        int: Yangi kamera ID si
    """
    camera_data = {
        "location": location,
        "last_record": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    return add_item("cameras", camera_data)


def update_camera(camera_id, location=None):
    """
    Kamera ma'lumotlarini yangilash

    Args:
        camera_id (int): Kamera ID si
        location (str, optional): Yangi joylashuv

    Returns:
        bool: Muvaffaqiyatli yangilangan bo'lsa True
    """
    camera = get_item("cameras", camera_id)
    if not camera:
        print(f"ID: {camera_id} bo'lgan kamera topilmadi")
        return False

    if location:
        camera["location"] = location

    # Har doim so'nggi yozuv vaqtini yangilash
    camera["last_record"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    return update_item("cameras", camera_id, camera)


def delete_camera(camera_id):
    """
    Kamerani o'chirish

    Args:
        camera_id (int): Kamera ID si

    Returns:
        bool: Muvaffaqiyatli o'chirilgan bo'lsa True
    """
    return delete_item("cameras", camera_id)


def view_all_cameras():
    """
    Barcha kameralarni ko'rish

    Returns:
        list: Kameralar ro'yxati
    """
    return get_all_items("cameras")


def view_all_orders():
    """
    Barcha buyurtmalarni ko'rish

    Returns:
        list: Buyurtmalar ro'yxati
    """
    return get_all_items("orders")


def update_order_status(order_id, status):
    """
    Buyurtma holatini yangilash

    Args:
        order_id (int): Buyurtma ID si
        status (str): Yangi holat ('pending', 'completed', 'cancelled')

    Returns:
        bool: Muvaffaqiyatli yangilangan bo'lsa True
    """
    order = get_item("orders", order_id)
    if not order:
        print(f"ID: {order_id} bo'lgan buyurtma topilmadi")
        return False

    order["status"] = status
    return update_item("orders", order_id, order)


def admin_menu():
    """
    Admin uchun menyu
    """
    while True:
        print("\n===== ADMIN PANEL =====")
        print("1. Mahsulotlar bilan ishlash")
        print("2. Xodimlar bilan ishlash")
        print("3. Kameralar bilan ishlash")
        print("4. Buyurtmalarni ko'rish")
        print("0. Chiqish")

        choice = input("Tanlang: ")

        if choice == "1":
            product_menu()
        elif choice == "2":
            employee_menu()
        elif choice == "3":
            camera_menu()
        elif choice == "4":
            orders_menu()
        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov!")


def product_menu():
    """
    Mahsulotlar bilan ishlash menyusi
    """
    while True:
        print("\n----- MAHSULOTLAR -----")
        print("1. Barcha mahsulotlarni ko'rish")
        print("2. Yangi mahsulot qo'shish")
        print("3. Mahsulotni yangilash")
        print("4. Mahsulotni o'chirish")
        print("0. Orqaga")

        choice = input("Tanlang: ")

        if choice == "1":
            products = view_all_products()
            if products:
                print("\nMAHSULOTLAR:")
                for product in products:
                    print(
                        f"ID: {product['id']}, Nomi: {product['name']}, Narxi: {product['price']}, Miqdori: {product['quantity']}")
            else:
                print("Mahsulotlar yo'q")

        elif choice == "2":
            name = input("Mahsulot nomi: ")
            price = float(input("Narxi: "))
            quantity = int(input("Miqdori: "))

            product_id = add_product(name, price, quantity)
            if product_id:
                print(f"Mahsulot qo'shildi. ID: {product_id}")
            else:
                print("Mahsulot qo'shishda xatolik")

        elif choice == "3":
            product_id = int(input("Mahsulot ID si: "))
            name = input("Yangi nomi (o'zgartirmaslik uchun bo'sh qoldiring): ")
            price_str = input("Yangi narxi (o'zgartirmaslik uchun bo'sh qoldiring): ")
            quantity_str = input("Yangi miqdori (o'zgartirmaslik uchun bo'sh qoldiring): ")

            price = float(price_str) if price_str else None
            quantity = int(quantity_str) if quantity_str else None

            if update_product(product_id, name if name else None, price, quantity):
                print("Mahsulot yangilandi")
            else:
                print("Mahsulotni yangilashda xatolik")

        elif choice == "4":
            product_id = int(input("O'chiriladigan mahsulot ID si: "))

            if delete_product(product_id):
                print("Mahsulot o'chirildi")
            else:
                print("Mahsulotni o'chirishda xatolik")

        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov!")


def employee_menu():
    """
    Xodimlar bilan ishlash menyusi
    """
    while True:
        print("\n----- XODIMLAR -----")
        print("1. Barcha xodimlarni ko'rish")
        print("2. Yangi xodim qo'shish")
        print("3. Xodim ma'lumotlarini yangilash")
        print("4. Xodimni o'chirish")
        print("0. Orqaga")

        choice = input("Tanlang: ")

        if choice == "1":
            employees = view_all_employees()
            if employees:
                print("\nXODIMLAR:")
                for employee in employees:
                    print(f"ID: {employee['id']}, Ismi: {employee['name']}, Lavozimi: {employee['role']}, " +
                          f"Ish vaqti: {employee['check_in']} - {employee['check_out']}")
            else:
                print("Xodimlar yo'q")

        elif choice == "2":
            name = input("Xodim ismi: ")
            role = input("Lavozimi: ")
            check_in = input("Ish boshlash vaqti (masalan, 09:00): ")
            check_out = input("Ish tugash vaqti (masalan, 18:00): ")

            employee_id = add_employee(name, role, check_in, check_out)
            if employee_id:
                print(f"Xodim qo'shildi. ID: {employee_id}")
            else:
                print("Xodim qo'shishda xatolik")

        elif choice == "3":
            employee_id = int(input("Xodim ID si: "))
            name = input("Yangi ismi (o'zgartirmaslik uchun bo'sh qoldiring): ")
            role = input("Yangi lavozimi (o'zgartirmaslik uchun bo'sh qoldiring): ")
            check_in = input("Yangi ish boshlash vaqti (o'zgartirmaslik uchun bo'sh qoldiring): ")
            check_out = input("Yangi ish tugash vaqti (o'zgartirmaslik uchun bo'sh qoldiring): ")

            if update_employee(employee_id,
                               name if name else None,
                               role if role else None,
                               check_in if check_in else None,
                               check_out if check_out else None):
                print("Xodim ma'lumotlari yangilandi")
            else:
                print("Xodim ma'lumotlarini yangilashda xatolik")

        elif choice == "4":
            employee_id = int(input("O'chiriladigan xodim ID si: "))

            if delete_employee(employee_id):
                print("Xodim o'chirildi")
            else:
                print("Xodimni o'chirishda xatolik")

        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov!")


def camera_menu():
    """
    Kameralar bilan ishlash menyusi
    """
    while True:
        print("\n----- KAMERALAR -----")
        print("1. Barcha kameralarni ko'rish")
        print("2. Yangi kamera qo'shish")
        print("3. Kamera ma'lumotlarini yangilash")
        print("4. Kamerani o'chirish")
        print("0. Orqaga")

        choice = input("Tanlang: ")

        if choice == "1":
            cameras = view_all_cameras()
            if cameras:
                print("\nKAMERALAR:")
                for camera in cameras:
                    print(f"ID: {camera['id']}, Joylashuvi: {camera['location']}, " +
                          f"So'nggi yozuv: {camera['last_record']}")
            else:
                print("Kameralar yo'q")

        elif choice == "2":
            location = input("Kamera joylashuvi: ")

            camera_id = add_camera(location)
            if camera_id:
                print(f"Kamera qo'shildi. ID: {camera_id}")
            else:
                print("Kamera qo'shishda xatolik")

        elif choice == "3":
            camera_id = int(input("Kamera ID si: "))
            location = input("Yangi joylashuvi: ")

            if update_camera(camera_id, location):
                print("Kamera ma'lumotlari yangilandi")
            else:
                print("Kamera ma'lumotlarini yangilashda xatolik")

        elif choice == "4":
            camera_id = int(input("O'chiriladigan kamera ID si: "))

            if delete_camera(camera_id):
                print("Kamera o'chirildi")
            else:
                print("Kamerani o'chirishda xatolik")


        elif choice == "0":

            break

        else:

            print("Noto'g'ri tanlov!")


def orders_menu():
    """

    Buyurtmalar bilan ishlash menyusi

    """

    while True:

        print("\n----- BUYURTMALAR -----")

        print("1. Barcha buyurtmalarni ko'rish")

        print("2. Buyurtma holatini yangilash")

        print("0. Orqaga")

        choice = input("Tanlang: ")

        if choice == "1":

            orders = view_all_orders()

            if orders:

                print("\nBUYURTMALAR:")

                for order in orders:

                    print(f"ID: {order['id']}, Foydalanuvchi ID: {order['user_id']}, " +

                          f"Umumiy narx: {order['total_price']}, Holati: {order['status']}")

                    print("Mahsulotlar:")

                    for product in order['products']:
                        print(f"  Mahsulot ID: {product['product_id']}, Miqdori: {product['quantity']}")

                    print()

            else:

                print("Buyurtmalar yo'q")


        elif choice == "2":

            order_id = int(input("Buyurtma ID si: "))

            print("Holatlar: 'pending', 'completed', 'cancelled'")

            status = input("Yangi holat: ")

            if update_order_status(order_id, status):

                print("Buyurtma holati yangilandi")

            else:

                print("Buyurtma holatini yangilashda xatolik")


        elif choice == "0":

            break

        else:

            print("Noto'g'ri tanlov!")
