import json
from dataclasses import dataclass, asdict

# Definisikan data model User dengan dataclass
@dataclass
class User:
    id: int
    nama: str
    email: str

def main():
    # Buat contoh data user
    user1 = User(id=1, nama="Prima", email="prima@example.com")
    user2 = User(id=2, nama="Budi", email="budi@example.com")

    # Konversi objek user ke dict, lalu ke JSON
    json_user1 = json.dumps(asdict(user1), indent=4)
    json_user2 = json.dumps(asdict(user2), indent=4)

    # Tampilkan hasil JSON
    print("User 1 dalam format JSON:")
    print(json_user1)

    print("\nUser 2 dalam format JSON:")
    print(json_user2)

if __name__ == "__main__":
    main()
