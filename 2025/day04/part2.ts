import process from "node:process";
const input = await Deno.readTextFile("input.txt");
const map = input.split("\n").slice(0, -1).map((row) =>
    row.split("").map(function (cell): number {
        switch (cell) {
            case "@":
                return 1;
            default:
                return 0;
        }
    })
);

function checkNeis(map: number[][], x: number, y: number, epoch: number) {
    const neis = [
        [1, 1],
        [1, 0],
        [1, -1],
        [0, 1],
        [0, -1],
        [-1, 1],
        [-1, 0],
        [-1, -1],
    ];

    let neiRolls = 0;
    for (const [offX, offY] of neis) {
        const neiX = x + offX;
        const neiY = y + offY;

        if (
            neiY >= 0 && neiY < map.length &&
            neiX >= 0 && neiX < map[neiY].length
        ) {
            if (map[neiY][neiX] >= epoch) {
                neiRolls++;
            }
        }
    }

    return neiRolls;
}

function pprintMap(map: number[][]) {
    for (const row of map) {
        for (const cell of row) {
            process.stdout.write(String(cell));
        }
        process.stdout.write("\n");
    }
}

let epoch = 1;
let total = 0;
while (true) {
    let freeRolls = 0;

    for (let y = 0; y < map.length; y++) {
        for (let x = 0; x < map[y].length; x++) {
            if (map[y][x] == epoch) {
                const neis = checkNeis(map, x, y, epoch);

                if (neis < 4) {
                    // console.log(`free roll at ${x}; ${y}`);
                    freeRolls += 1;
                } else {
                    map[y][x] = epoch + 1;
                }
            }
        }
    }

    // pprintMap(map);
    console.log(freeRolls);
    total += freeRolls;
    epoch++;
    if (freeRolls == 0) {
        break;
    }
}


console.log(`total: ${total}`);
