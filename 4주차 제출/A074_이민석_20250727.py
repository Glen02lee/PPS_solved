#PPS "A074"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. 모든 문자를 소문자로 변환하고, 영문자와 숫자만 필터링
        filtered = [c.lower() for c in s if c.isalnum()]
        # 2. 앞에서부터 읽은 것과 뒤에서부터 읽은 것이 같은지 확인
        return filtered == filtered[::-1]