def get_table(file_name):
    table = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            parts = line.split('\t')
            table.append(parts)
    return table


def count_games(file_name):
    return len(get_table(file_name))
