from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tempfile

from audio_to_matrix import AudioToMatrixConverter
from matrix_compressor import MatrixCompressor
from profile_extraction import extract_profiles
from fingerprint_generator import RowColCompressor
from lcs_comparison import LCSComparator


app = Flask(__name__)
CORS(app)


# Create your existing objects
converter = AudioToMatrixConverter()
compressor = MatrixCompressor()
fingerprint_generator = RowColCompressor()
comparator = LCSComparator()


def process_audio(file_path):
    """
    Runs the existing SpeechMatch pipeline
    on one WAV file.
    """

    # Stage 1: WAV → 64x64 matrix
    matrix_64 = converter.convert(file_path)

    # Stage 2: 64x64 → 16x16
    matrix_16 = compressor.compress(matrix_64)

    # Stage 3: Extract frequency and time profiles
    freq, time = extract_profiles(matrix_16)

    # Stage 4: Generate fingerprint
    fingerprint = fingerprint_generator.compress(
        freq,
        time
    )

    return fingerprint


@app.route("/compare", methods=["POST"])
def compare():

    # Check whether both files were uploaded
    if "audioA" not in request.files or "audioB" not in request.files:
        return jsonify({
            "error": "Both audio files are required."
        }), 400

    audio_a = request.files["audioA"]
    audio_b = request.files["audioB"]

    # Check filenames
    if audio_a.filename == "" or audio_b.filename == "":
        return jsonify({
            "error": "Please select both WAV files."
        }), 400

    temp_a = None
    temp_b = None

    try:

        # Create temporary files
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as file_a:

            audio_a.save(file_a.name)
            temp_a = file_a.name


        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as file_b:

            audio_b.save(file_b.name)
            temp_b = file_b.name


        # ==========================================
        # RUN YOUR EXISTING PIPELINE
        # ==========================================

        fingerprint_a = process_audio(temp_a)
        fingerprint_b = process_audio(temp_b)


        # ==========================================
        # LCS COMPARISON
        # ==========================================

        lcs, length, similarity = comparator.calculate_similarity(
            fingerprint_a,
            fingerprint_b
        )


        # ==========================================
        # SEND RESULT TO FRONTEND
        # ==========================================

        return jsonify({

            "success": True,

            "fingerprintA": fingerprint_a,

            "fingerprintB": fingerprint_b,

            "lcs": lcs,

            "lcsLength": length,

            "similarity": similarity

        })


    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


    finally:

        # Delete temporary files
        if temp_a and os.path.exists(temp_a):
            os.remove(temp_a)

        if temp_b and os.path.exists(temp_b):
            os.remove(temp_b)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )