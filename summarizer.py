#
# Author: Rustambek Sobithanov
# Course: CSc 110
# Description: The following lines of codes read in a game log file, process the information,
#              and print out a summary. The game log file includes lines which give information
#              in the order of: team player points. The program extracts that information and
#              creates a summary of the game by identifying who won the game and how many goals
#              each team scored, including information who and which team scored the first and
#              last goals.
#
#
def file_into_list(a_file):
    """
    The function takes a file of elements and appends them into a list using a nested for-loop
    :param a_file: a file with some lines of information in the format of: team player points
    :return: a list of elements in the order of: team player points
    """
    team_player_score = []
    for line in a_file:
        line = line.strip().split()
        for element in line:
            team_player_score.append(element)
    return team_player_score


def game_info(info_list):
    """
    The function identifies the two teams and how many goals each scored in the game
    :param info_list: a list of elements in the order of: team player points
    :return: the two teams and how many goals each scored in the game
    """

    # identifying the teams
    team_one = info_list[0]
    team_two = ''
    for index in range(0, len(info_list), 3):
        if info_list[index] != team_one:
            team_two = info_list[index]

    # determining how many goals each team scored
    score_one = 0
    score_two = 0
    index = 0
    while index < len(info_list):
        if info_list[index] == team_one:
            index += 2
            score_one += int(info_list[index])
            index += 1
        elif info_list[index] == team_two:
            index += 2
            score_two += int(info_list[index])
            index += 1
    return team_one, team_two, score_one, score_two


def results(info_list):
    """
    The function calculates the results of the game and prints out the winner,
    how many goals each team scored (printing first the one that scored the first goal then
    the other one), and which player scored the first goal and which player scored the last.
    :param info_list: a list of elements in the order of: team player points
    """

    # finding out who is the winner and loser of the game
    team_one, team_two, score_one, score_two = game_info(info_list)
    winner = ''
    loser = ''
    if score_one > score_two:
        winner += team_one
        loser += team_two
    else:
        winner += team_two
        loser += team_one

    # determining who and which team scored the first and last goals
    first_player = info_list[1]
    first_team_to_score = info_list[0]
    last_team_to_score = ''
    if winner == first_team_to_score:
        last_team_to_score += loser
    else:
        last_team_to_score += winner
    last_player = info_list[len(info_list) - 2]

    # printing the results
    print(winner, 'won!')
    print(first_team_to_score, 'scored', str(score_one), 'points.')
    print(last_team_to_score, 'scored', str(score_two), 'points.')
    print(first_player, 'scored first.')
    print(last_player, 'scored last.')


def main():
    file_name = input('enter gamelog file name:\n')
    a_file = open(file_name, 'r')
    info_list = file_into_list(a_file)
    results(info_list)


main()
