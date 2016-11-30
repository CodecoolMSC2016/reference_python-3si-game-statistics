def round_up(number):
    return int(number + 1)


def sort_table_by_year_and_title(table):
    sorted_table = []
    while len(table) > 0:
        min_i = 0
        min_row = table[min_i]
        min_game_title = min_row[0]
        min_game_year = int(min_row[2])
        for i in range(1, len(table)):
            row = table[i]
            game_title = row[0]
            game_year = int(row[2])
            newer_game = game_year > min_game_year
            same_year = game_year == min_game_year
            # need lower() because uppercase letters are 'less than'
            # their lowercase counterparts: 'A' < 'a' == True
            earlier_title = game_title.lower() < min_game_title.lower()
            if newer_game or (same_year and earlier_title):
                min_i = i
                min_row = row
                min_game_title = game_title
                min_game_year = game_year
        sorted_table.append(min_row)
        del table[min_i]
    table.extend(sorted_table)


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


def get_date_ordered(file_name):
    table = get_table(file_name)
    sort_table_by_year_and_title(table)
    titles = []
    for row in table:
        game_title = row[0]
        titles.append(game_title)
    return titles
