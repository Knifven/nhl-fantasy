import pandas as pd
import api_utils as au


def update_fantasy_roster_info(roster):
    new_roster = pd.DataFrame()
    if roster['player_id'].isnull().sum() > 0:
        missing_players = roster[roster['player_id'].isnull()]['name'].values
        teams = au.get_teams()
        for team_id in teams['id']:
            team_roster = au.get_team_roster(team_id)
            idx = team_roster['person.fullName'].isin(missing_players)
            if idx.any():
                team_roster = team_roster[idx]
                roster_part = roster.merge(team_roster, how='inner', left_on='name', right_on='person.fullName')
                roster_part['team'] = teams[teams['id'] == team_id].name.any()
                new_roster = pd.concat([new_roster, roster_part], ignore_index=True)
        cols = ['first_name', 'last_name', 'active_position', 'positions', 'name', 'team', 'jerseyNumber', 'person.id',
                'person.link', 'position.abbreviation']
    new_roster = new_roster[cols]
    return new_roster


def get_weekly_games_by_team(schedule):
    schedule['date'] = pd.to_datetime(schedule['date']) - \
                       pd.to_timedelta(pd.to_datetime(schedule['date']).dt.weekday, unit='D')
    schedule['date'] = schedule['date'].dt.date
    df_home = schedule[['date', 'home']].copy()
    df_home.rename(columns={'home': 'team'}, inplace=True)
    df_home['home'] = 1
    df_away = schedule[['date', 'away']].copy()
    df_away.rename(columns={'away': 'team'}, inplace=True)
    df_away['away'] = 1
    df = pd.concat([df_home, df_away], ignore_index=True, sort=True)
    df['home'].fillna(0, inplace=True)
    df['away'].fillna(0, inplace=True)
    df['total'] = df['home'] + df['away']
    df = pd.DataFrame(df.groupby(['date', 'team']).aggregate(sum).reset_index())
    return df
