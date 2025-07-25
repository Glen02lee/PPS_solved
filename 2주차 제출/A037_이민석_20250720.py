#PPS "A037"
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right + 1) 
                if all(int(d) != 0 and num % int(d) == 0 for d in str(num))]