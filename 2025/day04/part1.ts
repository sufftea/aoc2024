const input = await Deno.readTextFile("input.txt");
const map = input.split("\n").slice(0, -1).map((row) => row.split(''));

function checkNeis(map: string[], x: number, y: number) {
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
            if (map[neiY][neiX] == "@") {
                neiRolls++;
            }
        }
    }

    return neiRolls;
}

let freeRolls = 0;
for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[y].length; x++) {
        if (map[y][x] == "@") {
            const neis = checkNeis(map, x, y);

            if (neis < 4) {
                // console.log(`free roll at ${x}; ${y}`);
                freeRolls += 1;
            }
        }
    }
}

console.log(freeRolls);
