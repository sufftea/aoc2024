function parse(input: string): [number[], string][] {
    const lines = input.trim().split("\n");

    const problems: [number[], string][] = [];

    const width = lines[0].length;
    const height = lines.length;

    for (let i = 0; i < width; i++) {
        const op = lines[height - 1][i];

        const nums: number[] = [];

        while (true) {
            const numStr = lines.map((line) => line[i]).slice(0, -1).join("");

            if (numStr.match(/\d/)) {
                nums.push(
                    Number(numStr),
                );
                i++;
            } else {
                break;
            }
        }

        // console.log([nums, op]);
        problems.push([nums, op]);
    }

    return problems;
}

const input = await Deno.readTextFile("input.txt");
// console.log(input);
const problems = parse(input);

let total = 0;
for (const problem of problems) {
    const [nums, op] = problem;

    // console.log(problem);
    switch (op) {
        case "+": {
            total += nums.reduce(
                (previous, current, _, __) => previous + current,
                0,
            );
            break;
        }

        case "*": {
            total += nums.reduce(
                (previous, current, _, __) => previous * current,
                1,
            );
            break;
        }
    }
}

console.log(total);
