const input = await Deno.readTextFile("input.txt");
const batteries = input.split("\n").slice(0, -1);

let result = 0;

for (const bank of batteries) {
    const digits = bank.split("").map((value, _, __) => Number.parseInt(value));

    let searchStart = 0;
    for (let digitRank = 11; digitRank >= 0; digitRank--) {
        let highestIndex = searchStart;
        for (let i = searchStart; i < digits.length - digitRank; i++) {
            if (digits[highestIndex] < digits[i]) {
                highestIndex = i;
            }
        }


        searchStart = highestIndex + 1;
        result += digits[highestIndex] * Math.pow(10, digitRank);
    }
}

console.log(result);
