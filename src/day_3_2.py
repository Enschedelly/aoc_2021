from src.input_parser import parse_file


def binary(bin_arr):
    bin_int = "".join(map(str, bin_arr))
    return int(bin_int, 2)


def count_ones(values, i):
    ones = 0
    for value in values:
        if value[i] == '1':
            ones += 1
    return ones


def bit_criteria(values, rating_type):
    while len(values) > 1:
        for i in range(len(values[0])):
            ones = count_ones(values, i)

            if rating_type == 'oxygen':
                if ones >= (len(values) / 2):
                    values = [x for x in values if x[i] == "1"]
                else:
                    values = [x for x in values if x[i] == "0"]

                if len(values) == 1:
                    return values[0]

            elif rating_type == 'co2':
                if ones >= (len(values) / 2):
                    values = [x for x in values if x[i] == "0"]
                else:
                    values = [x for x in values if x[i] == "1"]

                if len(values) == 1:
                    return values[0]

            else:
                raise ValueError("Incorrect rating type.")


def run():
    values = parse_file('../inputs/day03.txt', 'bin')

    oxygen = bit_criteria(values, "oxygen")
    co2 = bit_criteria(values, "co2")

    return binary(oxygen) * binary(co2)


if __name__ == '__main__':
    print(run())
