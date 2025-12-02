const input = await Deno.readTextFile("input.txt");
const ranges = input.split(",").map((range, i, _) => {
    return range.replace("\n", "").split("-").map((pos) =>
        Number.parseInt(pos)
    );
});

let result = 0;
for (const range of ranges) {
    const last = range[1];
    let curr = range[0];

    while (curr <= last) {
        const currStr = String(curr);

        if (currStr.length % 2 == 0) {
            const middle = currStr.length / 2;

            const a = currStr.slice(0, middle);
            const b = currStr.slice(middle);

            if (a == b) {
                result += curr;
                console.log(`silly number: ${curr}`);
            }
        }

        curr++;
    }
}

console.log(result);
