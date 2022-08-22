class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
    
    def display(self):
        nodes_data = []
        while self:
            nodes_data.append(self.data)
            self = self.next
        print(nodes_data)
    
    def append(self, *args): 
        for arg in args: 
            while self.next:
                self = self.next
            self.next = Node(arg)

    def pop(self):
        prev = None
        while self.next:
            self, prev = self.next, self
        prev.next = None

    def length(self):
        i = 1
        while self.next:
            i+=1
            self = self.next
        return i

