import requests
import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os 

try:
	os.system('cls')
except Exception as e:
	os.system('clear')
else:
	pass

print(f"""                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %           =?000?                    
                      ?0%0?           %         %&0?====                    
                   =&%?=  ?%%   = = &0@%0==    &0                           
                            =&??#%@@#####@@@%?&?                            
                             0################0     =?0?=                   
                             %################@&  0&0?=?0%%?                
                     ===   %@##################@@&?        ?=               
                  =&%0??00%#######&%&##@%%@######%                          
                 0&       ?@####@=   0&    &#####%=                         
                0%        %@####&  ##?0@#? ?#####&%%0?                      
                ?        ?%######= ?0%@?0  &####@%   ?&=                    
                       =&0?%######&&@###&&#######&    ?@                    
                       @=  @@##################@%=     &0                   
                      00    ?&################@0       =@                   
                      @     &%&#############@&&%        0                   
                     ?&    &? =?&@&&#####@&@?  0&                           
                      =   ?%       ===00@0 ?    &=                          
                          ?&                    00                          
                           =                     ?                          
                                                                                                         
                                              
          			Quik Stats Iowa Web Crawler        
				By Syeam Bin Abdullah                                                                                                                                                                                                                              
                                                                                                                                            """)
input("""		--------- Press Any Key to Initiate Data Extraction -------												  """)

try:
	os.system('cls')
except Exception as e:
	os.system('clear')
else:
	pass

#########
##TEAMS##
#########

print('		---RUNNING INITIALIZATION FOR TEAM DATA EXTRACTION---		')
print('Requesting URL for Team Data...')
page_html = requests.get('http://quikstatsiowa.com/Public/Soccer/TeamStandings.aspx?IDSport=65E5DA09-90C6-45F5-847A-F9A84FD9C5B0').text
#parse
print('URL request successful')
print('Parsing HTML...')
page_soup = soup(page_html, "lxml")
print('Parsed successfully')
containers = page_soup.findAll("div",{"class":"container"})
container = containers[0]

print("Storing tag data...")
containerFile = open("parsed_pages/containers.txt", "w+")
containerFile.write(str(container.prettify()))

content = container.findAll("div",{"class":"content"})
contentFile = open("parsed_pages/content.txt", "w+")
contentFile.write(str(content))

formcontainer = container.findAll("div",{"class":"formcontainer","style":"width: 1000px;"})
formcontainerFile = open("parsed_pages/formcontainers.txt", "w+")
formcontainerFile.write(str(formcontainer))

table = container.findAll("table",{"style":"width: 100%; border-collapse: collapse;"})
tableFile = open("parsed_pages/table.txt", "w+")
tableFile.write(str(table))

table_columns = container.findAll("tr",{"style":"height: 30px;"})

records = container.findAll("td",{"style":"text-align: center;"})

print("Stored Successfully")

teamFile = "team_stats.csv"
f = open(teamFile, "w")

headers = "Team, Record, GP, G, A, P, Sh, Sh %, SOG, SOG %, CK, PKM, PKA, GA, Avg, S, S %\n"
f.write(headers)

print("INITIALIZATION COMPLETE")
print("Extracting Team Data...")

team_num = 1
team_links = []

