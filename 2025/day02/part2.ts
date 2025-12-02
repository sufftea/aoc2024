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

        let sillyFlag = false;

        patternLengths: for (
            let patternLength = 1;
            patternLength <= currStr.length / 2;
            patternLength++
        ) {
            let prevSlice: string | null = null;
            for (let i = 0; i < currStr.length; i += patternLength) {
                const slice = currStr.slice(i, i + patternLength);
                if (prevSlice !== null && slice != prevSlice) {
                    continue patternLengths; // todo
                }
                prevSlice = slice;
            }

            console.log(`invalid id: ${curr}`);
            // id is incorrect
            result += curr;
            break;
        }

        curr++;
    }
}

console.log(result);
