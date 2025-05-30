# 📁 BacaF - Struktur Folder Viewer (Tree Style)

Script Python ini menampilkan struktur direktori seperti pohon (tree), dan memberi warna pada file berdasarkan jenisnya:

* 🗾 File kode (PHP, HTML, CSS, Python, dll)
* 🔨 Dokumen (PDF, Word, Excel, dll)
* 🔪 Media (MP3, MP4, JPG, PNG, dll)
* 🔴 Executable (EXE, SH, BAT, dll)

---

## ✨ Fitur

* Menampilkan struktur folder seperti `tree`
* Penanda warna berdasarkan jenis file
* Bisa memilih untuk menampilkan folder **saja** atau **folder + file**

---

## ⚙️ Instalasi

### ✅ Prasyarat

Pastikan kamu sudah menginstall **Python 3** dan **pip**.

### 💻 Di Kali Linux

```bash
# 1. Clone repo
git clone https://github.com/afzan354/bacafolder.git
cd bacafolder

# 2. Install dependensi
pip install colorama

# 3. Jadikan executable
chmod +x bacaf.py

# 4. Tambahkan ke PATH (opsional agar bisa dipanggil dari mana saja)
sudo ln -s $(pwd)/bacaf.py /usr/local/bin/bacaf
```

> Sekarang kamu bisa menjalankan dengan:

```bash
bacaf /home/kamu/Documents -L
```

---

### 🩟 Di Windows

```powershell
# 1. Clone repo
git clone https://github.com/afzan354/bacafolder.git
cd bacafolder

# 2. Install dependensi
pip install colorama
```

#### Agar bisa dipanggil dari mana saja:

1. Rename file `bacaf.py` ke `bacaf` (hapus `.py`)
2. Buat file batch `bacaf.bat` seperti ini:

```bat
@echo off
python C:\path\to\bacaf.py %*
```

3. Simpan `bacaf.bat` di folder yang sudah masuk PATH (contoh: `C:\Windows\System32` atau buat custom PATH)
4. Sekarang kamu bisa panggil dari mana saja via Command Prompt:

```cmd
bacaf C:\Users\Kamu\Documents -L
```

---

## 🧪 Cara Penggunaan

```bash
# Menampilkan hanya folder:
bacaf /path/ke/direktori

# Menampilkan folder + file:
bacaf /path/ke/direktori -L
```

---

## 📌 Contoh Output

```bash
project/
├── src/
│   ├── main.py
│   └── utils.py
├── README.md
└── assets/
    └── logo.png
```

---

