class Queue:
    def __init__(self):
        self.data =[]

    def enqueue(self,element):
        self.data.append(element)

    def dequeue(self):
        if len(self.data)>0:
            return self.data.pop(0)
        else:
            return None

    def peak(self):
        if len(self.data)>0:
            return self.data[0]
        else:
            return None