# example teams.py (OOP inheritance approach)
class Team():
    def __init__(self, name, city="CITY NAME", players=["Player 1"]):
        self.name = name
        self.city = city
        self.players = players
    def advertise(self):
        #print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR GAMES!!!")
    @property
    def full_name(self):
        #return f"{my_team['city']} {my_team['name']}"
        return f"{self.city} {self.name}"
class BaseballTeam(Team):
    def __init__(self, name, city, starting_pitcher, players=["Player 1"]):
        super().__init__(name, city, players)
        self.starting_pitcher = starting_pitcher
    def advertise(self):
        #print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")
        print(f"HEY COME TO {self.city.upper()} TO SEE OUR PITCHER {self.starting_pitcher}!!!")
if __name__ == "__main__":
    football_team = Team("Cowboys", "Dallas")
    print(football_team.full_name)
    football_team.advertise()
    teams = [
        {"city": "New York", "name": "Yankees", "pitcher": "John"},
        {"city": "New York", "name": "Mets", "pitcher": "Jane"},
        {"city": "Boston", "name": "Red Sox",  "pitcher": "Ames"},
        {"city": "New Haven", "name": "Ravens",  "pitcher": "Vishal"},
        {"city": "Washington", "name": "Nationals",  "pitcher": "Cody"}
    ]
    for team_attributes in teams:
        team = BaseballTeam(name=team_attributes["name"], city=team_attributes["city"], starting_pitcher=team_attributes["pitcher"])
        print("-------")
        #print(full_name(team))
        #advertise(team)
        print(team.city)
        print(team.full_name)
        print(team.players)
        print(team.starting_pitcher)
        team.advertise()
    # df1 = DataFrame({"x": [1,2,3], "y": [4,5,6]})
    # df1.head()
    # df1.columns
    # df2 = DataFrame({"x": [7,7,7], "y": [4,4,4]})
    # df2.head()
    #team = Team(city="Washington", name="Wizards") # initialize / create an instance of the object
    #print(team)
    #print(type(team))
    #print(team.name) # invoking attributes
    #print(team.city) # invoking attributes
#
    #team2 = Team("Giants", "New York") # initialize / create an instance of the object
    #print(team2)
    #print(type(team2))
    #print(team2.name) # invoking attributes
    #print(team2.city) # invoking attributes