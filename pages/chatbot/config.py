# config.py
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('indonesian'))  # kalau mau hapus stopwords

def threshold ():
    return 0.3
def preprocess_text(text):
    """
    Preprocessing sederhana:
    - lowercase
    - hapus karakter selain huruf dan spasi
    - strip spasi
    - (opsional) hapus stopwords
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = text.strip()
    
    # Jika mau hapus stopwords, aktifkan ini:
    # words = text.split()
    # filtered = [w for w in words if w not in stop_words]
    # text = ' '.join(filtered)
    
    return text



data_training.py

from config import preprocess_text

inputs = [
    preprocess_text("halo"),
    preprocess_text("hai"),
    preprocess_text("apa namamu"),
    preprocess_text("siapa kamu"),
    preprocess_text("terima kasih banyak"),
    preprocess_text("makasih"),
    preprocess_text("selamat tinggal"),
    preprocess_text("dadah")
]

labels = [
    "hai",
    "hai",
    "nama",
    "nama",
    "terima kasih",
    "terima kasih",
    "selamat tinggal",
    "selamat tinggal"
]

inputs += [
  preprocess_text("aku suka eskrim"),
  preprocess_text("kamu suka eskrim?"),
  preprocess_text("makanan favoritmu apa"),
  preprocess_text("apa kamu suka eskrim")
]
 

responses = {
    "hai": ["Hai! Ada yang bisa saya bantu?", "Halo! Apa kabar?"],
    "nama": ["Saya chatbot sederhana.", "Namaku ChatBot ML."],
    "terima kasih": ["Sama-sama!", "Senang bisa membantu!"],
    "selamat tinggal": ["Sampai jumpa!", "Terima kasih sudah ngobrol!"]
}


user_data_manager.py
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


# ml_model.py
# ml_model.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from data_core import inputs, labels, responses
from config import preprocess_text

class MLModel:
    def __init__(self):
        # Preprocessing inputs sebelum training
        inputs_proc = [preprocess_text(text) for text in inputs]

        # Vectorizer dan model training
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(inputs_proc)

        self.model = MultinomialNB()
        self.model.fit(X, labels)

    def predict(self, text):
        """
        Menerima text input, memproses, dan mengembalikan
        prediksi label dan probabilitas maksimal.
        """
        text_proc = preprocess_text(text)
        X_test = self.vectorizer.transform([text_proc])
        proba = self.model.predict_proba(X_test)[0]
        max_prob = max(proba)
        pred_index = proba.argmax()
        pred_label = self.model.classes_[pred_index]
        return pred_label, max_prob


# main.py
import random
from config import preprocess_text, threshold
from user_data_manager import UserDataManager
from ml_model import MLModel

CONFIDENCE_THRESHOLD =threshold  # Threshold confidence ML untuk menjawab

def main():
    user_manager = UserDataManager()
    ml_model = MLModel()

    print("Chatbot siap! Ketik 'keluar' untuk berhenti.")

    while True:
        user_input = input("Kamu: ")
        if user_input.lower() == 'keluar':
            print("Bot: Sampai jumpa!")
            break

        # Perintah tambah data baru dari user
        if user_input.lower().startswith("tambah:"):
            try:
                data = user_input[7:].split("|")
                question = data[0].strip()
                answers = [a.strip() for a in data[1].split(",")]
                user_manager.tambah_data_user(question, answers)
            except Exception:
                print("Format tambah salah. Contoh: tambah:apa kabar?|Baik,Terima kasih")
            continue

        cleaned_input = preprocess_text(user_input)
        if not cleaned_input:
            print("Bot: Maaf, saya belum mengerti maksud kamu.")
            continue

        # Cek data user dulu (prioritas)
        user_resp = user_manager.search_user_data(cleaned_input)
        if user_resp:
            print("Bot:", user_resp)
            continue

        # Jika tidak ada di data user, gunakan ML model
        pred_label, max_prob = ml_model.predict(cleaned_input)
        if max_prob >= CONFIDENCE_THRESHOLD:
            print("Bot:", random.choice(preprocess_text[pred_label]))
        else:
            print("Bot: Maaf, saya belum mengerti maksud kamu.")

if __name__ == "__main__":
    main()

