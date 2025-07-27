#PPS "A067"
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # 중복 문자 제거
            else:
                stack.append(char)  # 스택에 추가
        return ''.join(stack)