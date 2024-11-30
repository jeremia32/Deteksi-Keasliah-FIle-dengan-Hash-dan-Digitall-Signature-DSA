# Proyek Verifikasi Keaslian File dengan RSA dan SHA-256

## **Alur Verifikasi Keaslian File**

### **1. Pengirim (Sender Mode)**
1.Pengirim pertama-tama menghitung hash dari file menggunakan fungsi generate_file_hash().
2.Tanda tangan digital (signature) dihasilkan dengan menandatangani hash menggunakan private key melalui fungsi sign_file().
3.Pengirim mengirimkan file asli dan file tanda tangan digital kepada penerima.

### **2. Penerima (Receiver Mode)**

1.Penerima menghitung ulang hash dari file yang diterima menggunakan fungsi generate_file_hash().
2.Tanda tangan diverifikasi menggunakan public key dengan fungsi verify_signature().
3.Jika tanda tangan dan hash cocok, file diterima sebagai asli dan tidak dimodifikasi.

---

## **Hubungan Antara Hash dan DSA**

- **Hashing** memastikan bahwa file yang diterima adalah salinan yang tepat dari file yang dikirim, tanpa perubahan apapun. Setiap perubahan dalam file akan menghasilkan hash yang berbeda, yang memungkinkan penerima untuk mendeteksi perubahan tersebut.
  
- **Digital Signature (DSA)** memberikan jaminan keaslian bahwa file tersebut benar-benar berasal dari pengirim yang sah dan tidak dimodifikasi selama pengiriman.

---

## **Kesimpulan**

- **Hashing** adalah teknik untuk mendeteksi integritas file. Dengan hashing, kita dapat dengan cepat memeriksa apakah file yang diterima sama persis dengan file yang dikirim.
  
- **Digital Signature (DSA)** adalah metode untuk memverifikasi keaslian dan asal-usul file, memastikan bahwa file benar-benar dikirim oleh pengirim yang sah dan tidak telah diubah oleh pihak lain selama pengiriman.

---

## **Persyaratan Sistem**

1.Python 3.8+.
2. Pustaka Python berikut:
Flask
cryptography

3. Folder dengan struktur berikut:
Deteksi-Keaslian-File/
├── app.py
├── app_logic.py
├── templates/
│   └── index.html
├── static/
├── files/
├── signatures/
├── keys/
│   ├── private_key.pem
│   ├── public_key.pem

---
## Digital Signature Verification Program ##
Program ini adalah aplikasi berbasis web menggunakan Flask untuk memverifikasi keaslian file melalui tanda tangan digital. Program ini mendukung algoritma RSA dan hashing SHA-256 untuk memastikan integritas dan keaslian file.




## **Cara Menggunakan Program**

### **Langkah-langkah untuk Menggunakan Program**

1. **Persiapan File.**
Sebelum menggunakan program, pastikan Anda memiliki file berikut:

File Asli: File yang ingin diverifikasi tanda tangannya.
Tanda Tangan Digital: File tanda tangan digital dari file asli.
Kunci Publik: File yang berisi kunci publik untuk verifikasi tanda tangan digital.

2. **Menjalankan Program**
Pastikan Anda Sudah Menginstal Dependensi Program membutuhkan beberapa pustaka Python. Jalankan perintah berikut untuk menginstal dependensi:
pip install flask cryptography  

3. Jalankan Server Flask Jalankan program dengan perintah berikut:
    ```bash
   python app.py


4. ** Mengunggah File untuk Verifikasi ** dengan perintah:

 Isi Formulir di Halaman Utama Anda akan melihat formulir dengan tiga bidang unggahan:

File: Unggah file asli.
Tanda Tangan: Unggah file tanda tangan digital yang sesuai.
Kunci Publik: Unggah file kunci publik untuk proses verifikasi.
Klik Tombol "Verify" Setelah mengisi semua bidang, klik tombol "Verify" untuk memulai proses verifikasi 


## **Kesimpulan** ##
Program ini memanfaatkan hashing dan RSA untuk memastikan file yang diterima tidak dimodifikasi dan berasal dari pengirim yang sah. Hal ini sangat berguna dalam menjaga keamanan file dalam pengiriman digital.



## **Kontribusi** ##
tim yang berkontribusi dalam membuat sistem ini terdiri dari :
syahrial jeremia sinaga -11422045 
Veri Marsil Marpaung -11422014
Diva Marchelliny Napitupulu -11422054

## **kontak** ##

Jika Anda memiliki pertanyaan atau saran, jangan ragu untuk menghubungi saya melalui email syahrialjsinaga@gmail.com

