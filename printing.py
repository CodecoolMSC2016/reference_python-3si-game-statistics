import reports


def count_games(input_file):
    res = reports.count_games(input_file)
    print('How many games are in the file?', res, '\n')


def decide(input_file):
    year = int(input('Enter a year:'))
    res = reports.decide(input_file, year)
    print('Is there a game from a given year?', res, '\n')


def get_latest(input_file):
    res = reports.get_latest(input_file)
    print('Which was the latest game?', res, '\n')


def count_by_genre(input_file):
    genre = input('Enter a genre:')
    res = reports.count_by_genre(input_file, genre)
    print('How many games do we have by genre?', res, '\n')


def get_line_number_by_title(input_file):
    title = input('Enter a title:')
    res = reports.get_line_number_by_title(input_file, title)
    print('What is the line number of the given game (by title)?', res, '\n')


def sort_abc(input_file):
    res = reports.sort_abc(input_file)
    res = ', '.join(res)
    print('What is the alphabetical ordered list of the titles?', res, '\n')


def get_genres(input_file):
    res = reports.get_genres(input_file)
    res = ', '.join(res)
    print('What are the genres?', res, '\n')


def when_was_top_sold_fps(input_file):
    res = reports.when_was_top_sold_fps(input_file)
    print('What is the release date of the top sold "First-person shooter" game?', res, '\n')


def main():
    input_file = "game_stat.txt"
    count_games(input_file)
    decide(input_file)
    get_latest(input_file)
    count_by_genre(input_file)
    sort_abc(input_file)
    get_genres(input_file)
    when_was_top_sold_fps(input_file)


if __name__ == '__main__':
    main()
