#PPS "A002"
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        if numRows == 0:
            return result
        
        result.append([1])
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        return result