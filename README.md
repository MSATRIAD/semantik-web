
# 🏛️ Website Translasi Sanghyang Tatwa Ajnyana

Aplikasi ini merupakan website translasi berbasis *Semantic Web* yang menampilkan transliterasi dan terjemahan naskah *Sanghyang Tatwa Ajnyana*. Dibangun menggunakan Python, Streamlit, dan GraphDB sebagai SPARQL endpoint RDF.

## 👥 Anggota Kelompok

| Nama                    | NPM           |
|-------------------------|---------------|
| Muhammad Faiz Fahri     | 140810220002  |
| Marciano Lie            | 140810220022  |
| Muhammad Satria Dharma  | 140810220080  |

---

## 📦 Daftar Isi

- [Fitur Aplikasi](#fitur-aplikasi)
- [Instalasi Aplikasi](#instalasi-aplikasi)
- [Menjalankan Aplikasi](#menjalankan-aplikasi)
- [Panduan Penggunaan](#panduan-penggunaan)
- [Anggota Kelompok](#anggota-kelompok)
- [Link GitHub](#link-github)

---

## 🧩 Fitur Aplikasi

- Menampilkan seluruh baris transliterasi dan terjemahan naskah (per recto dan verso)
- Fitur pencarian teks (transliterasi maupun terjemahan) berdasarkan keyword
- Tampilan responsif dan terstruktur dengan filter per sisi halaman
- Total statistik triple RDF ditampilkan di sidebar
- Highlight otomatis pada keyword hasil pencarian

---

## 🌏 Akses Aplikasi Melalui URL Public

**Website Dapat Melalui URL Di Bawah ini**
https://sanghyang-tatwa-ajnyana.streamlit.app/

---

## ⚙️ Instalasi Aplikasi Secara Lokal

1. **Clone repository ini** ke local:
   ```bash
   git clone https://github.com/MSATRIAD/semantik-web.git
   ```

2. **Buat endpoint RDF di GraphDB**:
   - Buka aplikasi **GraphDB Desktop**
   - Klik **GraphDB Workbench** → buka di browser (port `7200`)
   - Masuk ke **Repositories** → *Create new repository*
   - Gunakan pengaturan default dan beri nama repository
   - Upload file RDF (format Turtle) dari folder repository lokal ke GraphDB

---

## 🧭 Panduan Penggunaan

- Di **sidebar**:
  - Judul dan deskripsi aplikasi
  - Statistik jumlah triple RDF
  - Panduan pencarian

- Di **halaman utama**:
  - **List Naskah Berdasarkan Halaman**: Menampilkan seluruh translasi naskah
  - **List Naskah Berdasarkan Recto/Verso**: Menampilkan translasi per sisi halaman
  - **Pencarian**: Masukkan keyword untuk mencari baris yang mengandung kata tersebut
  - **Informasi**: Memberikan informasi mengenai website Sanghyang Tatwa Ajnyana 

---

## 🔗 Link GitHub

📁 Repository GitHub: [https://github.com/MSATRIAD/semantik-web.git](https://github.com/MSATRIAD/semantik-web.git)