#Teams
for team in range(team_num, len(table_columns)):
	table_columns = container.findAll("tr",{"style":"height: 30px;"})
	table_column = table_columns[team_num]
	team = table_column.td
	team_links.append(f'http://quikstatsiowa.com/Public/Soccer/{team.a["href"]}')
	team_name = team.a.text

	team_stats = table_column.findAll("td",{"style":"text-align: center;"})
	team_ga = table_column.findAll("td",{"style":"text-align: center; border-left: solid 1px black;"})
	
	rec_stat = team_stats[0].text.strip()
	games_played = team_stats[1].text.strip()
	goals = team_stats[2].text.strip()
	assists = team_stats[3].text.strip()
	points = team_stats[4].text.strip()
	shots = team_stats[5].text.strip()
	shot_percentage = team_stats[6].text.strip()
	shots_on_goal = team_stats[7].text.strip()
	shots_on_goal_percent = team_stats[8].text.strip()
	corner_kicks = team_stats[9].text.strip()
	penalty_kick_made = team_stats[10].text.strip()
	penalty_attempts = team_stats[11].text.strip()
	goals_against = team_ga[0].text.strip()
	goals_against_avg = team_stats[12].text.strip()
	saves = team_stats[13].text.strip()
	saves_percent = team_stats[14].text.strip()

	# print(team_name)

	# f.write(team_name + "," + rec_stat + "," + games_played + "," + goals + "," + assists + "," + points + "," + shots + "," + shot_percentage + "," + shots_on_goal + "," + shots_on_goal_percent + "," + corner_kicks + "," + penalty_kick_made + "," + penalty_attempts + "," + goals_against + "," + goals_against_avg + "," + saves + "," + saves_percent + "\n")
	
	f.write(f"{team_name}  ,  {rec_stat}  ,  {games_played}  ,  {goals}  ,  {assists}  ,  {points}  ,  {shots}  ,  {shot_percentage}  ,  {shots_on_goal}  ,  {shots_on_goal_percent}  ,  {corner_kicks}  ,  {penalty_kick_made}  ,  {penalty_attempts}  ,  {goals_against}  ,  {goals_against_avg}  ,  {saves}  ,  {saves_percent}  \n")

	team_num += 1


f.close()

print(f"\n\nTeam data successfully extracted to: {teamFile}\n\n")

tableColumnsFile = open("parsed_pages/table_columns.txt", "w+")
tableColumnsFile.write(str(table_columns))


###########################
### INDIVIDUAL PLAYERS ####m
###########################

print('		---RUNNING INITIALIZATION FOR PLAYER DATA EXTRACTION---		')
print('Requesting URL for Team Data...')
indiv_page_html = requests.get('http://quikstatsiowa.com/Public/Soccer/IndividualStandings.aspx?IDSport=65E5DA09-90C6-45F5-847A-F9A84FD9C5B0&IDSportSeason=h201903050124242861ca0fcfe178e41').text
print('URL request successful')
#parse
print('Parsing HTML...')
indiv_page_soup = soup(indiv_page_html, "lxml")
print('Parsed successfully')
indiv_containers = indiv_page_soup.findAll("div",{"class":"container"})
indiv_container = indiv_containers[0]
print("Storing tag data...")
indiv_containerFile = open("parsed_pages/indiv_containers.txt", "w+")
indiv_containerFile.write(str(indiv_container.prettify()))

indiv_content = indiv_container.findAll("div",{"class":"content"})
indiv_contentFile = open("parsed_pages/indiv_content.txt", "w+")
indiv_contentFile.write(str(indiv_content))

indiv_formcontainer = indiv_container.findAll("div",{"class":"formcontainer","style":"width: 1000px;"})
indiv_formcontainerFile = open("parsed_pages/indiv_formcontainers.txt", "w+")
indiv_formcontainerFile.write(str(indiv_formcontainer))

indiv_formcontent = indiv_container.findAll("div",{"class":"formcontent"})
indiv_formcontentFile = open("parsed_pages/indiv_formcontent.txt", "w+")
indiv_formcontentFile.write(str(indiv_formcontent))
indiv_formcontentList = indiv_formcontent[0]

indiv_table = indiv_formcontentList.findAll("table",{"style":"width: 100%; border-collapse: collapse; table-layout: fixed;"})
indiv_tableFile = open("parsed_pages/indiv_table.txt", "w+")
indiv_tableFile.write(str(indiv_table))
indiv_tableList = indiv_table[0]

indiv_columns = indiv_container.findAll("tr",{"style":"height: 30px;"})
indiv_columnsFile = open("parsed_pages/indiv_columns.txt", "w+")
indiv_columnsFile.write(str(indiv_columns))
print("Stored Successfully")

playerFile = "players.csv"

i = open(playerFile, "w")

playerHeaders = " Athlete, Team, GP, GS, G, A, P, Sh, Sh %, SOG, SOG %, PKM, PKA, GM, GA, GA Avg, S, S %\n"
i.write(playerHeaders)

player_num = 1

print("INITIALIZATION COMPLETE")
print("Extracting Player Data...")

