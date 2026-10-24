# Input: String yang berisi spasi berlebih di awal, akhir, dan antar kata
teks = "  belajar  python  untuk  pendidikan  "

# Proses:
# 1. Menghapus spasi di awal dan akhir string dengan strip()
# 2. Mengganti ganda spasi ("  ") menjadi spasi tunggal (" ") secara berulang hingga spasi ganda habis
# 3. Mengubah huruf pertama dari string menjadi huruf kapital dengan capitalize()
teks = teks.strip()
while "  " in teks:
    teks = teks.replace("  ", " ")

# Output: Menampilkan teks bersih dengan huruf kapital di awal kalimat
print(teks.capitalize())