import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random
from config import preprocess_text
from core_data import inputs, labels, responses

# Load user data tambahan
try:
    with open('user_data.json', 'r', encoding='utf-8') as f:
        user_data = json.load(f)
except FileNotFoundError:
    user_data = {}

# Training model core
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(inputs)
model = MultinomialNB()
model.fit(X, labels)

CONFIDENCE_THRESHOLD = 0.3

def search_user_data(text):
    # Cari exact match setelah preprocessing
    text_proc = preprocess_text(text)
    for question, answer_list in user_data.items():
        if preprocess_text(question) == text_proc:
            return random.choice(answer_list)
    return None

print("Chatbot siap! Ketik 'keluar' untuk berhenti.")

while True:
    user_input = input("Kamu: ")
    if user_input.lower() == 'keluar':
        print("Bot: Sampai jumpa!")
        break

    cleaned_input = preprocess_text(user_input)
    if not cleaned_input:
        print("Bot: Maaf, saya belum mengerti maksud kamu.")
        continue

    X_test = vectorizer.transform([cleaned_input])
    proba = model.predict_proba(X_test)[0]
    max_prob = max(proba)
    pred_index = proba.argmax()
    pred_label = model.classes_[pred_index]

    if max_prob >= CONFIDENCE_THRESHOLD:
        print("Bot:", random.choice(responses[pred_label]))
    else:
        user_resp = search_user_data(user_input)
        if user_resp:
            print("Bot:", user_resp)
        else:
            print("Bot: Maaf, saya belum mengerti maksud kamu.")

