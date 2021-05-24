"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_next(self, item):
        self.next = item

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


class CustomList:
    def __init__(self, *data):
        self.size = len(data)

        if self.size == 0:
            self.head = Item()
        else:
            self.head = Item(data[0])
            cur_item = self.head

            for value in data[1:]:
                new_item = Item(value)
                cur_item.set_next(new_item)
                cur_item = new_item

    def append(self, value):
        if self.head.get_data() is None:
            self.head.set_data(value)
        else:
            new_item = Item(value)
            cur_item = self.head

            while cur_item.get_next():
                cur_item = cur_item.get_next()

            cur_item.set_next(new_item)

        self.size += 1

    def add_start(self, value):
        if self.head.get_data() is None:
            self.head.set_data(value)
        else:
            new_item = Item(value)
            new_item.set_next(self.head)
            self.head = new_item

        self.size += 1

    def remove(self, value):
        cur_item = self.head

        while cur_item.get_next():
            if cur_item.get_next().get_data() == value:
                cur_item.set_next(cur_item.get_next().get_next())
                self.size -= 1
                break

            cur_item = cur_item.get_next()
        else:
            raise ValueError

    def __getitem__(self, index):
        if self.size <= index:
            raise IndexError

        cur_item = self.head
        while index != 0:
            cur_item = cur_item.get_next()
            index -= 1

        return cur_item.get_data()

    def __setitem__(self, index, data):
        if self.size <= index:
            raise IndexError

        cur_item = self.head
        while index != 0:
            cur_item = cur_item.get_next()
            index -= 1

        cur_item.set_data(data)

    def __delitem__(self, index):
        if self.size <= index:
            raise IndexError

        if index == 0:
            if self.head.get_next() is None:
                self.head = Item()
            else:
                self.head = self.head.get_next()
        else:
            cur_item = self.head
            while index != 1:
                cur_item = cur_item.get_next()
                index -= 1

            cur_item.set_next(cur_item.get_next().get_next())

        self.size -= 1

    def find(self, value):
        cur_item = self.head

        for i in range(self.size):
            if cur_item.get_data() == value:
                return i

            cur_item = cur_item.get_next()

        raise ValueError

    def clear(self):
        self.head = Item()
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        self.cur = self.head
        return self

    def __next__(self):
        if self.cur is None or self.cur.get_data() is None:
            raise StopIteration

        result = self.cur.get_data()
        self.cur = self.cur.get_next()
        return result

    def __str__(self):
        elms = []
        cur_item = self.head

        for _ in range(self.size):
            elms.append(str(cur_item.get_data()))
            cur_item = cur_item.get_next()

        return '; '.join(elms)
