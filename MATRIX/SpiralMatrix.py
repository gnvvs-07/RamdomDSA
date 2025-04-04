from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Move right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Move down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Move left
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # Move up
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
sol = Solution()
print(sol.spiralOrder(matrix))  # Expected output: [1,2,3,4,8,12,11,10,9,5,6,7]
