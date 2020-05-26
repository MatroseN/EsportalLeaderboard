# This class represents a player. You instanciate a player and then add the relevant stats to the player


class Player:
    def __init__(self, name, iD, matchesURL):
        self.name = name
        self.iD = iD
        self.matchesURL = matchesURL

    def printStats(self):
        print(self.name)
        print("Kdr: ", self.kdr, "Clutches: ", self.clutches, "Opening kills: ", self.openingKills, "Hs%: ",
              self.hSP, '%', "Assists: ", self.assists, "Elo change: ", self.eloChange)

    matches = []
    matchURLSTART = ""
    matchURLMID = "id="
    matchURLEND = ""

    kdr = 0
    clutches = 0
    openingKills = 0
    hSP = 0
    assists = 0
    eloChange = 0
    mostKillsInOneMatch = 0
    defuses = 0
    plants = 0
