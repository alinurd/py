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
