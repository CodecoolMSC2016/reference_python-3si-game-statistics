import reports

def count_games(input_file):
    res = str(reports.count_games(input_file))
    print('How many games are in the file?', res, '\n')
    return res

def decide(input_file):
    year = int(input('Enter a year:'))
    res = str(reports.decide(input_file, year))
    print('Is there a game from a given year?', res, '\n')
    return res

def get_latest(input_file):
    res = reports.get_latest(input_file)
    print('Which was the latest game?', res, '\n')
    return res

def count_by_genre(input_file):
    genre = input('Enter a genre:')
    res = str(reports.count_by_genre(input_file, genre))
    print('How many games do we have by genre?', res, '\n')
    return res

def get_line_number_by_title(input_file):
    title = input('Enter a title:')
    res = str(reports.get_line_number_by_title(input_file, title))
    print('What is the line number of the given game (by title)?', res, '\n')
    return res

def sort_abc(input_file):
    res = reports.sort_abc(input_file)
    res = ', '.join(res)
    print('What is the alphabetical ordered list of the titles?', res, '\n')
    return res

def get_genres(input_file):
    res = reports.get_genres(input_file)
    res = ', '.join(res)
    print('What are the genres?', res, '\n')
    return res

def when_was_top_sold_fps(input_file):
    res = str(reports.when_was_top_sold_fps(input_file))
    print('What is the release date of the top sold "First-person shooter" game?', res, '\n')
    return res

def main():
    input_file = "game_stat.txt"
    with open('game_stat_export.txt', 'w') as output_file:
        output_file.write(count_games(input_file))
        output_file.write('\n')

        output_file.write(decide(input_file))
        output_file.write('\n')

        output_file.write(get_latest(input_file))
        output_file.write('\n')

        output_file.write(count_by_genre(input_file))
        output_file.write('\n')

        output_file.write(sort_abc(input_file))
        output_file.write('\n')

        output_file.write(get_genres(input_file))
        output_file.write('\n')

        output_file.write(when_was_top_sold_fps(input_file))
        output_file.write('\n')

if __name__ == '__main__':
    main()
