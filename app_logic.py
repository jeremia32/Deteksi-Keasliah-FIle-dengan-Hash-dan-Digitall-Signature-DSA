import hashlib
import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
)
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric import padding


def generate_file_hash(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "rb") as f:
        file_data = f.read()
    hash_object = hashlib.sha256(file_data)
    return hash_object.digest()


def create_signature(file_path, private_key_path):
    file_hash = generate_file_hash(file_path)
    with open(private_key_path, "rb") as key_file:
        private_key = load_pem_private_key(key_file.read(), password=None)
    
    # Menandatangani menggunakan RSA dengan algoritma PSS (probabilistic signature scheme)
    signature = private_key.sign(
        file_hash,  # Data yang akan ditandatangani
        PKCS1v15(),  # Padding yang digunakan untuk RSA
        hashes.SHA256()  # Hashing yang digunakan untuk RSA
    )
    return signature


def generate_keys(private_key_path, public_key_path):
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    # Serialize and save private key
    with open(private_key_path, "wb") as private_file:
        private_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
    # Serialize and save public key
    public_key = private_key.public_key()
    with open(public_key_path, "wb") as public_file:
        public_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )
    return private_key_path, public_key_path


def verify_signature(file_path, signature, public_key_path):
    try:
        # Membaca file yang diunggah untuk dihitung hash-nya
        with open(file_path, "rb") as file:
            file_data = file.read()
        
        # Membaca kunci publik
        with open(public_key_path, "rb") as key_file:
            public_key = load_pem_public_key(key_file.read())
        
        # Menghitung hash dari file
        file_hash = hashlib.sha256(file_data).digest()

        # Memverifikasi tanda tangan menggunakan kunci publik dan padding yang sesuai
        public_key.verify(
            signature,
            file_hash,
            padding.PKCS1v15(),  # Padding yang digunakan untuk RSA
            hashes.SHA256()      # Algoritma hashing yang digunakan untuk tanda tangan
        )
        print("Verification successful!")
        return True  # Berhasil diverifikasi

    except Exception as e:
        print("Verification failed:", e)
        return False  # Gagal diverifikasi
