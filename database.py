import sqlite3

# Bazaga ulanish
def create_connection():
    conn = sqlite3.connect('shop.db')
    return conn

# Jadval yaratish
def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Users jadvali
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')

    # Products jadvali
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    # Orders jadvali
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            total_price REAL NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')

    # Employees jadvali
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            check_in TEXT,
            check_out TEXT
        )
    ''')

    conn.commit()
    conn.close()

# CRUD funksiyalari
# Foydalanuvchi qo'shish
def add_user(login, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (login, password) VALUES (?, ?)', (login, password))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Xatolik: Bu login allaqachon mavjud!")
    finally:
        conn.close()

# Mahsulot qo'shish
def add_product(name, price, quantity):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
    conn.commit()
    conn.close()

# Buyurtma qo'shish
def add_order(user_id, product_id, quantity, total_price):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (user_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)',
                   (user_id, product_id, quantity, total_price))
    conn.commit()
    conn.close()

# Xodim qo'shish
def add_employee(name, position, check_in, check_out):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, position, check_in, check_out) VALUES (?, ?, ?, ?)',
                   (name, position, check_in, check_out))
    conn.commit()
    conn.close()

# Ma'lumotlarni o'qish
def get_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Ma'lumotlarni yangilash
def update_user_balance(user_id, new_balance):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (new_balance, user_id))
    conn.commit()
    conn.close()

# Ma'lumotlarni o'chirish
def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

# Dastlabki sozlash
if __name__ == "__main__":
    create_tables()
    print("Jadvallar muvaffaqiyatli yaratildi!")
