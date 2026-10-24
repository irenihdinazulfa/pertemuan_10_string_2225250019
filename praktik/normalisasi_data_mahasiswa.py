# Fungsi 1: Normalisasi nama (menghapus spasi berlebih dan mengubah ke Title Case)
def normalisasi_nama(nama):
    nama_bersih = nama.strip()
    # Menggabungkan kembali kata jika terdapat spasi ganda di tengah nama
    kata_list = nama_bersih.split()
    nama_terformat = " ".join(kata_list).title()
    return nama_terformat

# Fungsi 2: Normalisasi kode kelas (menghapus spasi, mengganti spasi antar kata dengan '-', dan huruf besar)
def normalisasi_kode_kelas(kode):
    kode_bersih = kode.strip().upper()
    kata_list = kode_bersih.split()
    return "-".join(kata_list)

# Fungsi 3: Mengambil inisial dari nama yang sudah dinormalisasi
def ambil_inisial(nama):
    kata_list = nama.split()
    inisial = "".join([kata[0].upper() for kata in kata_list])
    return inisial

# Input data dari pengguna
nama_input = input("Nama: ")
kode_input = input("Kode kelas: ")

# Proses pengolahan teks menggunakan fungsi
nama_hasil = normalisasi_nama(nama_input)
kode_hasil = normalisasi_kode_kelas(kode_input)
jumlah_kata = len(nama_hasil.split())
inisial_hasil = ambil_inisial(nama_hasil)

# Output tampilan hasil normalisasi secara rapi
print()
print(f"Nama bersih : {nama_hasil}")
print(f"Kode kelas  : {kode_hasil}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial_hasil}")