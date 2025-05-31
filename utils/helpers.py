# helpers.py
# Fungsi bantu umum untuk manipulasi string dan validasi sederhana

def format_tulisan(teks: str, upper: bool = False) -> str:
    """
    Mengubah teks menjadi huruf besar jika upper=True,
    jika tidak, huruf pertama kapital.

    Args:
        teks (str): teks input
        upper (bool): jika True, ubah semua huruf jadi kapital

    Returns:
        str: teks yang sudah diformat
    """
    if upper:
        return teks.upper()   # Ubah semua huruf menjadi kapital
    return teks.capitalize()  # Kapitalisasi huruf pertama


def trim(teks: str) -> str:
    """
    Menghapus spasi kosong di awal dan akhir string.

    Args:
        teks (str): teks input

    Returns:
        str: teks tanpa spasi di awal dan akhir
    """
    return teks.strip()


def is_email_valid(email: str) -> bool:
    """
    Cek apakah format email valid secara sederhana.

    Args:
        email (str): alamat email

    Returns:
        bool: True jika format email valid, False jika tidak
    """
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def safe_int(teks: str, default: int = 0) -> int:
    """
    Mengubah string menjadi integer dengan aman.
    Jika gagal, mengembalikan nilai default.

    Args:
        teks (str): string input
        default (int): nilai default jika konversi gagal

    Returns:
        int: hasil konversi integer atau default
    """
    try:
        return int(teks)
    except (ValueError, TypeError):
        return default


def capitalize_each_word(teks: str) -> str:
    """
    Mengubah huruf pertama setiap kata menjadi kapital.

    Args:
        teks (str): teks input

    Returns:
        str: teks dengan setiap kata diawali huruf kapital
    """
    return teks.title()
