class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):                        
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

def merge_lists(l1, l2):
    merge_ll = Node(0)
    current = merge_ll

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next
    
    if l1 is not None:
        current.next = l1
    elif l2 is not None:
        current.next = l2

    return merge_ll.next

def sort_merged_ll(head):
    current = head
    while current is not None:
        cur = current.next
        while cur is not None:
            if current.data > cur.data:
                current.data, cur.data = cur.data, current.data
            cur = cur.next
        current = current.next

def get_input():
    while True:
        try:
            node_inp = int(input("\033[33m\033[1mPlease enter a number: \033[0m"))
            if -100 <= node_inp <= 100:
                return node_inp
            else:
                ask_again = int(input("\033[31m\033[1mEnter a number in the range -100 to 100: \033[0m"))
                return ask_again
        except ValueError:
            print("\033[31m\033[1mEnter integers only.\033[0m")

def ask_again(ask):
    while True:
        try:
            inp = int(input(ask))
            if 0 <= inp < 50:
                return inp
            else:
                print("\033[31m\033[1mThe input is too high. Enter integers in the range 0-50 only.\033[0m") 
        except ValueError:
            print("\033[31m\033[1mEnter integers only.\033[0m")

data1 = []
data2 = []

ask_num1 = ask_again(("\033[35m\033[1mInput range you want in the first list: \033[0m"))
ask_num2 = ask_again(("\033[34m\033[1mInput range you want in the second list: \033[0m"))

if ask_num1 and ask_num2 in range(0, 50):
    for i1 in range(ask_num1):
        data_set1 = get_input()
        data1.append(data_set1)
    for i2 in range(ask_num2):
        data_set2 = get_input()
        data2.append(data_set2)
else:
    print("\033[31m\033[1mThe input is too high.\033[0m")

data1.sort()
print("\n\033[35m\033[1mList 1: \033[0m", data1)

data2.sort()
print("\033[34m\033[1mList 2: \033[0m", data2)

list1 = LinkedList()
for item in data1:
    list1.insert_at_end(item)
print("\n\033[33m\033[1mLink list 1: \033[0m")
list1.printLinkedList()

list2 = LinkedList()
for item in data2:
    list2.insert_at_end(item)
print("\n\033[33m\033[1mLink list 2: \033[0m")
list2.printLinkedList()

merged = merge_lists(list1.head, list2.head)
sort_merged_ll(merged)

merge_lists = LinkedList()
merge_lists.head = merged
print("\n\033[32m\033[1mMerged Link Lists: \033[0m")
merge_lists.printLinkedList()