for player in range(player_num, len(indiv_columns)):
	indiv_columnsList = indiv_columns[player_num]

	player = indiv_columnsList.td
	player_name = player.span.text.strip()

	player_teamCheck = indiv_columnsList.findAll("td",{"style":"text-align: left;"})
	player_teamFile = open("parsed_pages/player_team.txt", "a")
	player_teamFile.write(str(player_teamCheck[1]) + "\n")

	player_stats = indiv_columnsList.findAll("td",{"style":"text-align: center;"})
	player_gm_stat = indiv_columnsList.findAll("td",{"style":"text-align: center; border-left: solid 1px black;"})

	player_team = player_teamCheck[1].a.text.strip()
	player_gp = player_stats[0].span.text.strip()
	player_gs = player_stats[1].span.text.strip()
	player_g = player_stats[2].span.text.strip()
	player_a = player_stats[3].span.text.strip()
	player_p = player_stats[4].span.text.strip()
	player_sh = player_stats[5].span.text.strip()
	player_sh_percent = player_stats[6].span.text.strip()
	player_sog = player_stats[7].span.text.strip()
	player_sog_percent = player_stats[8].span.text.strip()
	player_pkm = player_stats[9].span.text.strip()
	player_gm = player_gm_stat[0].span.text.strip()
	player_pka = player_stats[10].span.text.strip()
	player_ga = player_stats[11].span.text.strip()
	player_ga_avg = player_stats[12].span.text.strip()
	player_s = player_stats[13].span.text.strip()
	player_s_percent = player_stats[14].span.text.strip()

	i.write(player_name + "," + player_team + "," + player_gp + "," + player_gs + "," + player_g + "," + player_a + "," + player_p + "," + player_sh + "," + player_sh_percent + "," + player_sog + "," + player_sog_percent + "," + player_pkm + "," + player_pka + "," + player_gm + "," + player_ga + "," + player_ga_avg + "," + player_s + "," + player_s_percent + "\n")

	player_num += 1


player_teamFile = open("parsed_pages/player_team.txt", "w+")
player_teamFile.write(str(indiv_columnsList))
	

i.close()

print(f"\n\nPlayer data successfully extracted to: {playerFile}\n\n")


###########################
#### SINGLE GAME STATS ####
###########################

print('		---RUNNING INITIALIZATION FOR SINGLE GAME DATA EXTRACTION---		')
print('Requesting URL for Individual/Game (Single) Data...')
single_page_html = requests.get('http://quikstatsiowa.com/Public/Soccer/IndividualBestGameStandings.aspx?IDSport=65E5DA09-90C6-45F5-847A-F9A84FD9C5B0').text
print('URL request successful')
#parse
print('Parsing HTML...')
single_page_soup = soup(single_page_html, "lxml")
print('Parsed successfully')
single_container = single_page_soup.findAll("div",{"class":"container"})[0]
print("Storing tag data...")
single_containerFile = open("parsed_pages/single_container.txt", "w+")
single_containerFile.write(str(single_container.prettify()))

single_table = single_container.findAll("table")[1]
single_tableFile = open("parsed_pages/single_table.txt", "w+")
single_tableFile.write(str(single_table.prettify()))

single_columns = single_table.findAll("tr")
single_columnsFile = open("parsed_pages/single_columns.txt", "w+")
single_columnsFile.write(str(single_columns))


athlete_num = 1

singleFile = "single_game.csv"
s = open(singleFile, "w")
singleHeaders = "Athlete, Team, Goals, Date, Location, Opponent\n"
s.write(singleHeaders)

print("INITIALIZATION COMPLETE")
print("Extracting Single Game Data...")

for player in range(athlete_num, len(single_columns)):
	searching_column = single_columns[athlete_num]
	column_scan = searching_column.findAll("td")

	athlete = column_scan[0].span.text
	single_team = column_scan[1].a.text
	single_goals = column_scan[2].span.text
	single_date = column_scan[3].span.text
	single_location = column_scan[5].span.text
	single_opponent = column_scan[6].span.text

	s.write(f"{athlete}, {single_team}, {single_goals}, {single_date}, {single_location}, {single_opponent}\n")

	athlete_num += 1

