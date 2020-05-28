import CommandHelper
import difflib


class Stats(CommandHelper):
    def __init__(self, jsonFileName, playername, nameList):
        self.jsonFileName = jsonFileName
        self.stats = super().getJsonFile(self.jsonFileName)
        self.playername = playername
        self.nameList = nameList

    def checkIfNameExists(self):
        self.playername = str(difflib.get_close_matches(self.playername, self.nameList)).replace("[", "").replace("]","").replace("'", "")

        for name in self.nameList:
            if name == self.playername:
                return True

    def messagePlayerStats(self):
            message = ""
            for player in self.stats:
                for k, v in player.items():
                    if k == self.playername:
                        for m, n in v.items():
                            if m == "most defuses":
                                stat = "defuses"
                                value = str(n)
                            elif m == "most plants":
                                stat = "plants"
                                value = str(n)
                            else:
                                stat = str(m)
                                value = str(n)
                            message += "**" + stat + "**" + ': ' + value + '\n'
            return message
