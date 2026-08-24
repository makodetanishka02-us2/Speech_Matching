import wave
import numpy as np


class AudioToMatrixConverter:

    def __init__(self, frame_size=1024, hop_size=512):
        self.frame_size = frame_size
        self.hop_size = hop_size

    # Step 1: Read WAV and get PCM samples
    def read_wav(self, file_path):

        audio = wave.open(file_path, "rb")

        channels = audio.getnchannels()
        sample_width = audio.getsampwidth()
        sample_rate = audio.getframerate()
        number_of_frames = audio.getnframes()

        raw_data = audio.readframes(number_of_frames)

        audio.close()

        # Case study expects PCM audio.
        # This implementation handles 16-bit PCM.
        if sample_width != 2:
            raise ValueError("Only 16-bit PCM WAV files are supported.")

        # Convert raw PCM bytes into numbers
        samples = np.frombuffer(raw_data, dtype=np.int16)

        # Stereo → Mono
        if channels == 2:
            samples = samples.reshape(-1, 2)
            samples = samples.mean(axis=1)

        samples = samples.astype(np.float32)

        return sample_rate, samples

    # Step 2: Create spectrogram using FFT
    def create_spectrogram(self, samples):

        frames = []

        for start in range(
            0,
            len(samples) - self.frame_size + 1,
            self.hop_size
        ):

            frame = samples[start:start + self.frame_size]

            # Hamming window
            window = np.hamming(self.frame_size)

            frame = frame * window

            # FFT
            fft_result = np.fft.rfft(frame)

            # Magnitude = strength of frequencies
            magnitude = np.abs(fft_result)

            frames.append(magnitude)

        # Convert list of frames into matrix
        spectrogram = np.array(frames)

        # Currently:
        # rows    = time
        # columns = frequency
        #
        # We want:
        # rows    = frequency
        # columns = time

        spectrogram = spectrogram.T

        return spectrogram

    # Step 3: Resize spectrogram to 64 × 64
    def resize_to_64x64(self, matrix):

        old_rows, old_cols = matrix.shape

        row_indices = np.linspace(
            0,
            old_rows - 1,
            64
        ).astype(int)

        col_indices = np.linspace(
            0,
            old_cols - 1,
            64
        ).astype(int)

        resized_matrix = matrix[
            np.ix_(row_indices, col_indices)
        ]

        return resized_matrix

    # Step 4: Convert to 0/1
    def binarize(self, matrix):

        threshold = np.mean(matrix)

        binary_matrix = (matrix > threshold).astype(int)

        return binary_matrix

    # Complete Stage 2
    def convert(self, file_path):

        sample_rate, samples = self.read_wav(file_path)

        spectrogram = self.create_spectrogram(samples)

        matrix_64 = self.resize_to_64x64(spectrogram)

        binary_matrix = self.binarize(matrix_64)

        return binary_matrix