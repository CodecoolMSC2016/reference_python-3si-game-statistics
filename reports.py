def get_table(file_name):
    table = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            parts = line.split('\t')
            table.append(parts)
    return table


def count_games(file_name):
    return len(get_table(file_name))

def decide(file_name, year):
    table = get_table(file_name)
    for row in table:
        game_year = int(row[2])
        if year == game_year:
            return True
    return False

def get_latest(file_name):
    max_title = None
    max_year = None
    table = get_table(file_name)
    for row in table:
        game_title = row[0]
        game_year = int(row[2])
        if max_year is None or max_year < game_year:
            max_title = game_title
            max_year = game_year
    return max_title
