import sqlite3
from database import create_connection

# Mahsulot qo‘shish funksiyasi
def add_product(name, price, quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    conn.close()

# Mahsulotlarni ko‘rish funksiyasi
def get_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

if __name__ == "__main__":
    print(get_products())
