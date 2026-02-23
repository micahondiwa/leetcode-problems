class MyLinkedList(object):
    class Node:
        """Simple node for singly linked list."""
        def __init__(self, val=0):
            self.val = val
            self.next = None

    def __init__(self):
        """Initialize empty linked list with head and tail pointers."""
        self.head = None
        self.tail = None

    def get(self, index):
        """Return the value at given index (0-based), or -1 if invalid."""
        if index < 0 or not self.head:
            return -1

        curr = self.head
        pos = 0
        while curr:
            if pos == index:
                return curr.val
            curr = curr.next
            pos += 1
        return -1

    def addAtHead(self, val):
        """Add node with given value at the beginning."""
        new_node = self.Node(val)
        new_node.next = self.head
        self.head = new_node
        
        # If list was empty, tail must also point to new node
        if not self.tail:
            self.tail = new_node

    def addAtTail(self, val):
        """Add node with given value at the end – O(1) thanks to tail."""
        new_node = self.Node(val)
        
        if not self.head:
            # Empty list → new node is both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Non-empty → attach after current tail
            self.tail.next = new_node
            self.tail = new_node

    def addAtIndex(self, index, val):
        """Insert node at given index. Do nothing if index invalid."""
        if index < 0:
            return

        # Special case: insert at head
        if index == 0:
            self.addAtHead(val)
            return

        # Find previous node (position index-1)
        prev = self.head
        pos = 0
        while prev and pos < index - 1:
            prev = prev.next
            pos += 1

        # Index too large
        if not prev:
            return

        new_node = self.Node(val)
        new_node.next = prev.next
        prev.next = new_node

        # If inserted at end, update tail
        if not new_node.next:
            self.tail = new_node

    def deleteAtIndex(self, index):
        """Delete node at given index. Do nothing if index invalid."""
        if index < 0 or not self.head:
            return

        # Special case: delete head
        if index == 0:
            self.head = self.head.next
            # If list became empty, tail should be None
            if not self.head:
                self.tail = None
            return

        # Find previous node (position index-1)
        prev = self.head
        pos = 0
        while prev and pos < index - 1:
            prev = prev.next
            pos += 1

        # Cannot delete: index too large or no node at position
        if not prev or not prev.next:
            return

        # Delete by skipping
        to_delete = prev.next
        prev.next = to_delete.next

        # If we deleted the last node, update tail
        if not prev.next:
            self.tail = prev