class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def insert_after(self,prev_node,new_node):
        if prev_node is None:
            print("prev node must be in ll");
            return
        new_node=Node(new_node)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def insert_last(self,last_node):
        new_node=Node(last_node)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while (last.next):
            last=last.next
        last.next=new_node
    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    llist=Linkedlist()
    llist.insert_last(6)
    llist.push(1)
    llist.push(7)
    llist.insert_last(4)
    llist.insert_after(llist.head.next,9)
    llist.print_list()
    
    
    
    
#deleting node from ll
class Node(self,data):
    self.data=data
    self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def delete(self,key):
        temp=self.head
        while(temp is not None):
            if(temp.data==key):
                self.head=temp.next
            temp=None
            return
        while(temp is not None):
            if temp.data==key:
                break
                prev=temp
                temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp=None



#delete at a particular position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def deletenode(self,pos):
        if self.head==None:
            return
        temp=self.head
        if pos==0:
            self.head=temp.next
            temp=None
            return
        for i in range(pos-1):
            temp=temp.next
            if temp is None:
                break
        next=temp.next.next
        temp.next=None
        temp.next=next
    def printlist(self):
        temp=self.head
        while(temp):
            print("%d" %(temp.data),end=" ")
            temp=temp.next
llist=LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)
print("old list")
llist.printlist()
llist.deletenode(0)
print("new list")
llist.printlist()



#reverse a ll
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print("%d" %(temp.data))
            temp=temp.next
llist=LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print("old list")
llist.printlist()
llist.reverse()
print("reverse list")
llist.printlist()    


#move last element to front
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print("%d" %(temp.data))
            temp=temp.next
    def movetofront(self):
        temp=self.head
        sec_last=None
        while(temp.next):
            sec_last=temp
            temp=temp.next
        sec_last.next=None
        temp.next=self.head
        self.head=temp
if __name__ == '__main__': 
    llist = LinkedList() 
      
    # swap the 2 nodes 
    llist.push(5) 
    llist.push(4) 
    llist.push(3) 
    llist.push(2) 
    llist.push(1) 
    print ("Linked List before moving last to front ") 
    llist.printlist() 
    llist.movetofront() 
    print ("Linked List after moving last to front ") 
    llist.printlist() 


#frequency of numbers
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def count(self,num):
        current=self.head
        count=0
        while(current is not None):
            if current.data==num:
                count=count+1
            current=current.next
        return count
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist=LinkedList()
llist.push(1) 
llist.push(3) 
llist.push(1) 
llist.push(2) 
llist.push(1) 
print ("count of 1 is % d" %(llist.count(21))) 

































       
            
    
                
        
                
            



























