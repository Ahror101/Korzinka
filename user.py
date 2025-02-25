import sqlite3
from database import create_connection

# Ro‘yxatdan o‘tish funksiyasi
def register_user(name, login, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, login, password) VALUES (?, ?, ?)", (name, login, password))
        conn.commit()
        print("Foydalanuvchi muvaffaqiyatli qo‘shildi.")
    except sqlite3.IntegrityError:
        print("Bu login allaqachon mavjud!")
    conn.close()

# Foydalanuvchi login qilish funksiyasi
def login_user(login, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Tizimga muvaffaqiyatli kirdingiz!")
        return user
    else:
        print("Login yoki parol noto‘g‘ri!")
        return None
