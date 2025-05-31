
import json
from dataclasses import asdict
from config import settings          # Import konfigurasi global
from services import math_service    # Import layanan matematika
from utils import helpers            # Import fungsi bantu umum
from models.data_model import User        # Import modul data_model

def main():
    # Cetak objek class User dari data_model untuk memastikan import berhasil
   # Buat objek User
    user1 = User(id=1, nama="Prima", email="prima@example.com")
    user2 = User(id=2, nama="Budi", email="budi@example.com")

    # Konversi ke dict dan serialisasi ke JSON
    json_user1 = json.dumps(asdict(user1), indent=4)
    json_user2 = json.dumps(asdict(user2), indent=4)

    # Tampilkan hasil JSON
    print("User 1 dalam format JSON:")
    print(json_user1)

    print("\nUser 2 dalam format JSON:")
    print(json_user2)

    # Ambil nama aplikasi dari konfigurasi
    x = settings.APP_NAME

    # Cetak salam dengan menyisipkan nama aplikasi
    print("Selamat datang di Aplikasi Modular Python! " + x)

    # Hitung penjumlahan 10 + 5 menggunakan fungsi tambah di math_service
    hasil = math_service.tambah(10, 5)
    print(f"Hasil penjumlahan 10 + 5 = {hasil}")

    # Format teks 'hasil selesai' menjadi huruf kapital semua menggunakan helper
    teks = helpers.format_tulisan("hasil selesai", upper=True)
    print(teks)

# Pastikan main() hanya dijalankan kalau file ini dijalankan langsung
if __name__ == "__main__":
    main()

