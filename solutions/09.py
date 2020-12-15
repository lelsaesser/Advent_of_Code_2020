class Solution:

    def encoding_error_part_1(self):
        f = open("../inputs/09_input.txt")
        lines = f.read().split("\n")
        curr_idx = 25
        while True:
            valid = False
            value = int(lines[curr_idx])
            scope = lines[curr_idx-25:curr_idx]
            for n in scope:
                if int(n) >= value:
                    continue
                for n2 in scope:
                    if int(n2) >= value:
                        continue
                    if int(n) != int(n2):
                        if int(n) + int(n2) == value:
                            valid = True
                            break
                if valid:
                    break

            if not valid:
                return value
            curr_idx += 1

    def encoding_error_part_2(self):
        f = open("../inputs/09_input.txt")
        lines = f.read().split("\n")
        lines = [int(x) for x in lines]
        s = 1504371145
        while True:
            series = [lines[0]]
            curr_sum = lines[0]
            for i in range(1, len(lines)):
                if lines[0] != lines[i]:
                    series.append(lines[i])
                    curr_sum += lines[i]
                    if curr_sum > s:
                        break
                    if curr_sum == s:
                        return min(series) + max(series)

            del lines[0]


print(Solution().encoding_error_part_1())
print(Solution().encoding_error_part_2())
