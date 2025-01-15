#PPS "B002"
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        map_emp = {emp.id: emp for emp in employees}

        def dfs(emp_id):
            employee = map_emp[emp_id]
            total = employee.importance
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            return total

        return dfs(id)
    
"""
직원의 객체를 빠르게 조회하기 위해선 딕셔너리 기능을 사용해야겠다고 생각했다
문제에서 제공된 부분을 보고 키와 값의 쌍으로 이루어져있어서 딕셔너리가 잘 어울릴거라고 생각했다
자료구조를 공부하면서 기억나는 것은 아마 해시값으로 변환을 할 수 있고, 순차적으로 값을 찾는 리스트보다
속도가 훨씬 빠른것으로 알고 있다.
전체 직원들의 중요도 합을 구하는 문제이므로 DFS를 통해 트리 구조안에서 구하면 좋겠다는 생각이 들었다.

"""