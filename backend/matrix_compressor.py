class MatrixCompressor:

    def __init__(self, block_size=4, energy_ratio_threshold=0.5):
        self.block_size = block_size
        self.energy_ratio_threshold = energy_ratio_threshold

    def compress(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        if rows != 64 or cols != 64:
            raise ValueError("Input matrix must be 64x64.")

        compressed = []

        for i in range(0, rows, self.block_size):

            new_row = []

            for j in range(0, cols, self.block_size):

                block = [
                    row[j:j + self.block_size]
                    for row in matrix[i:i + self.block_size]
                ]

                energetic_count = sum(
                    cell
                    for row in block
                    for cell in row
                )

                total_cells = self.block_size * self.block_size

                energy_ratio = energetic_count / total_cells

                if energy_ratio >= self.energy_ratio_threshold:
                    new_row.append(1)
                else:
                    new_row.append(0)

            compressed.append(new_row)

        return compressed

    def print_matrix(self, matrix):

        for row in matrix:
            print("".join(str(cell) for cell in row))