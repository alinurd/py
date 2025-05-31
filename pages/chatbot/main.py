import random
from config import preprocess_text, threshold
from user_data_manager import UserDataManager
from ml_model import MLModel
from data_core import responses

CONFIDENCE_THRESHOLD = threshold()  # panggil fungsi threshold

def main():
    user_manager = UserDataManager()
    ml_model = MLModel()

    print("Chatbot siap! Ketik 'keluar' untuk berhenti.")

    while True:
        user_input = input("Kamu: ")
        if user_input.lower() == 'keluar':
            print("Bot: Sampai jumpa!")
            break

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

        user_resp = user_manager.search_user_data(cleaned_input)
        if user_resp:
            print("Bot:", user_resp)
            continue

        pred_label, max_prob = ml_model.predict(cleaned_input)
        if max_prob >= CONFIDENCE_THRESHOLD:
            print("Bot:", random.choice(responses[pred_label]))
        else:
            print("Bot: Maaf, saya belum mengerti maksud kamu.")

if __name__ == "__main__":
    main()

