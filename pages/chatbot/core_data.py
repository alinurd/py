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

responses = {
    "hai": ["Hai! Ada yang bisa saya bantu?", "Halo! Apa kabar?"],
    "nama": ["Saya chatbot sederhana.", "Namaku ChatBot ML."],
    "terima kasih": ["Sama-sama!", "Senang bisa membantu!"],
    "selamat tinggal": ["Sampai jumpa!", "Terima kasih sudah ngobrol!"]
}
