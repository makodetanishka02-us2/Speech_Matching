class LCSComparator:

    def find_lcs(self, A, B):

        m = len(A)
        n = len(B)

        # Create DP table
        dp = [[0 for j in range(n + 1)]
              for i in range(m + 1)]

        # Fill DP table
        for i in range(m + 1):
            for j in range(n + 1):

                # Base case
                if i == 0 or j == 0:
                    dp[i][j] = 0

                # Characters are different
                elif A[i - 1] != B[j - 1]:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

                # Characters are same
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        # LCS length
        lcs_length = dp[m][n]

        # Traceback to find the actual LCS
        i = m
        j = n
        lcs = []

        while i > 0 and j > 0:

            if A[i - 1] == B[j - 1]:
                lcs.append(A[i - 1])
                i -= 1
                j -= 1

            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1

            else:
                j -= 1

        # We collected the LCS backwards
        lcs.reverse()

        lcs_string = "".join(lcs)

        return lcs_string, lcs_length, dp

    def calculate_similarity(self, A, B):

        lcs_string, lcs_length, dp = self.find_lcs(A, B)

        shorter_length = min(len(A), len(B))

        similarity = (lcs_length / shorter_length) * 100

        return lcs_string, lcs_length, similarity