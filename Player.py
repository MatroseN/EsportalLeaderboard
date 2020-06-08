# This class represents a player. You instantiate a player and then add the relevant stats to the player


class Player:
    def __init__(self, name, iD, matchesURL):
        self.name = name
        self.iD = iD
        self.matchesURL = matchesURL
        self.matches = []
        self.matchURLSTART = ""
        self.matchURLMID = "id="
        self.matchURLEND = ""
        self.kdr = 0
        self.clutches = 0
        self.openingKills = 0
        self.hSP = 0
        self.assists = 0
        self.eloChange = 0
        self.mostKillsInOneMatch = 0
        self.defuses = 0
        self.plants = 0

    def printStats(self):
        print(self.name)
        print("Kdr: ", self.kdr, "Clutches: ", self.clutches, "Opening kills: ", self.openingKills, "Hs%: ",
              self.hSP, '%', "Assists: ", self.assists, "Elo change: ", self.eloChange)
