class MyStack:
    """
    Defined own stack methods.
    """

    def __init__(self):
        """
        initialize with an empty container
        """
        self.container = []

    def is_empty(self):
        """
        to check if the stack is empty
        :return: true if the size of stack is 0
        """
        return self.size() == 0

    def push(self, item):
        """
        pushes an item into the stack
        :param item: item to push inside the stack
        :return:
        """
        self.container.append(item)

    def pop(self):
        """
        to retrieve an item from the stack
        :return: the item at the to of stack
        """
        return self.container.pop()

    def peek(self):
        """
        to check the top most element of the stack but not remove it
        :return: the top most element of stack
        """
        if self.is_empty():
            raise Exception("Stack empty!")
        return self.container[-1]

    def size(self):
        """
        :return: the number of elements in the stack
        """
        return len(self.container)

    def show(self):
        """
        :return: returns all the elements in the stack
        """
        return self.container

