# math_service.py
# Menyimpan fungsi-fungsi matematika dasar dan utility

def tambah(a: int, b: int) -> int:
    """
    Mengembalikan hasil penjumlahan dua angka.

    Args:
        a (int): angka pertama
        b (int): angka kedua

    Returns:
        int: hasil penjumlahan a + b
    """
    return a + b


def kurang(a: int, b: int) -> int:
    """
    Mengembalikan hasil pengurangan dua angka.

    Args:
        a (int): angka pertama
        b (int): angka kedua

    Returns:
        int: hasil pengurangan a - b
    """
    return a - b


def kali(a: int, b: int) -> int:
    """
    Mengembalikan hasil perkalian dua angka.

    Args:
        a (int): angka pertama
        b (int): angka kedua

    Returns:
        int: hasil perkalian a * b
    """
    return a * b


def bagi(a: float, b: float) -> float:
    """
    Mengembalikan hasil pembagian dua angka.
    Jika pembagi (b) adalah nol, mengembalikan None dan mencetak peringatan.

    Args:
        a (float): angka pembilang
        b (float): angka penyebut

    Returns:
        float | None: hasil pembagian a / b, atau None jika pembagi nol
    """
    if b == 0:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
        return None
    return a / b


def pangkat(a: int, b: int) -> int:
    """
    Mengembalikan hasil perpangkatan a^b.

    Args:
        a (int): basis
        b (int): eksponen

    Returns:
        int: hasil a pangkat b
    """
    return a ** b


def modulus(a: int, b: int) -> int:
    """
    Mengembalikan sisa hasil bagi a modulo b.

    Args:
        a (int): angka pertama
        b (int): angka kedua

    Returns:
        int: sisa hasil bagi a % b
    """
    return a % b
