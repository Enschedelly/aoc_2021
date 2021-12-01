from src.input_parser import parse_file


def run():
    values = parse_file('../inputs/day01.txt', 'int')
    count = 0
    for i in range(len(values) - 1):
        if values[i+1] > values[i]:
            count += 1

    return count


if __name__ == '__main__':
    print(run())
