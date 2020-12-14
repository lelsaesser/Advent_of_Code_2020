class Solution:

    def find_seat_part_1(self):
        f = open("../inputs/05_input.txt", "r")
        seat_ids = []
        for line in f.readlines():
            row_col = []  # idx 0 = row, 1 = col
            curr_range = [0, 127]
            for char in line:
                if char == "F" or char == "L":
                    if abs(curr_range[0] - curr_range[1]) == 1:
                        row_col.append(curr_range[0])
                        curr_range = [0, 7]
                        continue
                    s = sum(curr_range) // 2
                    curr_range[1] = s

                elif char == "B" or char == "R":
                    if abs(curr_range[0] - curr_range[1]) == 1:
                        row_col.append(curr_range[1])
                        curr_range = [0, 7]
                        continue
                    s = sum(curr_range) // 2 + 1
                    curr_range[0] = s

            seat_ids.append(row_col[0] * 8 + row_col[1])

        return max(seat_ids), seat_ids

    def find_seat_part_2(self):
        seat_ids = self.find_seat_part_1()[1]
        sorted_seat_ids = sorted(seat_ids)
        for i in range(1, len(sorted_seat_ids)):
            if abs(sorted_seat_ids[i-1] - sorted_seat_ids[i]) == 2:
                return sorted_seat_ids[i] - 1


print(Solution().find_seat_part_1()[0])
print(Solution().find_seat_part_2())
