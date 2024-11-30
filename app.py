from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from app_logic import create_signature, verify_signature, generate_keys

app = Flask(__name__)

UPLOAD_FOLDER = 'files'
SIGNATURE_FOLDER = 'signatures'
KEYS_FOLDER = 'keys'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SIGNATURE_FOLDER'] = SIGNATURE_FOLDER
app.config['KEYS_FOLDER'] = KEYS_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mode = request.form.get("mode")
        file = request.files.get("file")
        private_key = request.files.get("private_key")
        public_key = request.files.get("public_key")
        signature_file = request.files.get("signature")

        if not file or not mode:
            return render_template("result.html", result_message="File and mode are required.")

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename))
        file.save(file_path)

        if mode == "sender" and private_key:
            private_key_path = os.path.join(app.config["KEYS_FOLDER"], secure_filename(private_key.filename))
            private_key.save(private_key_path)

            signature = create_signature(file_path, private_key_path)
            if signature:
                signature_path = os.path.join(app.config["SIGNATURE_FOLDER"], file.filename + ".sig")
                with open(signature_path, "wb") as sig_file:
                    sig_file.write(signature)
                return render_template("result.html", result_message=f"Signature saved to {signature_path}")
            return render_template("result.html", result_message="Failed to generate signature.")

        elif mode == "receiver" and public_key and signature_file:
            public_key_path = os.path.join(app.config["KEYS_FOLDER"], secure_filename(public_key.filename))
            signature_path = os.path.join(app.config["SIGNATURE_FOLDER"], secure_filename(signature_file.filename))

            public_key.save(public_key_path)
            signature_file.save(signature_path)

            with open(signature_path, "rb") as sig_file:
                signature = sig_file.read()

            # Proses verifikasi
            verification_status = False
            try:
                is_valid = verify_signature(file_path, signature, public_key_path)
                if is_valid:
                    verification_status = True
            except Exception as e:
                verification_status = False
                print("Verification failed:", e)

            # Kirim status verifikasi ke frontend
            if verification_status:
                result_message = "Signature is valid. The file is authentic."
            else:
                result_message = "Signature is invalid. The file may have been tampered with."

            return render_template("result.html", result_message=result_message)

        return render_template("result.html", result_message="Invalid mode or missing files.")
    
    return render_template("index.html")


@app.route('/generate-keys', methods=['POST'])
def generate_keys_route():
    private_key_path = os.path.join(app.config["KEYS_FOLDER"], "private_key.pem")
    public_key_path = os.path.join(app.config["KEYS_FOLDER"], "public_key.pem")
    try:
        private_key, public_key = generate_keys(private_key_path, public_key_path)
        return jsonify({
            "message": "Keys generated successfully.",
            "private_key_path": private_key_path,
            "public_key_path": public_key_path,
        })
    except Exception as e:
        return jsonify({"error": f"Key generation failed: {str(e)}"}), 500

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(SIGNATURE_FOLDER, exist_ok=True)
    os.makedirs(KEYS_FOLDER, exist_ok=True)
    app.run(debug=True)
