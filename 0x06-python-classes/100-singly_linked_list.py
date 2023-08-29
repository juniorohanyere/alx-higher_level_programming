#!/usr/bin/python3

''' a singly-linked list '''


class Node:
    ''' a node in a singly-linked list '''

    def __init__(self, data, next_node=None):
        ''' initialize values for the node

        Args:
            data (int): the data of the Node.
            next_node (Node): the next node of the the Node.
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' retrieve the data of the Node '''

        return (self.__data)

    @data.setter
    def data(self, value):
        ''' set the value for the data for the Node '''

        if not isinstance(value, int):
            raise (TypeError("data must be an integer"))

        self.__data = value

    @property
    def next_node(self):
        ''' retrieve the value of the next node '''

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        ''' set value for the next node '''

        if not isinstance(value, Node) and value is not None:
            raise (TypeError("next_node must be a Node object"))

        self.__next_node = value


class SinglyLinkedList:
    ''' singly linked list class '''

    def __init__(self):
        ''' initialize values for the singly linked list '''

        self.__head = None

    def sorted_insert(self, value):
        ''' inserts a new node into the singly linked list

        Args:
            value (Node): value of the new node to insert
        '''

        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new

        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new

        else:
            tmp = self.__head

            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node

            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        ''' the string definition for how the values are to be printed '''

        value = []
        tmp = self.__head

        while tmp is not None:
            value.append(str(tmp.data))
            tmp = tmp.next_node

        return ('\n'.join(value))
