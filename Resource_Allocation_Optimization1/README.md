# Resource Allocation Optimization untuk Efisiensi Energi pada Sistem Komputasi Modern

## Deskripsi Proyek
Proyek ini merupakan simulasi **resource allocation** pada sistem komputasi modern
yang bertujuan untuk mengoptimalkan **penggunaan energi** dengan memilih resource
yang tepat antara **CPU dan GPU** dalam mengeksekusi sejumlah task.

Program ini dirancang sebagai bagian dari **Tugas Besar Algoritma Scheduling dan
Resource Allocation**, dengan fokus pada:
- Efisiensi energi
- Analisis kompleksitas algoritma
- Visualisasi hasil menggunakan GUI

---

## Tujuan
1. Mensimulasikan proses alokasi resource CPU dan GPU
2. Menghitung kebutuhan energi untuk setiap task
3. Membandingkan total konsumsi energi CPU vs GPU
4. Menganalisis performa algoritma dari sisi waktu dan memori
5. Menyajikan hasil dalam bentuk GUI dan grafik

---

## Konsep Algoritma
Algoritma yang digunakan adalah **energy-aware resource allocation**, yaitu:
- Setiap task dihitung kebutuhan energinya pada CPU dan GPU
- Sistem memilih resource berdasarkan kebijakan alokasi (hybrid scheduling)
- Total energi dari masing-masing resource dibandingkan

Kompleksitas waktu algoritma adalah **O(n)**, dengan `n` sebagai jumlah task.

---

## Teknologi yang Digunakan
- **Python 3**
- **Tkinter** (GUI)
- **Matplotlib** (Visualisasi grafik)
- **tracemalloc** (Analisis memori)
- **time** (Analisis waktu eksekusi)

---

## Struktur Folder
Resource_Allocation_Optimization/
│
├── src/
│ ├── main.py # File utama (GUI & eksekusi)
│ ├── algorithm.py # Implementasi algoritma alokasi resource
│ └── utils.py # Analisis waktu dan memori
│
├── data/
│ ├── input/ # Data uji
│ └── output/ # Hasil eksekusi
│
├── tests/
│ └── test_algorithm.py # Unit testing
│
├── docs/
│ └── analysis_results.txt # Hasil analisis
│
├── README.md
└── requirements.txt

---

## Cara Menjalankan Program
1. Pastikan Python 3 sudah terinstall
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Jalankan Program
    python src/main.py
## Output Program

Tabel hasil alokasi task ke CPU atau GPU

Analisis:

Jumlah operasi

Waktu eksekusi

Penggunaan memori

Grafik perbandingan total energi CPU vs GPU

## Pengujian

Program diuji menggunakan beberapa skenario:

Best case

Average case

Worst case

Edge case

Boundary case

## Author

Nama: I WAYAN ALIT ARIMBAWA
NIM: 20230302037
Mata Kuliah: ALALISIS PERANCANGAN ALOGORITMA
Tahun: 2026
    

