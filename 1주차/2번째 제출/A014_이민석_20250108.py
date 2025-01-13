class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result
        """
       연속된 숫자 범위를 파악한 후 이를 요약하는 문제이다
       연속된 숫자가 있다면 화살표 ->를 이용해서 시작점과 끝을 알려주는 것인데,
       반복문을 통해 간단히 구현해보았다.
       f"{}" 문법을 통해 배열에 추가하는 방식대로 구현했다.
       
       
        """
