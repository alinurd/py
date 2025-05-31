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




