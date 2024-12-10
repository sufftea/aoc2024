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


class DiskRegion:
    def __init__(self, id, size):
        self.id = id
        self.size = size


def list_disk_regions(head):
    result = []
    while head is not None:
        result += [head.value.id] * head.value.size
        head = head.next

    return result


def reduce_file_map(tail):
    head = tail.get_head()

    while tail != None:
        if tail.value.id == None:
            tail = tail.prev
            continue

        free_candidate = head
        while free_candidate != tail:
            if (
                free_candidate.value.id is None
                and free_candidate.value.size >= tail.value.size
            ):
                size_diff = free_candidate.value.size - tail.value.size
                if size_diff != 0:
                    new_free_space = DiskRegion(id=None, size=size_diff)
                    free_candidate.insert_after(new_free_space)

                free_candidate.value.id = tail.value.id
                free_candidate.value.size = tail.value.size

                tail.value.id = None

                break

            free_candidate = free_candidate.next

        tail = tail.prev

    return head


with open("input.txt") as f:
    input = f.read()
    input = list(map(int, input[:-1]))
    if len(input) % 2 != 0:
        input += [0]

    map_tail = None
    for i in range(0, len(input), 2):
        if map_tail is None:
            map_tail = Node(
                DiskRegion(
                    id=i // 2,
                    size=input[i],
                ),
                prev=map_tail,
                next=None,
            )
        else:
            map_tail.insert_after(DiskRegion(id=i // 2, size=input[i]))
            map_tail = map_tail.next

        assert map_tail is not None
        map_tail.insert_after(
            DiskRegion(
                id=None,
                size=input[i + 1],
            )
        )
        map_tail = map_tail.next

    assert map_tail is not None
    reduced_map = reduce_file_map(map_tail)
    reduced_disk = list_disk_regions(reduced_map)

    # print("".join(str(reduced_disk)))

    result = 0
    for i, file in enumerate(reduced_disk):
        if file is None:
            continue
        result += i * file
    print(result)
