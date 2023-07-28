from queue import Queue

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        for item in range(self.q1.qsize() - 1):
            self.q2.put(self.q1.get())
        pop_element = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return pop_element

    def top(self) -> int:
        for item in range(self.q1.qsize() - 1):
            self.q2.put(self.q1.get())
        top_element = self.q1.get()
        self.q2.put(top_element)
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def empty(self) -> bool:
        return False if self.q1.qsize() else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()