# operasi.py
from data import nilai_mahasiswa

def tambah_nilai(nama, nilai):
    nilai_mahasiswa.append({
        "nama": nama,
        "nilai": nilai
    })

def tampilkan_nilai():
    if not nilai_mahasiswa:
        print("Belum ada data nilai.")
        return
    for mhs in nilai_mahasiswa:
        print(f"{mhs['nama']} : {mhs['nilai']}")

def rata_rata():
    if not nilai_mahasiswa:
        return 0
    total = sum(m['nilai'] for m in nilai_mahasiswa)
    return total / len(nilai_mahasiswa)