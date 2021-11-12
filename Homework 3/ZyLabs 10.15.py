#Ismael Diaz (PSID: 1846093)
#CIS 2348 Homework #3 Zylabs 10.11

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":
    name = input()
    wins = float(input())
    losses = float(input())

    team1 = Team()
    team1.team_name = name
    team1.team_wins = wins
    team1.team_losses = losses

    if team1.get_win_percentage() >= .50:
        print("Congratulations, Team {} has a winning average!".format(team1.team_name))
    else:
        print("Team {} has a losing average.".format(team1.team_name))
