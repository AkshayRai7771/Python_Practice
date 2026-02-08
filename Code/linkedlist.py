class Node:
    def __init__(self,value,next=None):
        self.data = value
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_in_the_begining(self,value):
        node = Node(value,self.head)
        self.head = node
    
    def insert_in_the_end(self,value):
        if self.head == None:
            node = Node(value,None)
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr=curr.next
            
            curr.next = Node(value,None)


    def insert_list(self,data_set):
        self.head = None
        for data in data_set :
            self.insert_in_the_end(data)

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        curr = self.head
        result = ""

        while curr:
            result += str(curr.data) + "-->"
            curr = curr.next
        
        print(result)


    def find_length(self):
        curr =self.head
        count = 0
        while curr:
            curr = curr.next
            count+=1
        print("Length is : ",count)

        return count

    def remove_at(self,index):
        if index<0 or index >= self.find_length():
            raise Exception("Index out of range!")
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        curr = self.head
        while curr:
            if count == index -1:
                curr.next = curr.next.next
            curr = curr.next
            count+=1

    def insert_at(self,index,value):
        if index<0 or index>=self.find_length():
            raise Exception("Index out of range!")
        
        if index == 0:
            self.insert_in_the_begining(value)
        else:
            count = 0
            curr = self.head
            node = Node(value,None)
            while curr:
                if count == index-1:
                    nxt = curr.next
                    curr.next = node
                    node.next = nxt
                
                curr = curr.next
                count+=1



        
if __name__ == "__main__":
    Link_list = Linkedlist()
    l = [1,2,3,4,5,6]
    Link_list.insert_list(l)
    Link_list.insert_at(6,30)
    Link_list.display()