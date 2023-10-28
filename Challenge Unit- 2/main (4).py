class Player:
  def __init__(self, name, team):
      self.name = name
      self.team = team

  def play(self):
      pass

class Batsman(Player):
  def play(self):
      return "The batsman is batting."

class Bowler(Player):
  def play(self):
      return "The bowler is bowling."
batsman1 = Batsman("Sachin Tendulkar", "India")
bowler1 = Bowler("Shane Warne", "Australia")


print(batsman1.play())
print(bowler1.play())