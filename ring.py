class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.next = None

    def __str__(self):
        return f"Node({self.node_id})"


class RingNetwork:
    def __init__(self):
        self.head = None

    def add_node(self, node_id):
        new_node = Node(node_id)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display_ring(self):
        if self.head is None:
            print("Ring is empty")
            return

        temp = self.head
        while True:
            print(temp.node_id, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    def elect_leader(self, start_id):
        if self.head is None:
            print("No nodes in the ring")
            return

        temp = self.head

        while temp.node_id != start_id:
            temp = temp.next
            if temp == self.head:
                print("Start node not found")
                return

        print(f"Election started from Node {start_id}")

        max_id = temp.node_id
        current = temp.next

        while current != temp:
            if current.node_id > max_id:
                max_id = current.node_id
            current = current.next

        print(f"Leader elected: Node {max_id}")
        return max_id