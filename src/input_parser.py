def parse_file(file, tijpe):
    lines = []
    with open(file, 'r') as f:
        for line in f.read().splitlines():
            if tijpe == 'int':
                lines.append(int(line))
            elif tijpe == '(str, int)':
                (s, i) = line.split()
                lines.append([s, int(i)])
            elif tijpe == 'bin':
                lines.append(line)
            else:
                raise ValueError("Too bad :)")
    return lines



