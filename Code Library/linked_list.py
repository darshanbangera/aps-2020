class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=node()

    def insert_node(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
