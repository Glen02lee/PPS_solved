#PPS "A061"
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # 조정이 필요함 (0 기반이 아니기 때문)
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result