class Player:

  # def __init__(self, name, team):
  def __init__(self, name, xp, team):
    self.name = name
    self.xp = xp
    self.team = team

  def introduce(self):
    # print(f" Hello ! I'm {self.name} and I'm for {self.team}")
    print(f" Hello ! I'm {self.name} and I'm for {self.team} My xp is {self.xp}")

class Team:

  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []
    self.total_xp = 0

  def add_player(self, name, xp):
    new_player = Player(name, xp, self.team_name)
    self.players.append(new_player)
    self.total_xp = self.total_xp + new_player.xp

  def remove_player(self, name):
    for player in self.players:
      if player.name == name:
        self.players.remove(player)
        self.total_xp = self.total_xp - player.xp

  def show_players(self):
      for player in self.players:
        player.introduce()

  def show_total_xp(self):
    print(f"{self.team_name} total xp is {self.total_xp}")

# nico = Player(name = "nico", team = "Team X")
# nico.introduce()

# lynn = Player(name = "lynn", team ='Team Blue')
# lynn.introduce()

team_x = Team("Team X")
team_x.add_player(name = "nico", xp = 2000)
team_x.add_player(name = "jason", xp = 1000 )
team_x.show_players()
team_x.show_total_xp()
print("-------------")
team_x.remove_player("jason")
team_x.show_players()
team_x.show_total_xp()

print("==========================================")

team_blue = Team("Blue Team")
team_blue.add_player(name = "Lynn", xp = 3000)
team_blue.add_player(name = "Lee", xp = 3000)
team_blue.show_players()
team_blue.show_total_xp()
print("-------------")
team_blue.remove_player("Lee")
team_blue.show_players()
team_blue.show_total_xp()