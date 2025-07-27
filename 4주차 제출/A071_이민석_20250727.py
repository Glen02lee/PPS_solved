#PPS "A071"
class MyQueue:

    def __init__(self):
        self.in_stack = []    # push할 때 사용하는 스택
        self.out_stack = []   # pop, peek할 때 사용하는 스택

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()              # out_stack이 비어 있으면 in_stack의 값을 옮기기
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())