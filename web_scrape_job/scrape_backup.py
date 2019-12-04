import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

allTeams_url = 'http://quikstatsiowa.com/Public/Soccer/TeamStandings.aspx?IDSport=65E5DA09-90C6-45F5-847A-F9A84FD9C5B0'
uClient = uReq(allTeams_url)  
page_html = uClient.read()
uClient.close()
#parse
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"container"})
container = containers[0]

containerFile = open("containers.txt", "w+")
containerFile.write(str(container))

content = container.findAll("div",{"class":"content"})
contentFile = open("content.txt", "w+")
contentFile.write(str(content))

formcontainer = container.findAll("div",{"class":"formcontainer","style":"width: 1000px;"})
formcontainerFile = open("formcontainers.txt", "w+")
formcontainerFile.write(str(formcontainer))

table = container.findAll("table",{"style":"width: 100%; border-collapse: collapse;"})
tableFile = open("table.txt", "w+")
tableFile.write(str(table))

table_columns = container.findAll("tr",{"style":"height: 30px;"})

records = container.findAll("td",{"style":"text-align: center;"})

team_num = 1
team_max = 154
team_statNum = 0 
team_statMax = 15

filename = "team_stats.csv"
f = open(filename, "w")

headers = "Team, Record, GP, G, A, P, Sh, Sh %, SOG, SOG %, CK, PKM, GA, GA Avg, S, S %\n"
f.write(headers)

#Teams
for team in table_columns:
	table_columns = container.findAll("tr",{"style":"height: 30px;"})
	table_column = table_columns[team_num]
	team = table_column.td
	team_name = team.a.text
	# print(team_name)

	f.write(team_name + "," record + "," + games_played + "," + goals + "," + assists + "," + points "," + shots "," + shot_percentage + "," + shots_on_goal + "," + shots_on_goal_percent + "," + corner_kicks + "," + penalty_kick_made + "," + penalty_attempts + "," + goals_against + "," + goals_against_avg + "," + saves + "," + saves_percent + "\n")

	team_num += 1

	if team_num >= team_max:
		team_num = 1
		break

for team in table_columns:
	table_columns = container.findAll("tr",{"style":"height: 30px;"})
	table_column = table_columns[1]
	print(table_column)
	record = records[1]
	# print(record)
	# print(team_num)
	# print(team_name)

	team_num += 1

	if team_num >= team_max:
		break


	


#Stats
# for team in table_columns:
# 	table_stats = container.findAll("td",{"style":"text-align: center;" and "text-align: center; border-left: solid 1px black;"}) 
# 	table_statGet = table_stats[team_statNum]
# 	table_stat = table_statGet.span

# 	print(table_stat)
	
# 	team_statNum += 1

# 	f.write(str(table_stat) + ",")

# 	if team_statNum == team_statMax:
# 		team_statNum = 0
# 		f.write("\n")




# for team in table_columns:
# 	table_columns = container.findAll("tr",{"style":"height: 30px;"})
# 	table_column = table_columns[team_num]
# 	team = table_column.td
# 	team_link = team.a["href"]
# 	print("team_link: http://quikstatsiowa.com/Public/Soccer/" + team_link)
# 	team_hyperlink = "http://quikstatsiowa.com/Public/Soccer/" + team_link

# 	team_num += 1

# 	if team_num >= team_max:
# 		break

f.close()


tableColumnsFile = open("table_columns.txt", "w+")
tableColumnsFile.write(str(table_columns))
