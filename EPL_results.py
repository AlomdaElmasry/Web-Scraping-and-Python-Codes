import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd

def showResults():
    url = "http://www.bbc.com/sport/football/premier-league/results"
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, 'html.parser')

    table = soup.find("table", attrs={'class': 'table-stats'})

    for i in table.find_all("caption"):
        print '\033[1m' + i.text + '\033[00m'

    home_team = []
    away_team = []
    score = []

    for i in table.find_all("span", attrs={'class': 'team-home teams'}):
        home_team.append(i.text)

    for i in table.find_all("span", attrs={'class': 'team-away teams'}):
        away_team.append(i.text)

    for i in table.find_all("span", attrs={'class':'score'}):
        score.append(i.text)

    home_team = map(lambda s: s.strip(), home_team)
    away_team = map(lambda s: s.strip(), away_team)
    score = map(lambda s: s.strip(), score)

    sequence = ["Home Team", "Score", "Away Team"]
    df = pd.DataFrame()
    df = df.reindex(columns=sequence)
    df["Home Team"] = home_team
    df["Score"] = score
    df["Away Team"] = away_team

    print df.to_string()

showResults()