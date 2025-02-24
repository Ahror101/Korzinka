GitHub-ga loyiha yuklash jarayonini quyidagicha amalga oshirishingiz mumkin. Loyihani GitHub-da saqlash uchun quyidagi qadamlarni bajaring:

---

### 1. **GitHub Repository Yaratish**
1. [GitHub](https://github.com/) saytiga kiring yoki ro‘yxatdan o‘ting.
2. O‘ng yuqori burchakda "+" tugmasini bosib, "New repository" ni tanlang.
3. Repository nomini kiriting (masalan, `karzinka_project`).
4. "Public" yoki "Private" tanlang (loyihangizni ochiq yoki yopiq saqlashni tanlashingiz mumkin).
5. "Initialize this repository with a README" ni belgilamaslik yaxshi bo‘ladi (biz keyinchalik o‘zimiz README.md faylini qo‘shamiz).
6. "Create repository" tugmasini bosing.

---

### 2. **Loyihani Git Bilan Lokal Sozlash**
Loyihangizni lokal kompyuteringizda Git bilan sozlash uchun quyidagi qadamlarni bajaring:

#### a) Git-ni O‘rnatish
Agar Git sizning kompyuteringizda o‘rnatilmagan bo‘lsa, uni o‘rnating:
- Windows uchun: [Git for Windows](https://git-scm.com/download/win)
- macOS uchun: `brew install git`
- Linux uchun: `sudo apt install git`

#### b) Loyihaning Iloji Boricha To‘liq Bo‘lishini Ta’minlang
Loyihangizning hamma fayllari to‘g‘ri joylashganligiga ishonch hosil qiling:
```
📂 karzinka_project/
├── 📄 main.py
├── 📄 database.py
├── 📄 shop.py
├── 📄 user.py
├── 📄 admin.py
└── 📂 data/
```

#### c) Git-ni Loyihaga Kiritish
Terminal yoki Git Bash orqali quyidagi buyruqlarni bajaring:

```bash
# Loyihaning papkasiga o'ting
cd karzinka_project

# Git repozitoriyasini boshlash
git init

# Barcha fayllarni kuzatishni yoqish
git add .

# Birinchi commit-ni yaratish
git commit -m "Birinchi versiya: Loyiha tuzilishi va asosiy funksiyalar"
```

---

### 3. **GitHub Repository-ga Yuklash**
GitHub-dagi yangi repository URL-manzilini olasiz. Masalan:
```
https://github.com/foydalanuvchi_ismi/karzinka_project.git
```

#### Terminalda quyidagi buyruqlarni bajaring:
```bash
# Remote repository-ni bog'lash
git remote add origin https://github.com/foydalanuvchi_ismi/karzinka_project.git

# Kodlarni GitHub-ga yuklash
git push -u origin master
```

Agar sizda `main` branch bo‘lsa, `master` o‘rniga `main` yozing:
```bash
git push -u origin main
```

---

### 4. **README.md Faylini Qo‘shish**
GitHub-dagi loyihangiz haqida ma’lumot berish uchun `README.md` faylini yarating. Bu Markdown formatida yoziladi.

#### Misol (`README.md`):
```markdown
# Karzinka Project

Oddiy buyum sotish tizimi. Foydalanuvchilar mahsulotlarni ko‘rishi, savatchaga qo‘shishi va buyurtma berishi mumkin. Admin mahsulotlarni qo‘shishi, o‘chirishi va tahrirlashi mumkin.

## Loyiha Tuzilishi
- **main.py**: Asosiy dastur.
- **database.py**: Ma'lumotlar bazasi bilan ishlash.
- **shop.py**: Mahsulotlar bilan ishlash funksiyalari.
- **user.py**: Foydalanuvchi savatchasi va buyurtmalar.
- **admin.py**: Admin paneli.

## Texnologiyalar
- Python
- SQLite
- CLI (Konsol interfeysi)

## O‘rnatish va Ishga Tushirish
1. Loyihani kompyuteringizga yuklab oling:
   ```bash
   git clone https://github.com/foydalanuvchi_ismi/karzinka_project.git
   ```
2. Kerakli kutubxonalarni o‘rnating (agar mavjud bo‘lsa):
   ```bash
   pip install -r requirements.txt
   ```
3. Loyihani ishga tushiring:
   ```bash
   python main.py
   ```

## Muallif
- [Sizning Ismingiz](https://github.com/foydalanuvchi_ismi)
```

#### README.md Faylini Yuklash
Terminalda quyidagi buyruqlarni bajaring:
```bash
# README.md faylini kuzatishga qo'shish
git add README.md

# Commit yaratish
git commit -m "README.md fayli qo'shildi"

# GitHub-ga yuklash
git push
```

---

### 5. **GitHub Repository-ni Tekshirish**
GitHub sahifangizga o‘ting va loyihangizni tekshiring. Endi sizning loyiha GitHub-da saqlangan va boshqa odamlar uni ko‘ra oladilar.

---

### 6. **Keyingi Bosqichlar**
Agar loyihangizni yanada rivojlantirmoqchi bo‘lsangiz:
1. **Foydalanuvchi ro‘yxatdan o‘tish va login qilish** funksiyalarini qo‘shing.
2. **Savatcha va buyurtmalar** funksiyalarini amalga oshiring.
3. **Unit testlar** yozing.
4. **Dockerfile** yoki `.env` fayllari qo‘shib, loyihani professionalroq qiling.

Agar yordam kerak bo‘lsa, yana murojaat qiling! 😊
