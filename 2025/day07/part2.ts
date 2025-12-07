function parse(input: string): string[] {
    return input.trim().split("\n");
}

const input = await Deno.readTextFile("input.txt");
const map = parse(input);
console.log(map);

let [startX, startY] = [0, 0];
for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[y].length; x++) {
        if (map[y][x] === "S") {
            [startX, startY] = [x, y];
        }
    }
}

const beamCounts = new Array<number>(map[0].length).fill(0);
beamCounts[startX] = 1;
console.log(beamCounts);

for (const line of map.slice(startY)) {
    for (const [beam, count] of beamCounts.entries()) {
        if (line[beam] == "^") {
            if (beam - 1 >= 0) {
                beamCounts[beam - 1] += count;
            }
            if (beam + 1 < line.length) {
                beamCounts[beam + 1] += count;
            }
            beamCounts[beam] = 0;
        }
    }

    console.log(beamCounts.map((e) => e.toString().padStart(3, "0")).join(","));
}

const total = beamCounts.reduce((prev, curr) => prev + curr, 0);
console.log(total);
