import requests
import pandas as pd


def get_season_schedule(season):
    url = 'https://statsapi.web.nhl.com/api/v1/schedule/'
    payload = {
        'season': season
    }
    r = requests.get(url, params=payload)
    return r.json()['dates']


def get_teams():
    url = 'https://statsapi.web.nhl.com/api/v1/teams/'
    r = requests.get(url)
    return pd.io.json.json_normalize(r.json()['teams'])


def get_team_roster(team_id):
    url = 'https://statsapi.web.nhl.com/api/v1/teams/' + str(team_id) + '/roster'
    r = requests.get(url)
    return pd.io.json.json_normalize(r.json()['roster'])
