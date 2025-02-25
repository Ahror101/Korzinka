from shop import add_product, get_products

# Admin paneli funksiyasi
def admin_panel():
    while True:
        print("\nAdmin paneli")
        print("1. Mahsulot qo‘shish")
        print("2. Mahsulotlarni ko‘rish")
        print("3. Chiqish")
        choice = input("Tanlovingiz: ")

        if choice == "1":
            name = input("Mahsulot nomi: ")
            price = float(input("Narxi: "))
            quantity = int(input("Miqdori: "))
            add_product(name, price, quantity)
        elif choice == "2":
            products = get_products()
            for p in products:
                print(p)
        elif choice == "3":
            break

if __name__ == "__main__":
    admin_panel()
