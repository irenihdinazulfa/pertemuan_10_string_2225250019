# Input: String nama yang memiliki spasi berlebih di awal/akhir dan kapitalisasi tak teratur
nama = "  FATHIYYAH mUTHMAINNAH  "

# Proses:
# 1. Menghapus spasi di awal dan akhir dengan strip()
# 2. Mengubah huruf awal setiap kata menjadi kapital dengan title()
# 3. Mengubah seluruh huruf menjadi kapital dengan upper()

# Output: Menampilkan hasil pembersihan dan penyesuaian format nama
print(nama.strip())
print(nama.strip().title())
print(nama.strip().upper())