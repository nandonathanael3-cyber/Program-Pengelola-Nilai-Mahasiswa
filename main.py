# main.py
from operasi import tambah_nilai, tampilkan_nilai, rata_rata

def menu():
    print("\n=== PROGRAM NILAI MAHASISWA ===")
    print("1. Tambah nilai mahasiswa")
    print("2. Tampilkan semua nilai")
    print("3. Hitung rata-rata nilai")
    print("0. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama mahasiswa: ")
        nilai = float(input("Nilai: "))
        tambah_nilai(nama, nilai)   
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        tampilkan_nilai()

    elif pilihan == "3":
        print(f"Rata-rata nilai: {rata_rata():.2f}")

    elif pilihan == "0":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid!")
