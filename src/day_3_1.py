from src.input_parser import parse_file


def binary(bin_arr):
    bin_int = "".join(map(str, bin_arr))
    return int(bin_int, 2)


def run():
    values = parse_file('../inputs/day03.txt', 'bin')
    gamma = []
    epsilon = []

    for i in range(len(values[0])):
        ones = 0
        for value in values:
            if value[i] == '1':
                ones += 1
        if ones > (len(values) / 2):
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)

    gamma_rate = binary(gamma)
    epsilon_rate = binary(epsilon)

    return gamma_rate * epsilon_rate


if __name__ == '__main__':
    print(run())
