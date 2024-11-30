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
```bash
pip install flask cryptography  

Jalankan Server Flask Jalankan program dengan perintah berikut:
```bash
pip install flask cryptography 

5. **Generate private key** dengan perintah:

   ```bash
   openssl genrsa -out private_key.pem 2048

6. **Generate public key** dengan perintah:
   ```bash
   openssl rsa -in private_key.pem -pubout -out public_key.pem
7. **Simpan keys tersebut dalam folder keys.**
8. Simpan file yang akan diberi signature dan diuji keasliannya dalam folder file.
9. Simpan signature di folder signature, seperti struktur folder pada repositori ini.

## **Menjalankan Program di Mode Pengirim (Sender Mode)**

Untuk menjalankan program di **mode pengirim**, gunakan perintah berikut:

```bash
python app.py --mode sender --file path/to/your/file.txt --private-key path/to/private_key.pem --signature path/to/signature.sig

contoh:
python app.py --mode sender --file file/test.txt --private-key keys/private_key.pem --signature signature/signature.sig 

--mode sender: Menentukan mode untuk pengirim yang menghasilkan tanda tangan.
--file path/to/your/file.txt: Menunjukkan file yang akan diberikan tanda tangan.
--private-key path/to/private_key.pem: Menunjukkan path ke private key yang digunakan untuk menandatangani.
--signature path/to/signature.sig: Menunjukkan path tempat menyimpan signature yang dihasilkan.


## **Menjalankan Program di Mode penerima (receiver Mode)**
```bash
python app.py --mode receiver --file path/to/your/file.txt --public-key path/to/public_key.pem --signature path/to/signature.sig

![Screenshot 2024-11-26 115903](https://github.com/user-attachments/assets/0771c479-e583-465e-93e9-0106779ab12f)


