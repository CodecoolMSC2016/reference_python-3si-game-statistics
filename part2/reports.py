def get_most_played(file_name):
    table = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split('\t')
            table.append(parts)
    most_played_title = None
    max_units_sold = None
    for row in table:
        game_title = row[0]
        units_sold = float(row[1])
        if max_units_sold is None or max_units_sold < units_sold:
            max_units_sold = units_sold
            most_played_title = game_title
    return most_played_title
