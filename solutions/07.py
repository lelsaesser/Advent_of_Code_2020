class Solution:

    def find_bag_colors_part_1(self):
        target_colors = ["shiny gold"]
        found_colors = []
        unique_colors = set()

        while True:
            f = open("../inputs/07_input.txt", "r")
            for line in f.readlines():
                for color in target_colors:
                    if color in line:
                        line_token = line.split(" ")
                        found_color = str(line_token[0] + " " + line_token[1])
                        if found_color != color:
                            found_colors.append(found_color)
                            unique_colors.add(found_color)

            target_colors = found_colors
            found_colors = []

            if not target_colors:
                break

        return len(unique_colors)

    def find_bag_size_part_2(self):
        target_colors = [("shiny gold", 1)]  # color name and bag multiplier
        found_colors = []
        total_bag_count = 0

        while True:
            for color in target_colors:
                f = open("../inputs/07_input.txt", "r")
                for line in f.readlines():
                    line_token = line.split(" ")
                    found_color = str(line_token[0] + " " + line_token[1])
                    if color[0] == found_color:
                        for token_idx in range(4, len(line_token), 4):  # skip both color tokens (e.g. "shiny", "gold") and "bags,"
                            try:
                                mult = int(line_token[token_idx]) * color[1]
                                found_color = line_token[token_idx + 1] + " " + line_token[token_idx + 2]
                                found_colors.append((found_color, mult))
                                total_bag_count += mult
                            except ValueError:
                                continue
                        break

            target_colors = found_colors
            found_colors = []

            if not target_colors:
                break

        return total_bag_count


print(Solution().find_bag_colors_part_1())
print(Solution().find_bag_size_part_2())
