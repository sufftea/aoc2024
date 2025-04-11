from collections import deque

import numpy as np


def check_cycles(adj, i):
    to_visit = deque()
    to_visit.append((i, 0))

    while True:
        curr, length = to_visit.popleft()

        if length == 3:
            # todo
            continue

        for i, edge in enumerate(adj[curr]):
            if edge == 1:
                to_visit.append((i, length + 1))


def find_cycles(adj, node_to_index):
    count = 0
    for node, i in node_to_index.items():
        if node[0] != "t":
            continue

        check_cycles(adj, i)


with open("test1.txt") as f:
    connections = []
    nodes = set()
    count = 0
    for connection in f:
        a, b = connection[:-1].split("-")
        nodes.add(a)
        nodes.add(b)

        connections.append((a, b))

    node_to_index = {node: i for i, node in enumerate(nodes)}
    index_to_node = {i: node for i, node in enumerate(nodes)}

    nof_nodes = len(nodes)

    adj = np.zeros((nof_nodes, nof_nodes), int)

    for a, b in connections:
        a_id = node_to_index[a]
        b_id = node_to_index[b]

        adj[a_id, b_id] = 1
