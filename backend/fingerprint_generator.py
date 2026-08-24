class RowColCompressor:

    def __init__(self):
        self.hex_chars = "0123456789ABCDEF"

    def average(self, values):

        # 16 values → 8 groups of 2 values
        averages = []

        for i in range(0, 16, 2):

            group = values[i:i + 2]

            average = sum(group) / len(group)

            averages.append(average)

        return averages

    def quantize(self, values):

        maximum = max(values)

        # Avoid division by zero
        if maximum == 0:
            return [0] * len(values)

        quantized = []

        for value in values:

            level = round((value / maximum) * 15)

            # Make sure level stays between 0 and 15
            level = max(0, min(15, level))

            quantized.append(level)

        return quantized

    def convert_to_hex(self, levels):

        fingerprint = ""

        for level in levels:

            fingerprint += self.hex_chars[level]

        return fingerprint

    def compress(self, freq_density, time_density):

        # 16 frequency values → 8 averages
        freq_averages = self.average(freq_density)

        # 16 time values → 8 averages
        time_averages = self.average(time_density)

        # 8 + 8 = 16 average values
        combined = freq_averages + time_averages

        # Convert averages to levels 0–15
        levels = self.quantize(combined)

        # Convert levels to hexadecimal characters
        fingerprint = self.convert_to_hex(levels)

        return fingerprint