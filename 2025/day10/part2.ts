const input = await Deno.readTextFile("input.txt");

type Machine = {
    joltages: number[];
    buttons: number[][];
};

const machines = input.trim().split("\n").map((machineStr) => {
    const data = machineStr.split(" ");
    const buttonsStr = data.slice(0, -1);
    let joltagesStr = data[-1];

    joltagesStr = joltagesStr.substring(1, joltagesStr.length - 1);

    // for (let i = 0; i < targetStr.length; i++) {
    //     if (targetStr[i] == "#") {
    //         target |= 1 << i;
    //     }
    // }

    const buttons: number[] = [];
    for (const buttonStr of buttonsStr) {
        const indicators = buttonStr.matchAll(/\d+/g).map((e) =>
            Number.parseInt(e[0])
        ).toArray();

        let button = 0;

        for (const indicator of indicators) {
            button |= 1 << indicator;
        }

        buttons.push(button);
    }

    return {
        target,
        buttons: buttons,
    };
});

function testButtonCount(
    state: number,
    buttons: number[],
    start: number,
): number[] | null {
    for (let i = start; i < buttons.length; i++) {
        const button = buttons[i];
        const newState = state ^ button;

        if (newState == 0) {
            return [i];
        }
    }

    let bestResultLength = Infinity;
    let bestResult: number[] | null = null;
    for (let i = start; i < buttons.length; i++) {
        const button = buttons[i];
        const newState = state ^ button;

        const result = testButtonCount(newState, buttons, i + 1);

        if (result === null) {
            continue;
        }
        if (result.length < bestResultLength) {
            bestResultLength = result.length;
            bestResult = [i, ...result];
        }
    }

    return bestResult;
}

let sum = 0;
for (const machine of machines) {
    // console.log(machine.buttons.map((e) => e.toString(2).padStart(8, "0")));

    const result = testButtonCount(machine.target, machine.buttons, 0);
    sum += result!.length;
    // console.log(result);
}

console.log(sum);
