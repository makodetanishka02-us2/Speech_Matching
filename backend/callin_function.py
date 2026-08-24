from audio_to_matrix import AudioToMatrixConverter
from matrix_compressor import MatrixCompressor
from profile_extraction import extract_profiles
from fingerprint_generator import RowColCompressor
from lcs_comparison import LCSComparator


#Stage 1
converter = AudioToMatrixConverter()
compressor = MatrixCompressor()
fingerprint_generator = RowColCompressor()

matrix_64_exp1 = converter.convert("../wav_files/Exponential_1.wav")
matrix_64_exp2 = converter.convert("../wav_files/Exponential_2.wav")
# stage 2
print("64x64 Matrix:")
for row in matrix_64_exp1:
    print("".join(str(cell) for cell in row))
# print("64x64 Matrix:")
# for row in matrix_64_exp2:
#     print("".join(str(cell) for cell in row))


# Stage 3
matrix_16_exp1 = compressor.compress(matrix_64_exp1)
# matrix_16_exp2 = compressor.compress(matrix_64_exp2)

print("\n16x16 Compressed Matrix:")
for row in matrix_16_exp1:
    print("".join(str(cell) for cell in row))

# print("\n16x16 Compressed Matrix:")
# for row in matrix_16_exp2:
#     print("".join(str(cell) for cell in row))


# Stage 4
freq_exp1, time_exp1 = extract_profiles(matrix_16_exp1)

print("\nFrequency Density:")
print(freq_exp1)

print("\nTime Density:")
print(time_exp1)

# freq_exp2, time_exp2 = extract_profiles(matrix_16_exp2)

# print("\nFrequency Density:")
# print(freq_exp2)

# print("\nTime Density:")
# print(time_exp2)

# stage 5
fingerprint_exp1 = fingerprint_generator.compress(
    freq_exp1,
    time_exp1
)
# fingerprint_exp2 = fingerprint_generator.compress(
#     freq_exp2,
#     time_exp2
# )
print("Exponential 1:")
print(fingerprint_exp1)

# print("\nExponential 2:")
# print(fingerprint_exp2)

comparator = LCSComparator()

# lcs, length, dp = comparator.find_lcs(fingerprint_exp1, fingerprint_exp2)

# print("String 1:", fingerprint_exp1)
# print("String 2:", fingerprint_exp2)
# print("LCS:", lcs)
# print("LCS Length:", length)

# print("\nDP Table:")

# for row in dp:
#     print(row)

# lcs, length, similarity = comparator.calculate_similarity(fingerprint_exp1, fingerprint_exp2)

# print("\nSimilarity:", similarity, "%")

# polynomial
matrix_64_poly = converter.convert("../wav_files/Polynomial.wav")

matrix_16_poly = compressor.compress(matrix_64_poly)

print("\n16x16 Compressed Matrix:")
for row in matrix_16_poly:
    print("".join(str(cell) for cell in row))

freq_poly, time_poly = extract_profiles(matrix_16_poly)

print("\nFrequency Density:")
print(freq_poly)

print("\nTime Density:")
print(time_poly)

fingerprint_poly = fingerprint_generator.compress(
    freq_poly,
    time_poly
)
print("Polynomial:")
print(fingerprint_poly)

lcs, length, dp = comparator.find_lcs(fingerprint_exp1, fingerprint_poly)

print("String 1:", fingerprint_exp1)
print("String 2:", fingerprint_poly)
print("LCS:", lcs)
print("LCS Length:", length)

print("\nDP Table:")

for row in dp:
    print(row)

lcs, length, similarity = comparator.calculate_similarity(fingerprint_exp1, fingerprint_poly)

print("\nSimilarity:", similarity, "%")