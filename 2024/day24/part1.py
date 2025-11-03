from dataclasses import dataclass


@dataclass
class Node:
    value: str
    name: str
    children: "list[Node]" = []
    # a: "Node | None" = None
    # b: "Node | None" = None


with open("test1.txt") as f:

    inputs, gates = f.read().split("\n\n")

    name_to_node = {}

    for input in inputs.split("\n"):
        name, value = input.split(": ")
        n = Node(
            value=value,
            name=name,
        )

        name_to_node[name] = n

    for gate in gates.split("\n"):
        # ntg XOR fgs -> mjb

        expr, name = gate.split(" -> ")
        name_a, operation, name_b = expr.split(" ")

        if name in name_to_node:
            :

        # if name_a in name_to_node:

