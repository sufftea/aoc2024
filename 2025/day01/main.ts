import { mod } from "../utils/mod.ts";

const input = await Deno.readTextFile("input.txt");
const rotations = input.split("\n");

let times_at_zero = 0;
let position = 50;

for (const line of rotations) {
    // parse line

    const match = line.match(/(L|R)(\d*)/);
    if (match === null) break;

    const [, dir, countStr] = match as [
        string,
        "L" | "R",
        string,
    ];
    const count = Number(countStr);
    // console.log(`${dir} - ${count}`);

    switch (dir) {
        case "L":
            if (position == 0) {
                times_at_zero--;
            }

            position = position - count;
            if (position < 0) {
                times_at_zero += Math.ceil(Math.abs(position) / 100);
            }

            position = mod(position, 100);
            if (position == 0) {
                times_at_zero++;
            }
            break;
        case "R":
            position = position + count;
            times_at_zero += Math.floor(position / 100);

            position = mod(position, 100);
            break;
    }
}

console.log(times_at_zero);
