import process from "node:process";
const input = await Deno.readTextFile("input.txt");

type Point = {
    x: number;
    y: number;
};

const positions = input.trim().split("\n").map((e) => {
    const [x, y] = e.trim().split(",").map(Number);
    return { x: x, y: y };
});

let maxArea = 0;

function isInside(
    point: Point,
    positions: Point[],
): boolean {
    // let hc = 0;
    // let vc = 0;

    // let rc = 0;
    // let lc = 0;
    // let uc = 0;
    // let dc = 0;

    let count = 0;
    for (let i = 0; i < positions.length; i++) {
        const la = positions[i];
        const lb = positions[i + 1 < positions.length ? i + 1 : 0];

        if (
            (la.x < lb.x && point.y == la.y && point.x >= la.x &&
                point.x <= lb.x) ||
            (la.x > lb.x && point.y == la.y && point.x >= lb.x &&
                point.x <= la.x) ||
            (la.y < lb.y && point.x == la.x && point.y >= la.y &&
                point.y <= lb.y) ||
            (la.y > lb.y && point.x == la.x && point.y >= lb.y &&
                point.y <= la.y)
        ) {
            return true;
        }

        if (
            (la.y < lb.y && point.y > la.y && point.y <= lb.y) ||
            (la.y > lb.y && point.y > lb.y && point.y <= la.y)
        ) {
            if (point.x >= la.x) {
                // lc++;
                count++;
            }
        }
    }

    return count % 2 !== 0;
}

// for (let y = 0; y < 25; y++) {
//     for (let x = 0; x < 25; x++) {
//         process.stdout.write(isInside({ x, y }, positions) ? "#" : ".");
//     }
//     process.stdout.write("\n");
// }

// for (let y = 0; y < 100; y++) {
//     for (let x = 0; x < 100; x++) {
//         process.stdout.write(
//             isInside([x * 1000, y * 1000], positions) ? "#" : ".",
//         );
//     }
//     process.stdout.write("\n");
// }

function verifyBox(
    up: number,
    down: number,
    left: number,
    right: number,
    positions: Point[],
) {
    // Check all the red tiles within the bounding box
    for (let i = 0; i < positions.length; i++) {
        const tile = positions[i];

        if (
            tile.x >= left && tile.x <= right && tile.y >= down &&
            tile.y <= up
        ) {
            const neis = [
                { x: tile.x - 1, y: tile.y - 1 },
                { x: tile.x + 1, y: tile.y - 1 },
                { x: tile.x - 1, y: tile.y + 1 },
                { x: tile.x + 1, y: tile.y + 1 },

                { x: tile.x, y: tile.y - 1 },
                { x: tile.x, y: tile.y - 1 },
                { x: tile.x - 1, y: tile.y },
                { x: tile.x + 1, y: tile.y },
            ];

            for (const nei of neis) {
                if (
                    nei.x >= left && nei.x <= right && nei.y >= down &&
                    nei.y <= up
                ) {
                    if (!isInside(nei, positions)) {
                        return false;
                    }
                }
            }
        } else {
            if (
                tile.x < left || tile.x > right && tile.y > down && tile.y < up
            ) {
                const neis = [
                    { x: left, y: tile.y + 1 },
                    { x: left, y: tile.y - 1 },
                    { x: right, y: tile.y + 1 },
                    { x: right, y: tile.y - 1 },
                ];

                for (const nei of neis) {
                    if (
                        nei.x >= left && nei.x <= right && nei.y >= down &&
                        nei.y <= up
                    ) {
                        if (!isInside(nei, positions)) {
                            return false;
                        }
                    }
                }
            } else if (
                tile.y < down || tile.y > up && tile.x > left && tile.x < right
            ) {
                const neis = [
                    { x: tile.x + 1, y: up },
                    { x: tile.x - 1, y: up },
                    { x: tile.x + 1, y: down },
                    { x: tile.x - 1, y: down },
                ];

                for (const nei of neis) {
                    if (
                        nei.x >= left && nei.x <= right && nei.y >= down &&
                        nei.y <= up
                    ) {
                        if (!isInside(nei, positions)) {
                            return false;
                        }
                    }
                }
            }
        }
    }

    return true;
}

/*

...............
  #XXXXXXXXXXXXXXXXXXXXXXXXXX#
  #XXXXXXXXXXXXXXXXXXXXXX#XXXX
                         XXXXX
                         XXXXX
                         XXXXX
                         XXXXX
                         XXXXX
             ?           XXXXX
                         XXXXX
                         XXXXX
                         XXXXX
                         XXXXX
                         XXXXX
                         #XXX#


*/

for (let i = 0; i < positions.length; i++) {
    const a = positions[i];

    console.log(`${i} / ${positions.length}`);
    for (let j = i + 1; j < positions.length; j++) {
        const b = positions[j];

        const up = Math.max(a.y, b.y);
        const down = Math.min(a.y, b.y);
        const left = Math.min(a.x, b.x);
        const right = Math.max(a.x, b.x);

        const area = (Math.abs(a.x - b.x) + 1) *
            (Math.abs(a.y - b.y) + 1);
        // console.log(`${a} -- ${b}; area: ${area}`);

        if (
            verifyBox(up, down, left, right, positions)
        ) {
            maxArea = Math.max(maxArea, area);
            // console.log(maxArea);
        } else {
            // console.log("skipping");
        }
    }
}

console.log(maxArea);

// 4629483216 -- too high
