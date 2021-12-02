from src.input_parser import parse_file


def run():
    values = parse_file('../inputs/day02.txt', '(str, int)')
    position = 0
    depth = 0
    aim = 0

    for value in values:
        if value[0] == 'forward':
            position = position + value[1]
            depth = depth + (aim * value[1])
        elif value[0] == 'down':
            aim = aim + value[1]
        elif value[0] == 'up':
            aim = aim - value[1]
        else:
            raise ValueError("Something went wrong")

    result = depth * position
    return result


if __name__ == '__main__':
    print(run())
