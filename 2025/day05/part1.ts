const input = await Deno.readTextFile("input.txt");

const [rangesStr, productsStr] = input.trim().split("\n\n");

const ranges = rangesStr.split("\n").map(function (line): [number, number] {
    return line.split("-").map(Number) as [number, number];
});

const products = productsStr.split("\n").map(Number);

// console.log(ranges);
// console.log(products);

let count = 0;
for (const product of products) {
    let valid = false;
    for (const range of ranges) {
        if (product >= range[0] && product <= range[1]) {
            valid = true;
        }
    }

    if (valid) {
        // console.log(`${product}: valid`);
        count++;
    }
}

console.log(count);
