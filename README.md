# Audio_Matching
#### Audio comparison tool using audio fingerprinting and Longest Common Subsequence Algorithm
#### It is an audio-matching system that compares two WAV audio files and determines how similar they are using **audio-to-matrix conversion, matrix compression, fingerprint generation, and Longest Common Subsequence (LCS)**.

#### Work Flow
#### 1)WAV Audio Files
#### 2)Audio → Matrix Conversion
#### 3)64 × 64 Matrix
#### 4)Matrix Compression
#### 5)16 × 16 Matrix
#### 6)Frequency & Time Profile Extraction
#### 7)Fingerprint Generation
#### 8)LCS Comparison
#### 9)Similarity Score

### Tech Stack
#### Backend
##### Python
##### Flask
##### Flask-CORS
#### Algorithms
##### Longest Common Subsequence (LCS)
#### Data Processing
##### Numerical matrix representation
###### Frequency profile extraction
###### Time profile extraction
#### Frontend
##### JavaScript
##### CSS
##### Html
##### The backend can communicate with a web frontend through the /compare REST API using HTTP requests.

### Advantages:
#### 1)Simple and easy to understand The project uses basic audio processing, matrix operations, and the LCS Dynamic Programming algorithm.
#### 2)Reduces large audio data significantly A raw .wav file is converted into a 64×64 matrix → 16×16 matrix → 16-character fingerprint, making the comparison much more compact.
#### 3)Uses LCS effectively : LCS provides a clear numerical measure of how much structural information is common between the two generated audio fingerprints.
#### 4)Modular and reusable design Each stage—audio conversion, matrix compression, profiling, fingerprint generation, and LCS comparison—can be implemented separately, making the system easier to test, debug, and modify  

### Applications
#### 1)Audio pattern matching
#### 2)Speech similarity analysis
#### 3)Audio duplicate detection

#### Audio_Matching is designed primarily for **educational and academic purposes** to demonstrate audio processing, fingerprint generation, matrix compression, and the **Longest Common Subsequence (LCS)** algorithm.
#### - The system is intended to compare **similar speech recordings, preferably from the same speaker**, rather than identify or authenticate a person's identity.
#### - Differences in microphone quality, background noise, pronunciation, speaking speed, volume, or recording conditions may affect the similarity score.
#### - The similarity score should **not be treated as a definitive measure of speaker identity or authenticity**.
#### - This project is a demonstration of an algorithmic approach and is **not intended for security, biometric authentication, legal, or high-stakes applications**.