s.close()

print(f"\n\Single Best Game data successfully extracted to: {singleFile}\n\n")

#Team Game Hsistory
print('		---RUNNING INITIALIZATION FOR TEAM GAME SCHEDULE DATA EXTRACTION---		')
link_num = 0 
for team_link in range(link_num, len(team_links)):
	print(f"Job: {link_num}/{len(team_links)}")
	print("Requesting")
	team_link = team_links[link_num]
	print("Opening Link")
	game = requests.get(team_link).text
	print("Souping Link")
	game_soup = soup(game, 'lxml')
	print("Finding Team Name")
	table_titles = game_soup.findAll("span", {"id":"ctl00_ContentPlaceHolder1_ui_TeamRosterSchedule_ui_Title_Label"})
	table_title = table_titles[0].text
	print(f"Found Team Name: {table_title}")
	
	print("Gathering Info") 
	game_container = game_soup.findAll("div", {"class":"container"})[0]
	game_containerFile = open("container.txt", "w+")
	game_containerFile.write(str(container.prettify()))
	team_tables = game_container.findAll("table")


	# print(f"{team_tables}\n\n\n")
	team_table = team_tables[3]

	print("start of the line")
	team_rows = team_table.findAll("tr")
	# print(f"{team_rows}\n\n\n")
	print("end of the line")
	
	print("Setting Directory")
	game_stats = f'game_stats/{table_title}.csv'
	print("Open")
	g = open(game_stats, "w")
	print("Write")
	gHeaders = "Status, Date, Location, Opponent, Outcome, Score\n"
	g.write(gHeaders)

	row_num = 1
	for status in range(row_num, len(team_rows)):
		# print(f"{team_rows}\n\n\n")
		# print(f"{team_rows[1]}\n\n\n")
		row = team_rows[row_num]
		column = row.findAll("td")

		team_status = column[0].span.text
		date = column[1].span.text
		location = column[2].span.text
		opponent = column[3].a.text
		outcome = column[4].span.text
		if outcome == '':
			outcome = 'Game Cancelled'
		else:
			pass
		score = column[5].a.text
		if score == '':
			score = 'N/A'
		else:
			pass
		
		
		g.write(f"{team_status}, {date}, {location}, {opponent}, {outcome}, {score}\n")
		row_num += 1
	g.write(f"Team Page: {team_link}")
	print("Close\n")
	g.close()
	link_num += 1
	try:
		os.system('cls')
	except:
		os.system('clear')
	else:
		pass
print("""                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %                                     
                                      %           =?000?                    
                      ?0%0?           %         %&0?====                    
                   =&%?=  ?%%   = = &0@%0==    &0                           
                            =&??#%@@#####@@@%?&?                            
                             0################0     =?0?=                   
                             %################@&  0&0?=?0%%?                
                     ===   %@##################@@&?        ?=               
                  =&%0??00%#######&%&##@%%@######%                          
                 0&       ?@####@=   0&    &#####%=                         
                0%        %@####&  ##?0@#? ?#####&%%0?                      
                ?        ?%######= ?0%@?0  &####@%   ?&=                    
                       =&0?%######&&@###&&#######&    ?@                    
                       @=  @@##################@%=     &0                   
                      00    ?&################@0       =@                   
                      @     &%&#############@&&%        0                   
                     ?&    &? =?&@&&#####@&@?  0&                           
                      =   ?%       ===00@0 ?    &=                          
                          ?&                    00                          
                           =                     ?                          
                                                                             
""")

print('		---------- DATA EXTRACTION COMPLETE ----------		\n')

print("-----------------------------------------------------------------")
print(f"Team Season Stats saved to: {teamFile}")
print(f"Individual Season Stats saved to: {playerFile}")
print(f"Best Single Game stats saved to: {singleFile}")
print(f"Team Game Schedule saved to the game_stats folder")
print("-----------------------------------------------------------------")


# try:
# 	print("		---------- OPENING CSV DATA FILES ----------		")
# 	os.system(f'{teamFile}')
# 	os.system(f'{playerFile}')
# 	os.system(f'{singleFile}')
# except:
# 	pass