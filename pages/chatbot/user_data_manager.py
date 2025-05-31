import os
import json
import random
import difflib
from config import preprocess_text


class UserDataManager:
    def __init__(self, filepath='/pages/chatbot/user_training/user_data.json'):
        self.filepath = filepath
        self.ensure_folder_exists()
        self.user_data = self.load_user_data()
        # Preprocess seluruh pertanyaan untuk pencarian konsisten
        self.user_data_proc = {
            preprocess_text(q): a for q, a in self.user_data.items()
        }

    def ensure_folder_exists(self):
        """Pastikan folder tempat penyimpanan file JSON tersedia."""
        folder = os.path.dirname(self.filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            print(f"[INFO] Folder '{folder}' dibuat.")

    def load_user_data(self):
        """Muat data user dari file JSON. Jika tidak ada, kembalikan dictionary kosong."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"[INFO] Data user berhasil dimuat dari {self.filepath}")
                return data
        except FileNotFoundError:
            print(f"[WARNING] File {self.filepath} tidak ditemukan. Membuat data kosong.")
            return {}
        except json.JSONDecodeError as e:
            print(f"[ERROR] Gagal membaca JSON: {e}")
            return {}

    def save_user_data(self):
        """Simpan data user ke file JSON."""
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.user_data, f, indent=2, ensure_ascii=False)
            print(f"[INFO] Data user berhasil disimpan ke {self.filepath}")
        except Exception as e:
            print(f"[ERROR] Gagal menyimpan user data: {e}")

    def tambah_data_user(self, question, answers):
        """Tambahkan pertanyaan & jawaban baru ke data user."""
        question_proc = preprocess_text(question)

        if question_proc in self.user_data_proc:
            print("[INFO] Pertanyaan sudah ada dalam data.")
            return

        # Tambahkan pertanyaan dan jawabannya
        self.user_data[question] = answers
        self.user_data_proc[question_proc] = answers
        self.save_user_data()
        print(f"[SUCCESS] Data berhasil ditambahkan: '{question}' -> {answers}")

    def search_user_data(self, text_proc, threshold=0.7):
        """
        Cari jawaban dari data user berdasarkan pencocokan pertanyaan.
        Menggunakan difflib.get_close_matches dengan ambang kemiripan tertentu.
        """
        questions = list(self.user_data_proc.keys())
        matches = difflib.get_close_matches(text_proc, questions, n=1, cutoff=threshold)
        if matches:
            print(f"[DEBUG] Pertanyaan cocok ditemukan: '{matches[0]}'")
            return random.choice(self.user_data_proc[matches[0]])
        print("[DEBUG] Tidak ada pertanyaan cocok ditemukan.")
        return None
