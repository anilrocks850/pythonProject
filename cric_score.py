import csv
players_dict = dict()
country_match_dict = dict()
def ordinal_for_num (n):
    if n==1:
        return "st"
    if n==2:
        return 'nd'
    if n==3:
        return 'rd'
    if n>3:
        return 'th'


def score_card(csv_reader):
    # line = list(next(csv_reader))
    country_dict = dict()
    i = 1

    for line in csv_reader:
        if i == 20:
            break
        i += 1
    for line in csv_reader:
        if len(line) == 4:
            line = list(line)
            if line[2] not in country_dict:
                country_dict[line[2]] = {'team_score': 0, 'wickets': 0}
                country_dict[line[2]][line[3]] = {'score': 0, 'balls': 0, 'strike_rate': 0, '4s': 0,
                                                  '6s': 0, 'wickets': 0, 'overs': 0, 'runs_conceded': 0, 'economy': 0}
            if line[2] in country_dict:
                if line[3] not in country_dict[line[2]]:
                    country_dict[line[2]][line[3]] = {'score': 0, 'balls': 0, 'strike_rate': 0,
                                                      'strike_rate': 0, '4s': 0, '6s': 0, 'wickets': 0, 'overs': 0,
                                                      'runs_conceded': 0, 'economy': 0}
            if line[3] not in players_dict:
                players_dict[line[3]] = {'matches':0,'total_score': 0, 'total_balls': 0, 'total_strike_rate': 0, 'innings': 0,
                                         'average': 0, 'wickets': 0,'total_4s':0,'total_6s':0,'50s':0,'100s':0}
            if line[3] in players_dict:
                players_dict[line[3]]['matches'] +=1
        else:
            break
    print(country_dict['India'])
    print(players_dict)
    teams = list(country_dict.keys())
    match_between = 'India' + " and "+ teams[1-(teams.index('India'))]
    if match_between in country_match_dict:
        country_match_dict[match_between] += 1
        print("This is " + str(country_match_dict[match_between]) + ordinal_for_num (country_match_dict[match_between]) + " match between " + match_between)
    if match_between not in country_match_dict:
        country_match_dict[match_between] = 1
        print("This is 1st match between " + match_between)

    def update_score_by_ball(input_ball):
        x = (country_dict[input_ball[3]][input_ball[4]]['score']) // 50
        country_dict[input_ball[3]][input_ball[4]]['score'] += int(input_ball[7])
        # if it is 4 or 6
        if int(input_ball[7]) == 4:
            country_dict[input_ball[3]][input_ball[4]]['4s'] += 1
            players_dict[line[4]]['total_4s']+=1
        if int(input_ball[7]) == 6:
            country_dict[input_ball[3]][input_ball[4]]['6s'] += 1
            players_dict[line[4]]['total_6s'] += 1


        # 50 and 100
        y = (country_dict[input_ball[3]][input_ball[4]]['score']) // 50
        if y-x == 1 and y==1:
            print("At " + input_ball[2] + " " + input_ball[4] + " scored " + str(y * 50) + " runs..")
            players_dict[line[4]]['50s'] += 1
            if players_dict[line[4]]['50s'] == 1:
                print("It's Maiden 50 for " + input_ball[4])
            else:
                print("It's 50 number " + str(players_dict[line[4]]['50s']) +" for " + input_ball[4] )
        if y-x == 1 and y==2:
            print("At " + input_ball[2] + " " + input_ball[4] + " scored " + str(y * 50) + " runs..")
            players_dict[line[4]]['100s'] += 1
            players_dict[line[4]]['50s'] -= 1
            if players_dict[line[4]]['100s'] == 1:
                print("It's Maiden 100 for " + input_ball[4])
            else:
                print("It's 100 number " + str(players_dict[line[4]]['50s']) +" for " + input_ball[4] )
        # bowling_team
        team_index = teams.index(input_ball[3])
        opponent_team = teams[1 - team_index]
        # if it was a wicket
        if input_ball[14] != "":
            country_dict[input_ball[3]]['wickets'] += 1
            country_dict[input_ball[3]][input_ball[15]]['type_of_dismissal'] = input_ball[14]
            if input_ball[14] != "run out":
                # increase wicket count to bowler
                country_dict[opponent_team][input_ball[6]]['wickets'] += 1
                players_dict[input_ball[6]]['wickets'] += 1
                print(input_ball[2] + " " + input_ball[15] + " " + input_ball[14] + " (bowler) " + input_ball[6])
            else:
                print(input_ball[2] + " " + input_ball[15] + " " + input_ball[14])
        # balls faced by batsman
        country_dict[input_ball[3]][input_ball[4]]['balls'] += 1
        # strike_rate of batsman
        country_dict[input_ball[3]][input_ball[4]]['strike_rate'] = round(100 * (
                    country_dict[input_ball[3]][input_ball[4]]['score'] / country_dict[input_ball[3]][input_ball[4]][
                'balls']), 2)
        # team_score
        country_dict[input_ball[3]]['team_score'] += (int(input_ball[7]) + int(input_ball[8]))
        # {'total_score': 0, 'total_balls': 0, 'total_strike_rate': 0, 'innings': 0,
        # 'average': 0,'wickets':0}
        a = players_dict[input_ball[4]]['total_score'] // 1000
        players_dict[input_ball[4]]['total_balls'] += 1
        players_dict[input_ball[4]]['total_score'] += int(input_ball[7])
        b = players_dict[input_ball[4]]['total_score'] // 1000
        if b - a != 0:
            print(input_ball[4] + " scored " + str(b * 1000) + " runs ")
        players_dict[input_ball[4]]['total_strike_rate'] = round(
            100 * (players_dict[input_ball[4]]['total_score'] / players_dict[input_ball[4]]['total_balls']), 2)

    for line in csv_reader:
        if len(line) == 16:
            input_ball = list(line)
            update_score_by_ball(input_ball)
    print(country_dict['India'])
    print(country_dict[teams[1-(teams.index('India'))]])
    # print(players_dict)


with open("64939.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    score_card(csv_reader)
with open("64941.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    score_card(csv_reader)
with open("64943.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    score_card(csv_reader)
with open("65032.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    score_card(csv_reader)
print(players_dict)
























