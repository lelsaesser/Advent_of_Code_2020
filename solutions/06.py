class Solution:

    def count_answers_part_1(self):
        f = open("../inputs/06_input.txt")
        unique_answers = set()
        result_sum = 0
        for line in f.readlines():
            if line == "\n":
                result_sum += len(unique_answers)
                unique_answers = set()

            else:
                [unique_answers.add(char) for char in line.replace("\n", "")]

        result_sum += len(unique_answers)
        return result_sum

    def _count_answers(self, group: str, group_lines: int):
        answer_count = dict()
        result_sum = 0
        for char in group:
            try:
                answer_count[char] += 1
            except KeyError:
                answer_count[char] = 1

        for key, value in answer_count.items():
            if value == group_lines:
                result_sum += 1

        return result_sum

    def count_answers_part_2(self):
        f = open("../inputs/06_input.txt")
        group = ""
        group_lines = 0
        result_sum = 0

        for line in f.readlines():
            if line == "\n":
                result_sum += self._count_answers(group, group_lines)
                group_lines = 0
                group = ""

            else:
                group_lines += 1
                group += line.replace("\n", "")

        result_sum += self._count_answers(group, group_lines)
        return result_sum


print(Solution().count_answers_part_1())
print(Solution().count_answers_part_2())
