class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ptr = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def Display(self):
        curr = self.head
        while(curr.ptr is not None):
            print(curr.data,end=" -> ")
            curr = curr.ptr
        print(curr.data)
        print()

    def Insert(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
        else:
            curr = self.head
            while (curr.ptr is not None):
                curr = curr.ptr
            curr.ptr = NewNode

    def Remove(self,data):
        if(self.head is not None):
            if(self.head.data == data):
                self.head = self.head.ptr
            else:
                curr = self.head
                while(curr.ptr is not None and curr.ptr.data!=data):
                    curr = curr.ptr
                if(curr.ptr is not None):
                    curr.ptr = curr.ptr.ptr
                else:
                    print("Data Not Found")
        else:
            print("LL is Empty")

LL = LinkedList()
LL.Insert(1)
LL.Insert(2)
LL.Insert(3)
LL.Insert(4)
LL.Insert(5)
LL.Display()
LL.Remove(9)
LL.Display()
