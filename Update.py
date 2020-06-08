from JsonFetcher import *
import JsonComparator


class Update(JsonFetcher):
    def __init__(self):
        self.leaderboardJson = self.getLeaderboardJson()
        self.jsonComparator = JsonComparator.JsonComparator(self.leaderboardJson)

    def getLeaderboardJson(self):
        leaderboardJson = self.getJsonFile("leaderboard.json")
        return leaderboardJson

    def checkForUpdate(self):
        if self.jsonComparator.compareAndUpdateJson(self.leaderboardJson, "leaderboard.json"):
            return True
        else:
            return False

    def composeAndGetMessage(self):
        msg_leaderboard = "__***Stats based on 9 latest matches:***__" + '\n' + '\n'

        for k, v in self.getLeaderboardJson().items():
            msg_leaderboard += ('**' + str(k) + ": " + '**' + '\n')
            for m, n in v.items():
                if k == 'Headshot machine':
                    msg_leaderboard += (str(m) + ": " + str(n) + '%' + '\n')
                else:
                    msg_leaderboard += (str(m) + ": " + str(n) + '\n')
            msg_leaderboard += "\n"

        return msg_leaderboard
