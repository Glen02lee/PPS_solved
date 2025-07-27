#PPS "A063"
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 이진 문자열 → 정수로 변환한 후 더하기
        sum_decimal = int(a, 2) + int(b, 2)
        # 다시 이진 문자열로 변환
        return bin(sum_decimal)[2:]