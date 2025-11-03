import re


with open('input.txt') as f:
    input = f.read()
    
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")

    enabled = True
    result = 0;

    for expr in re.findall(pattern, input):
        
        if re.match(r'do\(\)', expr):
            enabled = True
        elif re.match(r"don't\(\)", expr):
            enabled = False
        elif enabled and re.match(r'mul\(\d+,\d+\)', expr):
            [a, b] = list(map(int, re.findall(r'\d+', expr)))

            result += a * b

    print(result)

