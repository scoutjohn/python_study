from DSA.queue.Queue import Queue

class QueueExample:
    def __init__(self):
        self.queue = Queue()

    def queue_data(self,element):
        self.queue.enqueue(element)

    def run(self):
        while self.queue.peak():
            self.print_value(self.queue.dequeue())

    def print_value(self,value):
        print(f"{value}")