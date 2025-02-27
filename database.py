import json
import os

# JSON fayl nomi
JSON_FILE = "karzinka.json"

# Boshlang'ich ma'lumotlar strukturasi
DEFAULT_DATA = {
    "users": [],
    "products": [],
    "orders": [],
    "employees": [],
    "cameras": []
}


def load_data():
    """
    JSON faylidan ma'lumotlarni o'qish.
    Agar fayl mavjud bo'lmasa, yangi fayl yaratiladi.
    """
    try:
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            # Agar fayl mavjud bo'lmasa, yangi fayl yaratish
            save_data(DEFAULT_DATA)
            return DEFAULT_DATA
    except json.JSONDecodeError:
        print("Xato: JSON fayli buzilgan. Yangi fayl yaratilmoqda.")
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
        return DEFAULT_DATA


def save_data(data):
    """
    Ma'lumotlarni JSON fayliga saqlash
    """
    try:
        with open(JSON_FILE, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Ma'lumotlarni saqlashda xato: {e}")
        return False


def add_item(section, data):
    """
    Ma'lum bo'limga yangi element qo'shish

    Args:
        section (str): Bo'lim nomi ('users', 'products', etc.)
        data (dict): Qo'shiladigan ma'lumot

    Returns:
        int: Yangi qo'shilgan elementning ID raqami
    """
    try:
        all_data = load_data()

        # Agar bo'lim mavjud bo'lmasa
        if section not in all_data:
            all_data[section] = []

        # Yangi ID yaratish
        if all_data[section]:
            new_id = max(item["id"] for item in all_data[section]) + 1
        else:
            new_id = 1

        # ID ni ma'lumotga qo'shish
        data["id"] = new_id

        # Ma'lumotni bo'limga qo'shish
        all_data[section].append(data)

        # O'zgarishlarni saqlash
        save_data(all_data)
        return new_id
    except Exception as e:
        print(f"Element qo'shishda xato: {e}")
        return None


def get_item(section, item_id):
    """
    ID bo'yicha elementni olish

    Args:
        section (str): Bo'lim nomi
        item_id (int): Element ID si

    Returns:
        dict: Topilgan element yoki None
    """
    try:
        all_data = load_data()

        if section not in all_data:
            return None

        for item in all_data[section]:
            if item["id"] == item_id:
                return item

        return None
    except Exception as e:
        print(f"Elementni olishda xato: {e}")
        return None


def update_item(section, item_id, new_data):
    """
    Elementni yangilash

    Args:
        section (str): Bo'lim nomi
        item_id (int): Element ID si
        new_data (dict): Yangi ma'lumotlar

    Returns:
        bool: Muvaffaqiyatli yangilangan bo'lsa True
    """
    try:
        all_data = load_data()

        if section not in all_data:
            return False

        for i, item in enumerate(all_data[section]):
            if item["id"] == item_id:
                # ID ni o'zgartirmaslik uchun
                new_data["id"] = item_id
                all_data[section][i] = new_data
                save_data(all_data)
                return True

        return False
    except Exception as e:
        print(f"Elementni yangilashda xato: {e}")
        return False


def delete_item(section, item_id):
    """
    Elementni o'chirish

    Args:
        section (str): Bo'lim nomi
        item_id (int): Element ID si

    Returns:
        bool: Muvaffaqiyatli o'chirilgan bo'lsa True
    """
    try:
        all_data = load_data()

        if section not in all_data:
            return False

        for i, item in enumerate(all_data[section]):
            if item["id"] == item_id:
                del all_data[section][i]
                save_data(all_data)
                return True

        return False
    except Exception as e:
        print(f"Elementni o'chirishda xato: {e}")
        return False


def get_all_items(section):
    """
    Bo'limdagi barcha elementlarni olish

    Args:
        section (str): Bo'lim nomi

    Returns:
        list: Elementlar ro'yxati
    """
    try:
        all_data = load_data()

        if section not in all_data:
            return []

        return all_data[section]
    except Exception as e:
        print(f"Elementlarni olishda xato: {e}")
        return []


def search_items(section, key, value):
    """
    Ma'lum qiymat bo'yicha elementlarni qidirish

    Args:
        section (str): Bo'lim nomi
        key (str): Qidirilayotgan kalit
        value: Qidirilayotgan qiymat

    Returns:
        list: Topilgan elementlar ro'yxati
    """
    try:
        all_data = load_data()

        if section not in all_data:
            return []

        return [item for item in all_data[section] if key in item and item[key] == value]
    except Exception as e:
        print(f"Qidirishda xato: {e}")
        return []