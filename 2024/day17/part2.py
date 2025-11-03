import re
from dataclasses import dataclass
from typing import Optional

dp = {}


@dataclass
class Computer:
    reg_a: int
    reg_b: int
    reg_c: int
    program: list[int]
    pointer: int = 0

    def get_combo_value(self, combo) -> int:
        match combo:
            case 0 | 1 | 2 | 3:
                return combo
            case 4:
                return self.reg_a
            case 5:
                return self.reg_b
            case 6:
                return self.reg_c
            case _:
                assert False

    def adv(self, operand):
        denum = self.get_combo_value(operand)
        numer = self.reg_a
        self.reg_a = numer >> denum
        self.pointer += 2

    def bxl(self, operand):
        self.reg_b = self.reg_b ^ operand
        self.pointer += 2

    def bst(self, operand):
        operand = self.get_combo_value(operand)
        self.reg_b = operand % 8
        self.pointer += 2

    def jnz(self, operand):
        if self.reg_a == 0:
            self.pointer += 2
            return
        self.pointer = operand

    def bxc(self, _):
        self.reg_b = self.reg_b ^ self.reg_c
        self.pointer += 2

    def out(self, operand, output):
        operand = self.get_combo_value(operand)
        output.append(operand % 8)
        self.pointer += 2

    def bdv(self, operand):
        denum = self.get_combo_value(operand)
        numer = self.reg_a
        # self.reg_b = int(float(numer) // (2**denum))
        self.reg_b = numer >> denum
        self.pointer += 2

    def cdv(self, operand):
        denum = self.get_combo_value(operand)
        numer = self.reg_a
        self.reg_c = numer >> denum
        self.pointer += 2

    def run_step(self) -> Optional[int]:
        if self.pointer + 1 > len(self.program):
            return None

        operation = program[self.pointer]
        operand = program[self.pointer + 1]

        match operation:
            case 0:
                self.adv(operand)
            case 1:
                self.bxl(operand)
            case 2:
                self.bst(operand)
            case 3:
                self.jnz(operand)
            case 4:
                self.bxc(operand)
            case 5:
                self.out(operand, output)
            case 6:
                self.bdv(operand)
            case 7:
                self.cdv(operand)

    def run_program(self, expected_output):
        output = []

        while True:
            if self.pointer + 1 > len(self.program):
                break

            state = (
                self.reg_a,
                self.reg_b,
                self.reg_c,
                self.pointer,
            )
            result_len = dp.get(state, None)
            if result_len is not None and len(output) + result_len != len(
                expected_output
            ):
                print(f"cache hit for len={result_len}")
                return None

            operation = program[self.pointer]
            operand = program[self.pointer + 1]

            match operation:
                case 0:
                    self.adv(operand)
                case 1:
                    self.bxl(operand)
                case 2:
                    self.bst(operand)
                case 3:
                    self.jnz(operand)
                case 4:
                    self.bxc(operand)
                case 5:
                    self.out(operand, output)
                case 6:
                    self.bdv(operand)
                case 7:
                    self.cdv(operand)

        return output


with open("input.txt") as f:
    (reg_a,) = re.findall(r"(\d+)", f.readline())
    reg_a = int(reg_a)

    (reg_b,) = re.findall(r"(\d+)", f.readline())
    reg_b = int(reg_b)

    (reg_c,) = re.findall(r"(\d+)", f.readline())
    reg_c = int(reg_c)

    print(reg_a, reg_b, reg_c)

    f.readline()

    program = re.findall(r"(\d)", f.readline())
    program = list(map(int, program))
    print(program)

    i = 0
    best_match = []
    while True:
        computer = Computer(
            reg_a=i,
            reg_b=reg_b,
            reg_c=reg_c,
            program=program,
        )

        initial_state = (
            computer.reg_a,
            computer.reg_b,
            computer.reg_c,
            computer.pointer,
        )
        output = computer.run_program(program)

        if output is not None:
            if output == program[-len(output) :]:
                dp[initial_state] = len(output)

            if len(output) > len(best_match):
                best_match = output
                print(f"new best match at i={i}\t: {best_match}")

            if output == program:
                print(f"reg_a value: {i}")
                # print(f"output: {output}")
                print(computer)
                break

        i += 1

    # print(",".join(map(str, output)))
