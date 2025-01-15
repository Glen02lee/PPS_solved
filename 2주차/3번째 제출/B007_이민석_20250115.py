class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # 중간 인덱스
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1  # 오른쪽 탐색
            else:
                right = mid - 1  # 왼쪽 탐색
        
        return -1
        """
        이 코드는 이진탐색을 사용하여 배열에서 타겟수를 찾는 함수이다.
        이진 탐색을 사용하면 굉장히 빠르게 탐색할 수 있기 때문에 사용하였다.
        시간제한이 만약있었다면 선형탐색에 경우 굉장히 느려지기 때문에 배제하였다.
        이 이진탐색을 수행하는 반복문내에서 리턴이 되지 않는다면 배열에 타겟수가 없다는 뜻이므로
        -1을 리턴해줬다.
        """