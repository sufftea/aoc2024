const input = await Deno.readTextFile("input.txt");

const positions = input.trim().split("\n").map((positionStr, i) => {
    return positionStr.trim().split(",").map(Number) as [
        number,
        number,
        number,
    ];
});

type Edge = {
    aIndex: number;
    bIndex: number;
    distance: number;
};

const edges: Edge[] = [];

for (let i = 0; i < positions.length; i++) {
    for (let j = i + 1; j < positions.length; j++) {
        const a = positions[i];
        const b = positions[j];

        edges.push({
            aIndex: i,
            bIndex: j,
            distance: Math.sqrt(
                Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2) +
                    Math.pow(a[2] - b[2], 2),
            ),
        });
    }
}

const sortedEdges = edges.sort((a, b) => a.distance - b.distance);

type Node = {
    pos: [number, number, number];
    parent: Node | null;
    // only meaningful in roots
    size: number;
};

function getRoot(node: Node) {
    let curr = node;
    while (curr.parent !== null) {
        curr = curr.parent;
    }
    return curr;
}

const nodes = positions.map<Node>((e) => {
    return {
        pos: e,
        parent: null,
        size: 1,
    };
});

let lastConnectedEdge: Edge | null = null;
for (const edge of sortedEdges) {
    // const edge = sortedEdges[i];

    const rootA = getRoot(nodes[edge.aIndex]);
    const rootB = getRoot(nodes[edge.bIndex]);

    if (
        rootA === rootB
    ) {
        continue;
    }

    rootA.parent = nodes[edge.bIndex];
    rootB.size += rootA.size;

    lastConnectedEdge = edge;
}

console.log(JSON.stringify(lastConnectedEdge));

const a = nodes[lastConnectedEdge!.aIndex].pos[0];
const b = nodes[lastConnectedEdge!.bIndex].pos[0];
const result = a * b;
console.log(result);
