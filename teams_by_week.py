import pandas as pd
import utils

schedule_path = 'resources/nhl_schedule_20182019.csv'


def main():
    schedule = pd.read_csv(schedule_path)
    utils.get_weekly_games_by_team(schedule)


if __name__ == '__main__':
    main()
