'''
    Challenge #9
    From : https://www.w3resource.com/python-exercises/oop/index.php

'''
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueueing(self, value):
        if len(self.queue) != 0:
            self.queue.insert(0, value)
        else:
            self.queue.append(value)

    def dequeueing(self):
        self.queue.pop()


queue1 = Queue()
queue1.enqueueing(1)
queue1.enqueueing(3)
queue1.enqueueing(18)
queue1.dequeueing()
print(queue1.queue)


