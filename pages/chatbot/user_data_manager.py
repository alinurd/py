# user_data_manager.py
import json
import random
import difflib
from config import preprocess_text

class UserDataManager:
    def __init__(self, filepath='user_data.json'):
        self.filepath = filepath
        self.user_data = self.load_user_data()
        # Buat versi preprocessed dari user_data untuk pencarian yang konsisten
        self.user_data_proc = {preprocess_text(q): a for q, a in self.user_data.items()}

    def load_user_data(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_user_data(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.user_data, f, indent=2, ensure_ascii=False)

    def tambah_data_user(self, question, answers):
        question_proc = preprocess_text(question)
        if question_proc in self.user_data_proc:
            print("Pertanyaan sudah ada di user data.")
            return
        self.user_data[question] = answers
        self.user_data_proc[question_proc] = answers
        self.save_user_data()
        print("Data user berhasil ditambahkan.")

    def search_user_data(self, text_proc, threshold=0.7):
        """
        Cari jawaban dari data user dengan menggunakan
        pencocokan string mendekati (difflib.get_close_matches)
        berdasarkan text yang sudah dipreproses.
        """
        questions = list(self.user_data_proc.keys())
        matches = difflib.get_close_matches(text_proc, questions, n=1, cutoff=threshold)
        if matches:
            return random.choice(self.user_data_proc[matches[0]])
        return None
