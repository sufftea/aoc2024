const input = await Deno.readTextFile("input.txt");
const batteries = input.split("\n");

let result = 0;

for (const bank of batteries) {
    let digits = bank.split("").map((value, _, __) => Number.parseInt(value));

    let highestFirst = 0;
    let firstIndex = 0;
    for (let i = 0; i < digits.length - 1; i++) {
        if (digits[i] > highestFirst) {
            highestFirst = digits[i];
            firstIndex = i;
        }
    }

    let highestSecond = 0;
    for (let i = firstIndex + 1; i < digits.length; i++) {
        if (digits[i] > highestSecond) {
            highestSecond = digits[i];
        }
    }

    const curr = 10 * highestFirst + highestSecond;
    result += curr;
}

console.log(result);
