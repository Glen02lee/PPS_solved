#PPS "A055"
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0

        for ch in s:
            if ch == '(':
                if opened > 0:
                    result.append(ch)
                opened += 1
            elif ch == ')':
                opened -= 1
                if opened > 0:
                    result.append(ch)
        
        return ''.join(result)