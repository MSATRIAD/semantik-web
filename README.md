
# 🏛️ Website Translasi Sanghyang Tatwa Ajnyana

Aplikasi ini merupakan website translasi berbasis *Semantic Web* yang menampilkan transliterasi dan terjemahan naskah *Sanghyang Tatwa Ajnyana*. Dibangun menggunakan Python, Streamlit, dan GraphDB sebagai SPARQL endpoint RDF.

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

## ⚙️ Instalasi Aplikasi

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

## 🚀 Menjalankan Aplikasi

1. **Ubah `SPARQL_ENDPOINT` di `app.py`**:
   ```python
   SPARQL_ENDPOINT = "http://localhost:7200/repositories/NamaRepository"
   ```

2. **Instal dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi**:
   ```bash
   streamlit run app.py
   ```

---

## 🧭 Panduan Penggunaan

- Di **sidebar**:
  - Judul dan deskripsi aplikasi
  - Statistik jumlah triple RDF
  - Panduan pencarian

- Di **halaman utama**:
  - **Semua Baris**: Menampilkan seluruh translasi naskah
  - **Recto/Verso Dropdown**: Menampilkan translasi per sisi halaman
  - **Pencarian**: Masukkan keyword untuk mencari baris yang mengandung kata tersebut
  - **Highlight**: Hasil pencarian akan otomatis menyoroti keyword

---

## 👥 Anggota Kelompok

| Nama                    | NPM           |
|-------------------------|---------------|
| Muhammad Faiz Fahri     | 140810220002  |
| Marciano Lie            | 140810220022  |
| Muhammad Satria Dharma  | 140810220080  |

---

## 🔗 Link GitHub

📁 Repository GitHub: [https://github.com/MSATRIAD/semantik-web.git](https://github.com/MSATRIAD/semantik-web.git)
