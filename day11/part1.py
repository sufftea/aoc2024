class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def get_head(self):
        curr = self

        while curr.prev is not None:
            curr = curr.prev

        return curr

    def insert_after(self, value):
        new_node = Node(
            value=value,
            next=None,
            prev=None,
        )

        if self.next is not None:
            self.next.prev = new_node
        new_node.next = self.next
        new_node.prev = self
        self.next = new_node

    def to_list(self):
        curr = self
        l = []
        while curr is not None:
            l.append(curr.value)
            curr = curr.next

        return l


with open("input.txt") as f:
    stones = list(map(int, f.read().split(" ")))

    tail = Node(None, None, None)
    for stone in stones:
        tail.insert_after(stone)
        assert tail.next is not None
        tail = tail.next

    head = tail.get_head()
    head = head.next
    assert head is not None
    head.prev = None

    for i in range(0, 25):

        print(i)
        # print(head.to_list())

        curr = head
        while curr is not None:
            if curr.value == 0:
                curr.value = 1
                curr = curr.next
            elif len(str(curr.value)) % 2 == 0:
                s = str(curr.value)
                a = s[: len(s) // 2]
                b = s[len(s) // 2 :]

                curr.value = int(a)
                curr.insert_after(int(b))
                curr = curr.next
                assert curr is not None
                curr = curr.next
            else:
                curr.value *= 2024
                curr = curr.next

    print(len(head.to_list()))
