from src.input_parser import parse_file


def run():
    values = parse_file('../inputs/day01.txt', 'int')
    count = 0
    for i in range(len(values) - 3):
        a = values[i] + values[i + 1] + values[i + 2]
        b = values[i + 1] + values[i + 2] + values[i + 3]
        if b > a:
            count += 1

    return count


if __name__ == '__main__':
    print(run())