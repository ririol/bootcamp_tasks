from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        for item in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        pop_element = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        return pop_element

    def top(self) -> int:
        for item in range(len(self.q1) - 1):
            self.q2.append(self.q1.popleft())
        top_element = self.q1.pop()
        self.q2.append(top_element)
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
        return False if len(self.q1) else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()