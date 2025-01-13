#PPS "A024"
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five +=1
            elif bill == 10:
                if five == 0:
                    return False
                five -=1
                ten +=1
            elif bill == 20:
                if ten > 0 and five > 0:
                    ten -=1
                    five -=1
                elif five >= 3:
                    five -=3
                else:
                    return False
        return True
        """
        five와 ten은 각 지폐의 개수이다
        5달러는 바로, 10달러는 5달러가 있을 때 아닐때,
        20달러는 5, 10달러가 각각 있을때 하나씩 있을 때를 구분하여 조건문을 걸어주었다.
        위 조건을 만족하지 못하면 거스름돈을 줄수 없다 ==> False
        
        그리기 알고리즘이라고 보면 될 것 같다
        """