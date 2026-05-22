class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
        The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.next = None


    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        return self.value


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        current_node = self._head
        if current_node is None:
            return 0
        length = 1
        while current_node.next is not None:
            length += 1
            current_node = current_node.next
        return length
            
    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Returns
            item

        Raises
            IndexError if n >= length
        """
        if n >= self.length():
            raise IndexError("n >= length")
        current_node = self._head
        for i in range(n):
            current_node = current_node.next
        return current_node.get()

    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        if n > self.length():
            raise IndexError("n > length")
        elif n == 0:
            next_node = self._head
            self._head = Node(item)
            self._head.next = next_node
        elif n == self.length():
            self.append(item)
        else:
            current_node = self._head
            for i in range(n-1):
                current_node = current_node.next
            new_node = Node(item)
            new_node.next = current_node.next
            current_node.next = new_node

    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        if self._head is None:
            self._head = Node(item)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(item)

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Raises
            IndexError if n > length
        """
        if n > self.length():
            raise IndexError("n > length")
        elif n == 0:
            self._head = self._head.next
        else:
            current_node = self._head # 0th item
            for i in range(n-1):
                current_node = current_node.next #loops until the item before
            current_node.next = current_node.next.next
       
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        current_node = self._head
        if current_node is None:
            return False
        elif current_node.get() == item:
            return True
        else:
            while current_node.next is not None:
                if current_node.get() == item:
                    return True
                current_node = current_node.next
            return current_node.get() == item