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

labels += [
  "favorit",
  "favorit",
  "favorit",
  "favorit"
]


responses = {
    "hai": ["Hai! Ada yang bisa saya bantu?", "Halo! Apa kabar?"],
    "nama": ["Saya chatbot sederhana.", "Namaku ChatBot ML."],
    "terima kasih": ["Sama-sama!", "Senang bisa membantu!"],
    "selamat tinggal": ["Sampai jumpa!", "Terima kasih sudah ngobrol!"]
}


responses["favorit"] = [
  "Saya tidak makan eskrim, tapi saya suka ngobrol tentang itu!",
  "Es krim memang enak ya!",
  "Saya suka semua rasa eskrim."
]
