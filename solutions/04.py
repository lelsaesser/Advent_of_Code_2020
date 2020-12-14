import re

class Solution:

    def count_valid_passports_part_1(self):
        f = open("../inputs/04_input.txt", "r")
        valid_count = 0
        fields_present = set()
        relevant_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

        for line in f.readlines():
            if line == "\n":
                if all(field_name in fields_present for field_name in relevant_fields):
                    valid_count += 1
                fields_present = set()
                continue

            for field in relevant_fields:
                if field in line:
                    fields_present.add(field)

        # check must be repeated here, since input does not end with newline, therefore not triggering evaluation
        # for last input line
        if all(field_name in fields_present for field_name in relevant_fields):
            valid_count += 1
        return valid_count

    def _input_validation(self, field_values: dict) -> bool:
        # additional input validation
        if not 1920 <= int(field_values.get("byr")) <= 2002: return False
        if not 2010 <= int(field_values.get("iyr")) <= 2020: return False
        if not 2020 <= int(field_values.get("eyr")) <= 2030: return False

        hgt = field_values.get("hgt")
        hgt_trim = hgt[:len(hgt) - 2]
        if "cm" in hgt:
            if not 150 <= int(hgt_trim) <= 193: return False
        elif "in" in hgt:
            if not 59 <= int(hgt_trim) <= 76: return False
        else:
            return False

        hcl = field_values.get("hcl")
        regex = re.compile(r'^#[0-9a-f]{6}$')
        if not regex.match(hcl): return False

        if field_values.get("ecl") not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}: return False

        regex = re.compile(r'^[0-9]{9}$')
        if not regex.match(field_values.get("pid")): return False

        return True

    def count_valid_passports_part_2(self):
        f = open("../inputs/04_input.txt", "r")
        valid_count = 0
        relevant_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        field_values = {}

        for line in f.readlines():
            if line == "\n":
                if all(field_name in field_values for field_name in relevant_fields):
                    if self._input_validation(field_values):
                        valid_count += 1

                field_values = {}
                continue

            line_split = line.split(" ")
            for part in line_split:
                for field in relevant_fields:
                    if field in part:
                        value = part.split(":")[1]
                        field_values[field] = value.replace("\n", "")

        if self._input_validation(field_values):
            valid_count += 1
        return valid_count


print(Solution().count_valid_passports_part_1())
print(Solution().count_valid_passports_part_2())
