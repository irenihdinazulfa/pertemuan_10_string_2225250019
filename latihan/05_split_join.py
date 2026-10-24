# Input: String kalimat sederhana
kalimat = "data teks perlu dibersihkan"

# Proses:
# 1. Memecah kalimat menjadi list kata menggunakan split()
# 2. Menggabungkan kembali list kata menjadi string baru dengan tanda hubung (-) menggunakan join()
kata = kalimat.split()

# Output: Menampilkan list hasil split dan string hasil join
print(kata)
print("-".join(kata))