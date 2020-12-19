class Solution:
    f = open("../inputs/10_input.txt")
    lines = f.read().split("\n")
    lines = sorted([int(x) for x in lines])

    def adapter_array_part_1(self) -> int:
        three_diff_count = 1
        one_diff_count = 1

        for i in range(len(self.lines) - 1):
            if self.lines[i+1] - self.lines[i] == 1:
                one_diff_count += 1
            elif self.lines[i+1] - self.lines[i] == 3:
                three_diff_count += 1

        return one_diff_count * three_diff_count

    def adapter_array_part_2(self) -> int:
        self.lines.insert(0, 0)
        self.lines.append(self.lines[-1] + 3)
        paths = [0] * (max(self.lines) + 1)
        paths[0] = 1

        for i in range(1, max(self.lines) + 1):
            for x in range(1, 4):
                if i - x in self.lines:
                    paths[i] += paths[i - x]

        return paths[-1]


print(Solution().adapter_array_part_1())
print(Solution().adapter_array_part_2())
