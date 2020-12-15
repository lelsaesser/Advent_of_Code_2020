class Solution:

    def handheld_halting_part_1(self):
        f = open("../inputs/08_input.txt")
        lines = f.read().split("\n")
        acc = 0
        idx_history = set()
        start_idx = 0
        while True:
            for line_idx in range(start_idx, len(lines)):
                line = lines[line_idx]
                if line_idx in idx_history:
                    return acc
                else:
                    idx_history.add(line_idx)

                operation = line.split(" ")
                op = operation[0]
                value = operation[1]
                if op == "acc":
                    acc += int(value)
                elif op == "jmp":
                    start_idx = line_idx + int(value)
                    break

    def handheld_halting_part_1_alternative_approach(self):
        f = open("../inputs/08_input.txt")
        lines = f.read().split("\n")
        acc = 0
        idx_history = set()
        line_idx = 0
        while True:
            line = lines[line_idx]
            if line_idx in idx_history:
                return acc
            else:
                idx_history.add(line_idx)

            operation = line.split(" ")
            op = operation[0]
            value = operation[1]
            if op == "nop":
                line_idx += 1
            if op == "acc":
                acc += int(value)
                line_idx += 1
            elif op == "jmp":
                line_idx += int(value)

    def _test_bootcode(self, lines):
        acc = 0
        idx_history = set()
        line_idx = 0
        while True:
            line = lines[line_idx]
            if line_idx in idx_history:
                return 0
            else:
                idx_history.add(line_idx)

            operation = line.split(" ")
            op = operation[0]
            value = operation[1]
            if op == "nop":
                line_idx += 1
            if op == "acc":
                acc += int(value)
                line_idx += 1
            elif op == "jmp":
                line_idx += int(value)

            if line_idx == 642:
                return acc

    def handheld_halting_part_2(self):
        line_idx = 0
        while True:
            f = open("../inputs/08_input.txt")
            lines = f.read().split("\n")
            if "nop" in lines[line_idx]:
                lines[line_idx] = lines[line_idx].replace("nop", "jmp")
                res = self._test_bootcode(lines)
                if res:
                    return res

            elif "jmp" in lines[line_idx]:
                lines[line_idx] = lines[line_idx].replace("jmp", "nop")
                res = self._test_bootcode(lines)
                if res:
                    return res

            line_idx += 1


print(Solution().handheld_halting_part_1())
print(Solution().handheld_halting_part_1_alternative_approach())
print(Solution().handheld_halting_part_2())
