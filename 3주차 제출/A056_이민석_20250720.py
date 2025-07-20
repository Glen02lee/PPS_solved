#PPS "A056"
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # nums2 순회하면서 각 숫자의 다음 큰 수를 저장
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # 스택에 남은 원소는 더 큰 수가 없는 것이므로 -1
        for num in stack:
            next_greater[num] = -1

        # nums1 기준으로 결과 반환
        return [next_greater[num] for num in nums1]