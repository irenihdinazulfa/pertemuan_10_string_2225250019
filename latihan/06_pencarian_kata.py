# Input: String kalimat dan kata yang ingin dicari
teks = "Python untuk data. Python untuk pendidikan."
teks = teks.lower()  # Normalisasi ke huruf kecil agar pencarian bersifat case-insensitive
kata = "python"

# Proses:
# 1. Memeriksa keberadaan kata dengan operator 'in'
# 2. Menghitung frekuensi kemunculan kata dengan count()
# 3. Mencari posisi indeks kemunculan pertama dengan find()

# Output: Menampilkan status keberadaan (True/False), jumlah kemunculan, dan indeks posisi pertama
print(kata in teks)
print(teks.count(kata))
print(teks.find(kata))