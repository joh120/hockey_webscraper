from bs4 import BeautifulSoup

import requests 
import csv


url = 'https://www.scrapethissite.com/pages/forms/'

hockey_site = requests.get(url) # request to get establish access to hockey webpage
                                # status code is 200 - OK

soup = BeautifulSoup(hockey_site.text, 'lxml') # allows to use BeautifulSoup to extract data from the hockey webpage

file_path = "hockey_teams.csv"

team_data = soup.find_all('tr', class_ ="team") # Look all teams information founded within the rows on the stat table


for team in team_data: # Takes hockey team information from each row and extracts it 

    team_name = team.find('td', class_="name").text.strip()

    team_year = team.find('td', class_="year").text.strip()
 
    team_wins = team.find('td', class_="wins").text.strip()
 
    team_losses = team.find('td', class_="losses").text.strip()

    hockey_stats = [[team_name, team_year, team_wins, team_losses]] # Take each of the following information from each row and puts in a list                                                                     #
    # print(hockey_stats)


    try:
        with open(file_path, "a", newline="") as file:
            content = csv.writer(file)
            for hockey_data in hockey_stats: # loop data in from the each row 
                content.writerow(hockey_data) # store the data as rows in the csv file
    except:
        print("File was not successfully created")
