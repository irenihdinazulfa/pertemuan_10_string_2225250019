# Pertemuan 10 - String dan Pengolahan Teks

Nama: Iren Ihdina Zulfa
NIM: 2225250019
Kelas: Pendidikan Matematika

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan
python3 tugas/normalisasi_data_mahasiswa.py

## Algoritma
1. Menerima data teks input yang masih memiliki format tidak konsisten (misalnya spasi berlebih, variasi huruf kapital, dan karakter tidak diinginkan).
2. Menghapus spasi di awal dan akhir string menggunakan fungsi `strip()`.
3. Membersihkan spasi berlebih di antara kata menggunakan perulangan `while` dengan `replace("  ", " ")` atau `split()` dan `join()`.
4. Mengubah format kapitalisasi teks menggunakan `lower()`, `upper()`, `title()`, atau `capitalize()` sesuai kebutuhan data.
5. Menyimpan atau menampilkan data teks yang telah bersih dan terspesifikasi secara rapi.

## Test Case
| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| `"  FATHIYYAH mUTHMAINNAH  "` | `"Fathiyyah Muthmainnah"` | `"Fathiyyah Muthmainnah"` | PASSED |
| `"  belajar  python  untuk  pendidikan  "` | `"Belajar python untuk pendidikan"` | `"Belajar python untuk pendidikan"` | PASSED |

## Refleksi
- **Masalah Teks:** Teks input sering kali mengandung spasi ganda tak terlihat dan variasi huruf kapital/kecil yang tidak seragam (misal: `"mUTHMAINNAH"`).
- **Cara Memperbaiki:** Menggunakan metode `strip()` untuk menghilangkan spasi ujung, `while "  " in teks` dengan `replace()` untuk menyatukan spasi ganda, serta metode `title()` atau `capitalize()` untuk menyamakan format huruf kapital.