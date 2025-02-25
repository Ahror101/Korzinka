from database import get_products, add_order

# Mahsulotlarni ko'rish
def view_products():
    products = get_products()
    print("\nMavjud mahsulotlar:")
    for product in products:
        print(f"ID: {product[0]}, Nomi: {product[1]}, Narxi: {product[2]}, Soni: {product[3]}")

# Savatni ko'rish
def view_cart(cart):
    if not cart:
        print("Savatingiz bo'sh.")
        return
    print("\nSavatingizdagi mahsulotlar:")
    for item in cart:
        print(f"ID: {item['id']}, Nomi: {item['name']}, Narxi: {item['price']}, Soni: {item['quantity']}")

# Savatga mahsulot qo'shish
def add_to_cart(cart, products):
    product_id = int(input("Qo'shmoqchi bo'lgan mahsulot ID-sini kiriting: "))
    quantity = int(input("Soni: "))

    # Mahsulotni tekshirish
    product = next((p for p in products if p[0] == product_id), None)
    if product:
        if product[3] >= quantity:
            cart.append({
                'id': product[0],
                'name': product[1],
                'price': product[2],
                'quantity': quantity
            })
            print(f"{product[1]} savatga qo'shildi!")
        else:
            print("Xatolik: Mavjud mahsulot soni yetarli emas!")
    else:
        print("Xatolik: Bunday ID-li mahsulot mavjud emas!")

# Savatdan mahsulot olib tashlash
def remove_from_cart(cart):
    if not cart:
        print("Savatingiz bo'sh.")
        return

    view_cart(cart)
    product_id = int(input("O'chirmoqchi bo'lgan mahsulot ID-sini kiriting: "))
    cart[:] = [item for item in cart if item['id'] != product_id]
    print("Mahsulot savatdan o'chirildi!")

# Buyurtmani tasdiqlash
def confirm_order(user_id, cart):
    if not cart:
        print("Savatingiz bo'sh. Buyurtma berish uchun avval mahsulot qo'shing.")
        return

    total_price = sum(item['price'] * item['quantity'] for item in cart)
    print(f"\nUmumiy narx: {total_price}")

    confirm = input("Buyurtmani tasdiqlaysizmi? (ha/yo'q): ").lower()
    if confirm == "ha":
        for item in cart:
            add_order(user_id, item['id'], item['quantity'], item['price'] * item['quantity'])
        print("Buyurtma muvaffaqiyatli tasdiqlandi!")
        cart.clear()
    else:
        print("Buyurtma bekor qilindi.")

# Do'kon menyusi
def shop_menu(user_id):
    cart = []
    while True:
        print("\n--- Do'kon ---")
        print("1. Mahsulotlarni ko'rish")
        print("2. Savatga mahsulot qo'shish")
        print("3. Savatni ko'rish")
        print("4. Savatdan mahsulot olib tashlash")
        print("5. Buyurtmani tasdiqlash")
        print("6. Chiqish")
        choice = input("Tanlang: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            products = get_products()
            add_to_cart(cart, products)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            remove_from_cart(cart)
        elif choice == "5":
            confirm_order(user_id, cart)
        elif choice == "6":
            print("Do'kondan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov!")

# Asosiy funksiya
if __name__ == "__main__":
    user_id = 1  # Misol uchun foydalanuvchi ID-si
    shop_menu(user_id)