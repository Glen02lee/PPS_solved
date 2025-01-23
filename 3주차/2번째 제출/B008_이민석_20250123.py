#PPS "B008"
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

'''
이진탐색을 통해 시간복잡도를 줄여 구현했다 주어진 배열에서 타겟 넘버가 존재하는
인덱스를 찾거나 타겟을 삽입할 위치를 찾는 문제라고 생각했다
'''