def get_table(file_name):
    table = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
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
    table = get_table(file_name)
    sum_units_sold = 0
    for row in table:
        units_sold = float(row[1])
        sum_units_sold += units_sold
    return sum_units_sold


def get_selling_avg(file_name):
    return sum_sold(file_name) / len(get_table(file_name))
