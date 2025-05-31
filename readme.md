✨ Menambahkan preprocessing (normalisasi teks)

💡 Pakai TfidfVectorizer

🧩 Tambah kategori + data latihan baru

🤖 Ubah chatbot ke versi NLP modern (pakai Hugging Face)


# Chatbot Python Terstruktur dengan Machine Learning dan Data User

Chatbot sederhana berbasis Python yang mengombinasikan model Machine Learning Naive Bayes dengan data tanya-jawab tambahan dari pengguna secara dinamis. Struktur kode dipisah menjadi beberapa modul agar mudah dikembangkan, dimodifikasi, dan dipelihara.

---

## Fitur

- Preprocessing teks input (lowercase, hapus tanda baca, dan trim spasi).
- Model Machine Learning Naive Bayes untuk mengklasifikasikan pertanyaan inti.
- Penyimpanan data tanya-jawab tambahan dari user ke file JSON (`user_data.json`).
- Pencocokan fuzzy (mirip) untuk mencari jawaban dari data tambahan user.
- Penambahan data tanya-jawab dari user melalui perintah chat.
- Struktur kode modular: `config.py`, `data_core.py`, `user_data_manager.py`, `ml_model.py`, dan `main.py`.

---

## Struktur Direktori & File

- `config.py`  
  Berisi fungsi preprocessing dan data respons chatbot inti.

- `data_core.py`  
  Data pelatihan awal chatbot berupa daftar pertanyaan dan label.

- `user_data_manager.py`  
  Kelas untuk mengelola data tanya-jawab tambahan dari pengguna (baca/tulis file JSON).

- `ml_model.py`  
  Kelas model Naive Bayes untuk training dan prediksi respons.

- `main.py`  
  Script utama yang menjalankan chatbot, mengatur alur interaksi pengguna.

- `user_data.json`  
  File JSON untuk menyimpan data tambahan dari user (otomatis dibuat saat pertama kali dijalankan jika belum ada).

---

## Cara Menggunakan

1. Pastikan Python 3.7+ sudah terinstall.
2. Install dependensi yang diperlukan:

```bash
pip install scikit-learn
