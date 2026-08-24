def compute_freq_density(matrix):
    return [sum(row) for row in matrix]
def compute_time_density(matrix):
    num_cols = len(matrix[0])

    return [
        sum(row[j] for row in matrix)
        for j in range(num_cols)
    ]
def extract_profiles(matrix):

    freq_density = compute_freq_density(matrix)

    time_density = compute_time_density(matrix)

    return freq_density, time_density