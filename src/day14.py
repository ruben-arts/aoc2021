class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        #    new node as head
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def get_as_list(self):
        temp = self.head
        l = []
        while temp:
            l.append(temp.data)
            temp = temp.next
        return l

    def printList(self):
        temp = self.head
        string = ""
        while temp:
            string += temp.data
            temp = temp.next
        print(string)

    def len(self):
        temp = self.head
        len = 0
        while temp:
            len += 1
            temp = temp.next
        return len

if __name__ == '__main__':
    with open("../input/input_day14.txt", "r") as file:
        lines = file.read().splitlines()

    start = lines[0]

    insertions = lines[2:]

    commands = {}
    for i in insertions:
        pair, insertable = i.split(" -> ")

        commands[pair] = insertable

    ll = LinkedList()
    for elm in start:
        ll.append(elm)
    ll.printList()
    print()

    last_len = 1
    for _ in range(10):
        current_node = ll.head
        while current_node:
            next_node = current_node.next
            if next_node:
                if current_node.data + next_node.data in commands.keys():
                    ll.insert_after(current_node, commands[current_node.data + next_node.data])
            current_node = next_node


    current_node = ll.head
    count_dict = {}
    while current_node:
        if current_node.data in count_dict.keys():
            count_dict[current_node.data] += 1
        else:
            count_dict[current_node.data] = 1
        current_node = current_node.next
    print(f"max - min = {max(count_dict.values()) - min(count_dict.values())}")