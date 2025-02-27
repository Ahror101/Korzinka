from database import get_item, get_all_items, update_item, add_item


class Cart:
    def __init__(self, user_id):
        """
        Savat yaratish

        Args:
            user_id (int): Foydalanuvchi ID si
        """
        self.user_id = user_id
        self.items = []  # [{"product_id": id, "quantity": qty}, ...]
        self.total_price = 0

    def add_product(self, product_id, quantity=1):
        """
        Savatga mahsulot qo'shish

        Args:
            product_id (int): Mahsulot ID si
            quantity (int): Miqdori

        Returns:
            bool: Muvaffaqiyatli qo'shilgan bo'lsa True
        """
        # Mahsulotni tekshirish
        product = get_item("products", product_id)
        if not product:
            print(f"ID: {product_id} bo'lgan mahsulot topilmadi")
            return False

        # Omborda yetarli mahsulot borligini tekshirish
        if product["quantity"] < quantity:
            print(f"Omborda faqat {product['quantity']} dona {product['name']} mavjud")
            return False

        # Agar mahsulot allaqachon savatda bo'lsa, miqdorini oshirish
        for item in self.items:
            if item["product_id"] == product_id:
                item["quantity"] += quantity
                self._update_total_price()
                return True

        # Yangi mahsulot qo'shish
        self.items.append({
            "product_id": product_id,
            "quantity": quantity
        })

        self._update_total_price()
        return True

    def remove_product(self, product_id, quantity=None):
        """
        Savatdan mahsulotni olib tashlash

        Args:
            product_id (int): Mahsulot ID si
            quantity (int, optional): Olib tashlanadigan miqdor. None bo'lsa, to'liq olib tashlash.

        Returns:
            bool: Muvaffaqiyatli olib tashlangan bo'lsa True
        """
        for i, item in enumerate(self.items):
            if item["product_id"] == product_id:
                if quantity is None or quantity >= item["quantity"]:
                    # Mahsulotni to'liq olib tashlash
                    del self.items[i]
                else:
                    # Miqdorni kamaytirish
                    item["quantity"] -= quantity

                self._update_total_price()
                return True

        print(f"ID: {product_id} bo'lgan mahsulot savatda topilmadi")
        return False

    def clear(self):
        """
        Savatni tozalash
        """
        self.items = []
        self.total_price = 0

    def _update_total_price(self):
        """
        Umumiy narxni yangilash
        """
        self.total_price = 0
        for item in self.items:
            product = get_item("products", item["product_id"])
            if product:
                self.total_price += product["price"] * item["quantity"]

    def view_cart(self):
        """
        Savatni ko'rish

        Returns:
            dict: Savat ma'lumotlari
        """
        cart_items = []
        for item in self.items:
            product = get_item("products", item["product_id"])
            if product:
                cart_items.append({
                    "product_id": item["product_id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": item["quantity"],
                    "subtotal": product["price"] * item["quantity"]
                })

        return {
            "items": cart_items,
            "total_price": self.total_price
        }

    def checkout(self):
        """
        Buyurtmani tasdiqlash

        Returns:
            int: Buyurtma ID si yoki None
        """
        if not self.items:
            print("Savat bo'sh")
            return None

        # Foydalanuvchini tekshirish
        user = get_item("users", self.user_id)
        if not user:
            print(f"ID: {self.user_id} bo'lgan foydalanuvchi topilmadi")
            return None

        # Foydalanuvchi balansini tekshirish
        if user["balance"] < self.total_price:
            print(f"Yetarli mablag' yo'q. Balans: {user['balance']}, Kerak: {self.total_price}")
            return None

        # Mahsulotlar miqdorini tekshirish va yangilash
        for item in self.items:
            product = get_item("products", item["product_id"])
            if not product:
                print(f"ID: {item['product_id']} bo'lgan mahsulot topilmadi")
                return None

            if product["quantity"] < item["quantity"]:
                print(f"Omborda faqat {product['quantity']} dona {product['name']} mavjud")
                return None

            # Mahsulot miqdorini kamaytirish
            product["quantity"] -= item["quantity"]
            update_item("products", item["product_id"], product)

        # Foydalanuvchi balansini kamaytirish
        user["balance"] -= self.total_price
        update_item("users", self.user_id, user)

        # Buyurtma yaratish
        order_data = {
            "user_id": self.user_id,
            "products": self.items,
            "total_price": self.total_price,
            "status": "pending"
        }

        order_id = add_item("orders", order_data)

        # Savatni tozalash
        self.clear()

        return order_id


def view_all_products():
    """
    Barcha mahsulotlarni ko'rish

    Returns:
        list: Mahsulotlar ro'yxati
    """
    return get_all_items("products")


def get_product(product_id):
    """
    Mahsulot ma'lumotlarini olish

    Args:
        product_id (int): Mahsulot ID si

    Returns:
        dict: Mahsulot ma'lumotlari
    """
    return get_item("products", product_id)


def shop_menu(user_id):
    """
    Do'kon menyusi

    Args:
        user_id (int): Foydalanuvchi ID si
    """
    cart = Cart(user_id)

    while True:
        print("\n===== DO'KON =====")
        print("1. Mahsulotlarni ko'rish")
        print("2. Savatni ko'rish")
        print("3. Savatga mahsulot qo'shish")
        print("4. Savatdan mahsulot olib tashlash")
        print("5. Savatni tozalash")
        print("6. Buyurtmani tasdiqlash")
        print("0. Chiqish")

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
            cart_data = cart.view_cart()
            if cart_data["items"]:
                print("\nSAVAT:")
                for item in cart_data["items"]:
                    print(
                        f"Nomi: {item['name']}, Narxi: {item['price']}, Miqdori: {item['quantity']}, Jami: {item['subtotal']}")
                print(f"\nUmumiy narx: {cart_data['total_price']}")
            else:
                print("Savat bo'sh")

        elif choice == "3":
            product_id = int(input("Mahsulot ID si: "))
            quantity = int(input("Miqdori: "))

            if cart.add_product(product_id, quantity):
                print("Mahsulot savatga qo'shildi")
            else:
                print("Mahsulotni savatga qo'shishda xatolik")

        elif choice == "4":
            product_id = int(input("Mahsulot ID si: "))
            quantity_str = input("Miqdori (to'liq olib tashlash uchun bo'sh qoldiring): ")

            quantity = int(quantity_str) if quantity_str else None

            if cart.remove_product(product_id, quantity):
                print("Mahsulot savatdan olib tashlandi")
            else:
                print("Mahsulotni savatdan olib tashlashda xatolik")

        elif choice == "5":
            cart.clear()
            print("Savat tozalandi")

        elif choice == "6":
            order_id = cart.checkout()
            if order_id:
                print(f"Buyurtma tasdiqlandi. Buyurtma ID: {order_id}")
            else:
                print("Buyurtmani tasdiqlashda xatolik")

        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov!")