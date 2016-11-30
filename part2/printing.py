import reports


def get_most_played(input_file):
    res = reports.get_most_played(input_file)
    print('What is the title of the most played game?', res, '\n')


def sum_sold(input_file):
    res = reports.sum_sold(input_file)
    print('How many copies have been sold total?', res, '\n')


def get_selling_avg(input_file):
    res = reports.get_selling_avg(input_file)
    print('What is the average selling?', res, '\n')


def count_longest_title(input_file):
    res = reports.count_longest_title(input_file)
    print('How many characters long is the longest title?', res, '\n')


def get_date_avg(input_file):
    res = reports.get_date_avg(input_file)
    print('What is the average of the release dates?', res, '\n')


def get_game(input_file):
    title = input('Enter a title:')
    res = reports.get_game(input_file, title)
    res = [str(x) for x in res]
    res = ', '.join(res)
    print('What properties has a game?', res, '\n')


def count_grouped_by_genre(input_file):
    res = reports.count_grouped_by_genre(input_file)
    res = [k + ':' + str(v) for k, v in res.items()]
    res = ', '.join(res)
    print('How many games are there grouped by genre?', res, '\n')


def get_date_ordered(input_file):
    res = reports.get_date_ordered(input_file)
    res = ', '.join(res)
    print('What is the date ordered list of the games? ', res, '\n')


def main():
    input_file = "game_stat.txt"
    get_most_played(input_file)
    sum_sold(input_file)
    get_selling_avg(input_file)
    count_longest_title(input_file)
    get_game(input_file)
    count_grouped_by_genre(input_file)
    get_date_ordered(input_file)


if __name__ == '__main__':
    main()
