#PPS "A014"
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []
        start = nums[0]
        
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == nums[i]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i]}")
                if i < len(nums) - 1:
                    start = nums[i + 1]
        
        return result