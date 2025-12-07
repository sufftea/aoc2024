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

let beams = new Set<number>();
beams.add(startX);

let splits = 0;
for (const line of map.slice(startY)) {
    // const beamsEntries = beams.entries();
    const newBeams = new Set<number>();
    for (const beam of beams) {
        if (line[beam] == "^") {
            splits++;
            if (beam - 1 >= 0) {
                newBeams.add(beam - 1);
            }
            if (beam + 1 < line.length) {
                newBeams.add(beam + 1);
            }
        } else {
            newBeams.add(beam);
        }
    }

    beams = newBeams;
}

console.log(splits);
