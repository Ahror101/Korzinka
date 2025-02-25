import sqlite3
from datetime import datetime


# Bazaga ulanish
def create_connection():
    conn = sqlite3.connect('shop.db')
    return conn


# Xodimning ishga kelish-ketishini qayd qilish
def log_employee_check_in_out(employee_id, check_type):
    conn = create_connection()
    cursor = conn.cursor()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if check_type == "in":
        cursor.execute('UPDATE employees SET check_in = ? WHERE id = ?', (current_time, employee_id))
        print(f"Xodim ID {employee_id} ishga keldi: {current_time}")
    elif check_type == "out":
        cursor.execute('UPDATE employees SET check_out = ? WHERE id = ?', (current_time, employee_id))
        print(f"Xodim ID {employee_id} ishdan ketdi: {current_time}")

    conn.commit()
    conn.close()


# Kamera ma'lumotlarini log qilish
def log_camera_data(employee_name, action):
    log_message = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {employee_name}: {action}\n"
    with open("camera_log.txt", "a") as log_file:
        log_file.write(log_message)
    print(f"Log qilindi: {log_message.strip()}")


# Xavfsizlik menyusi
def security_menu():
    while True:
        print("\n--- Xavfsizlik Panel ---")
        print("1. Xodimni ishga kelishini qayd qilish")
        print("2. Xodimni ishdan ketishini qayd qilish")
        print("3. Kamera ma'lumotlarini log qilish")
        print("4. Chiqish")
        choice = input("Tanlang: ")

        if choice == "1":
            employee_id = int(input("Xodim ID-sini kiriting: "))
            log_employee_check_in_out(employee_id, "in")
        elif choice == "2":
            employee_id = int(input("Xodim ID-sini kiriting: "))
            log_employee_check_in_out(employee_id, "out")
        elif choice == "3":
            employee_name = input("Xodim ismini kiriting: ")
            action = input("Amalni kiriting (masalan, 'Ish joyiga kirish'): ")
            log_camera_data(employee_name, action)
        elif choice == "4":
            print("Xavfsizlik panelidan chiqildi.")
            break
        else:
            print("Noto'g'ri tanlov!")


# Asosiy funksiya
if __name__ == "__main__":
    security_menu()