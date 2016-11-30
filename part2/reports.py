def round_up(number):
    return int(number + 1)


def get_table(file_name):
    table = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            parts = line.split('\t')
            table.append(parts)
    return table


def get_most_played(file_name):
    most_played_title = None
    max_units_sold = None
    table = get_table(file_name)
    for row in table:
        game_title = row[0]
        units_sold = float(row[1])
        if max_units_sold is None or max_units_sold < units_sold:
            max_units_sold = units_sold
            most_played_title = game_title
    return most_played_title


def sum_sold(file_name):
    sum_units_sold = 0
    table = get_table(file_name)
    for row in table:
        units_sold = float(row[1])
        sum_units_sold += units_sold
    return sum_units_sold


def get_selling_avg(file_name):
    table = get_table(file_name)
    table_length = len(table)
    if table_length == 0:
        return 0
    return sum_sold(file_name) / table_length


def count_longest_title(file_name):
    longest_title_length = None
    table = get_table(file_name)
    for row in table:
        game_title_length = len(row[0])
        if longest_title_length is None \
                or longest_title_length < game_title_length:
            longest_title_length = game_title_length
    return longest_title_length


def get_date_avg(file_name):
    table = get_table(file_name)
    table_length = len(table)
    if table_length == 0:
        return 0
    sum_year = 0
    for row in table:
        game_year = int(row[2])
        sum_year += game_year
    return round_up(sum_year / table_length)


def get_game(file_name, title):
    table = get_table(file_name)
    for row in table:
        game_title = row[0]
        if title == game_title:
            return [
                row[0],
                float(row[1]),
                int(row[2]),
                row[3],
                row[4],
            ]


def count_grouped_by_genre(file_name):
    genre_count = {}
    table = get_table(file_name)
    for row in table:
        game_genre = row[3]
        if game_genre in genre_count:
            genre_count[game_genre] += 1
        else:
            genre_count[game_genre] = 1
    return genre_count
