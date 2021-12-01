def parse_file(file, tijpe):
    lines = []
    with open(file, 'r') as f:
        for line in f.read().splitlines():
            if tijpe == 'int':
                lines.append(int(line))
            else:
                raise ValueError("Too bad :)")
    return lines



