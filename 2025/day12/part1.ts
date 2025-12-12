const input = Deno.readTextFileSync("input.txt");

const data = input.trim().split("\n").map((e) => {
    const [sizeStr, amountsStr] = e.split(":");

    const size = sizeStr.split("x").map<number>(Number);
    const amounts = amountsStr.trim().split(" ").map(Number);

    return {
        size: size as [number, number],
        amounts: amounts,
    };
});

let canFit = 0;
for (const line of data) {
    const totalArea = line.size[0] * line.size[1];
    const dumbRequiredArea = line.amounts.reduce(
        (total, curr) => total + curr * 9,
        0,
    );

    const bestRequiredArea = line.amounts[0] * 7 +
        line.amounts[1] * 7 +
        line.amounts[2] * 7 +
        line.amounts[3] * 5 +
        line.amounts[4] * 7 +
        line.amounts[5] * 6;

    if (dumbRequiredArea <= totalArea) {
        canFit++;
    } else if (bestRequiredArea > totalArea) {
        console.log("definitelly impossible");
    } else {
        console.log("unfortunate 3rd option");
    }
}

console.log(canFit);
