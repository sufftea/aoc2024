function parse(input: string): [number[], string][] {
    const lines = input.trim().split("\n").map((line) =>
        line.trim().split(/ +/)
    );

    const problems: [number[], string][] = Array<[number[], string]>(
        lines[0].length,
    );
    for (let i = 0; i < lines[0].length; i++) {
        const column = lines.map((line) => line[i]);
        problems[i] = [
            column.slice(0, -1).map(Number),
            column[column.length - 1],
        ];
    }

    return problems;
}

const input = await Deno.readTextFile("input.txt");
const problems = parse(input);

let total = 0;
for (const problem of problems) {
    const [nums, op] = problem;

    console.log(problem);
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
