def get_table(file_name):
    table = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            parts = line.split('\t')
            table.append(parts)
    return table


def sort_strings(strings):
    sorted_strings = []
    while len(strings) > 0:
        min_i = 0
        for i in range(1, len(strings)):
            # need lower() because uppercase letters are 'less than'
            # their lowercase counterparts: 'A' < 'a' == True
            if strings[i].lower() < strings[min_i].lower():
                min_i = i
        sorted_strings.append(strings[min_i])
        del strings[min_i]
    strings.extend(sorted_strings)


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


def count_by_genre(file_name, genre):
    count = 0
    table = get_table(file_name)
    for row in table:
        game_genre = row[3]
        if genre == game_genre:
            count += 1
    return count


def get_line_number_by_title(file_name, title):
    table = get_table(file_name)
    for i in range(len(table)):
        row = table[i]
        game_title = row[0]
        if title == game_title:
            return i + 1
    raise ValueError()


def sort_abc(file_name):
    table = get_table(file_name)
    titles = []
    for row in table:
        game_title = row[0]
        titles.append(game_title)
    sort_strings(titles)
    return titles


def get_genres(file_name):
    table = get_table(file_name)
    genres = []
    for row in table:
        game_genre = row[3]
        if game_genre not in genres:
            genres.append(game_genre)
    sort_strings(genres)
    return genres


def when_was_top_sold_fps(file_name):
    table = get_table(file_name)
    max_units_sold = None
    max_year = None
    for row in table:
        game_genre = row[3]
        if game_genre != 'First-person shooter':
            continue
        units_sold = float(row[1])
        game_year = int(row[2])
        if max_units_sold is None or max_units_sold < units_sold:
            max_units_sold = units_sold
            max_year = game_year
    if max_year is None:
        raise ValueError()
    return max_year
