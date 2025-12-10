const input = await Deno.readTextFile("input.txt");

const positions = input.trim().split("\n").map((e) =>
    e.trim().split(",").map(Number)
);

console.log(positions);

let maxArea = 0;

for (let i = 0; i < positions.length; i++) {
    const a = positions[i];
    for (let j = 0; j < positions.length; j++) {
        const b = positions[j];

        const area = (Math.abs(a[0] - b[0]) + 1) * (Math.abs(a[1] - b[1]) + 1);

        maxArea = Math.max(maxArea, area);
    }
}

console.log(maxArea);
