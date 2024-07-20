class Node:
    def __init__(self,Data) -> None:
        self.head = None
        self.Data = Data
        self.last = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last = None

    def Display(self):
        curr = self.head
        while(curr.ptr is not None):
            print(curr.data,end=" -> ")
            curr = curr.ptr
        print(curr.data)
        print()

    def Insert(self,Data) -> None:
        