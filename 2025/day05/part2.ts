const input = await Deno.readTextFile("input.txt");

const [rangesStr, productsStr] = input.trim().split("\n\n");

const rs = rangesStr.split("\n").map(function (line): [number, number] {
    return line.split("-").map(Number) as [number, number];
}).sort((a, b) => a[0] - b[0]);

const visitedRanges = new Set<number>();
let total = 0;

for (let i = 0; i < rs.length; i++) {
    if (visitedRanges.has(i)) {
        continue;
    }
    const currRange = rs[i];
    for (let j = i + 1; j < rs.length; j++) {
        if (
            rs[j][0] >= currRange[0] && rs[j][0] <= currRange[1]
        ) {
            currRange[1] = Math.max(currRange[1], rs[j][1]);
            visitedRanges.add(j);
        }

        if (
            rs[j][1] <= currRange[1] && rs[j][1] >= currRange[0]
        ) {
            currRange[0] = Math.min(currRange[0], rs[j][0]);
            visitedRanges.add(j);
        }
    }

    console.log(currRange);
    total += currRange[1] - currRange[0] + 1;
}

console.log(total);
