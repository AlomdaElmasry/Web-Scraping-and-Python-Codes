import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd


def getFixtures():
    url = "http://www.bbc.com/sport/football/premier-league/fixtures"
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, 'html.parser')

    main = soup.find("table", attrs={'class': 'table-stats'})

    home_team = []
    away_team = []
    time = []

    for j in main.find_all("span", attrs={"class": "team-home teams"}):
        home_team.append(j.text)

    home_team = map(lambda s: s.strip(), home_team)

    for j in main.find_all("span", attrs={"class": "team-away teams"}):
        away_team.append(j.text)

    away_team = map(lambda s: s.strip(), away_team)

    for j in main.find_all("td", attrs = {"class" : "kickoff"}):
        time.append(j.text)

    time = map(lambda s: s.strip(), time)

    sequence = ["Home Team", "Away Team", "Time UTC"]
    df = pd.DataFrame()
    df = df.reindex(columns=sequence)
    df["Home Team"] = home_team
    df["Away Team"] = away_team
    df["Time UTC"] = time

    print "\n"

    for j in main.find_all('caption'):
        print '\033[1m' + j.text + '\033[00m'

    print "\n"
    print df.to_string()
    print "\n"


getFixtures()

