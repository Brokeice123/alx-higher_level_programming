#!/usr/bin/python3
"""Singly Linked List"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Initialize a new Node
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the Node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List"""
    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the SinglyLinkedList.
        Args:
            value (int): The data of the new Node.
        """

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None:
                if current.next_node.data > value:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    break
                current = current.next_node
            if current.next_node is None:
                current.next_node = new_node

    def __str__(self):
        """Return the string representation of the SinglyLinkedList."""
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string

