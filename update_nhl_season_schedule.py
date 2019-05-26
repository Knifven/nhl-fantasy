season = '20182019'


def main():
    import pandas as pd
    import api_utils as au
    dates = au.get_season_schedule(season)
    struct_data = {
            'date': [],
            'gamePk': [],
            'home': [],
            'away': [],
            'homeScore': [],
            'awayScore': [],
            'season': [],
            'gameType': []
        }
    for d in dates:
        for g in d['games']:
            struct_data['date'].append(d['date'])
            struct_data['gamePk'].append(g['gamePk'])
            struct_data['home'].append(g['teams']['home']['team']['name'])
            struct_data['away'].append(g['teams']['away']['team']['name'])
            struct_data['homeScore'].append(g['teams']['home']['score'])
            struct_data['awayScore'].append(g['teams']['away']['score'])
            struct_data['season'].append(g['season'])
            struct_data['gameType'].append(g['gameType'])

    df = pd.DataFrame.from_dict(struct_data)
    df.to_csv('resources/nhl_schedule_' + season + '.csv', index=False)
    print('NHL Schedule updated for the ' + season + ' season')


if __name__ == '__main__':
    main()
