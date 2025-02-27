from database import get_item, update_item, get_all_items, add_item
import datetime


def record_employee_check_in(employee_id):
    """
    Xodimning ishga kelishini qayd qilish

    Args:
        employee_id (int): Xodim ID si

    Returns:
        bool: Muvaffaqiyatli qayd qilingan bo'lsa True
    """
    employee = get_item("employees", employee_id)
    if not employee:
        print(f"ID: {employee_id} bo'lgan xodim topilmadi")
        return False

    # Xodimning ishga kelish vaqtini yangilash
    current_time = datetime.datetime.now().strftime("%H:%M")
    employee["check_in"] = current_time

    return update_item("employees", employee_id, employee)


def record_employee_check_out(employee_id):
    """
    Xodimning ishdan ketishini qayd qilish

    Args:
        employee_id (int): Xodim ID si

    Returns:
        bool: Muvaffaqiyatli qayd qilingan bo'lsa True
    """
    employee = get_item("employees", employee_id)
    if not employee:
        print(f"ID: {employee_id} bo'lgan xodim topilmadi")
        return False

    # Xodimning ishdan ketish vaqtini yangilash
    current_time = datetime.datetime.now().strftime("%H:%M")
    employee["check_out"] = current_time

    return update_item("employees", employee_id, employee)


def record_camera_activity(camera_id, activity_description):
    """
    Kamera faoliyatini qayd qilish

    Args:
        camera_id (int): Kamera ID si
        activity_description (str): Faoliyat tavsifi

    Returns:
        bool: Muvaffaqiyatli qayd qilingan bo'lsa True
    """
    camera = get_item("cameras", camera_id)
    if not camera:
        print(f"ID: {camera_id} bo'lgan kamera topilmadi")
        return False

    # Kameraning so'nggi yozuv vaqtini yangilash
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    camera["last_record"] = current_time

    # Faoliyat tavsifini qo'shish (ixtiyoriy)
    if "activities" not in camera:
        camera["activities"] = []

    camera["activities"].append({
        "time": current_time,
        "description": activity_description
    })

    return update_item("cameras", camera_id, camera)


def view_employee_attendance():
    """
    Xodimlarning ishga kelish-ketish vaqtlarini ko'rish

    Returns:
        list: Xodimlar ro'yxati
    """
    return get_all_items("employees")


def view_camera_activities():
    """
    Kameralar faoliyatini ko'rish

    Returns:
        list: Kameralar ro'yxati
    """
    return get_all_items("cameras")


def security_menu():
    """
    Xavfsizlik menyusi
    """
    while True:
        print("\n===== XAVFSIZLIK =====")
        print("1. Xodimning ishga kelishini qayd qilish")
        print("2. Xodimning ishdan ketishini qayd qilish")
        print("3. Kamera faoliyatini qayd qilish")
        print("4. Xodimlarning ishga kelish-ketish vaqtlarini ko'rish")
        print("5. Kameralar faoliyatini ko'rish")
        print("0. Chiqish")

        choice = input("Tanlang: ")

        if choice == "1":
            employees = view_employee_attendance()
            if employees:
                print("\nXODIMLAR:")
                for employee in employees:
                    print(f"ID: {employee['id']}, Ismi: {employee['name']}, Lavozimi: {employee['role']}")

                employee_id = int(input("Xodim ID si: "))
                if record_employee_check_in(employee_id):
                    print("Xodimning ishga kelishi qayd qilindi")
                else:
                    print("Xodimning ishga kelishini qayd qilishda xatolik")
            else:
                print("Xodimlar yo'q")

        elif choice == "2":
            employees = view_employee_attendance()
            if employees:
                print("\nXODIMLAR:")
                for employee in employees:
                    print(f"ID: {employee['id']}, Ismi: {employee['name']}, Lavozimi: {employee['role']}")

                employee_id = int(input("Xodim ID si: "))
                if record_employee_check_out(employee_id):
                    print("Xodimning ishdan ketishi qayd qilindi")
                else:
                    print("Xodimning ishdan ketishini qayd qilishda xatolik")
            else:
                print("Xodimlar yo'q")

        elif choice == "3":
            cameras = view_camera_activities()
            if cameras:
                print("\nKAMERALAR:")
                for camera in cameras:
                    print(f"ID: {camera['id']}, Joylashuvi: {camera['location']}")

                camera_id = int(input("Kamera ID si: "))
                activity = input("Faoliyat tavsifi: ")

                if record_camera_activity(camera_id, activity):
                    print("Kamera faoliyati qayd qilindi")
                else:
                    print("Kamera faoliyatini qayd qilishda xatolik")
            else:
                print("Kameralar yo'q")

        elif choice == "4":
            employees = view_employee_attendance()
            if employees:
                print("\nXODIMLARNING ISHGA KELISH-KETISH VAQTLARI:")
                for employee in employees:
                    print(f"ID: {employee['id']}, Ismi: {employee['name']}, " +
                          f"Lavozimi: {employee['role']}, " +
                          f"Kelish: {employee['check_in']}, Ketish: {employee['check_out']}")
            else:
                print("Xodimlar yo'q")

        elif choice == "5":
            cameras = view_camera_activities()
            if cameras:
                print("\nKAMERALAR FAOLIYATI:")
                for camera in cameras:
                    print(f"ID: {camera['id']}, Joylashuvi: {camera['location']}, " +
                          f"So'nggi yozuv: {camera['last_record']}")

                    if "activities" in camera and camera["activities"]:
                        print("Faoliyatlar:")
                        for activity in camera["activities"]:
                            print(f"  Vaqt: {activity['time']}, Tavsif: {activity['description']}")
                    print()
            else:
                print("Kameralar yo'q")

        elif choice == "0":
            break
        else:
            print("Noto'g'ri tanlov!")