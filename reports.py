def get_table(file_name):
    table = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            parts = line.split('\t')
            table.append(parts)
    return table


def sort_strings(strings):
    sorted_strings = []
    while len(strings) > 0:
        min_i = None
        for i in range(len(strings)):
            # need lower() because uppercase letters are 'less than'
            # their lowercase counterparts: 'A' < 'a' == True
            if min_i is None or strings[i].lower() < strings[min_i].lower():
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
    line_number = None
    table = get_table(file_name)
    for i in range(len(table)):
        row = table[i]
        game_title = row[0]
        if title == game_title:
            line_number = i + 1
    if line_number is None:
        raise ValueError()
    return line_number


def sort_abc(file_name):
    table = get_table(file_name)
    titles = []
    for row in table:
        game_title = row[0]
        titles.append(game_title)
    sort_strings(titles)
    return titles
