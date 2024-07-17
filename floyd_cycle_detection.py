class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        
def detectLoop(head):
    slowPointer = head
    fastPointer = head
    slow2 = head
    while (slowPointer != None
           and fastPointer != None
           and fastPointer.next != None):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if (slowPointer == fastPointer):
            break
    while True:
            if slowPointer == slow2:
                break
            slowPointer = slowPointer.next
            slow2 = slow2.next            
    return slow2.data

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
 

temp = head
while (temp.next != None):
    temp = temp.next
 
temp.next = head

print(detectLoop(head))


 
    