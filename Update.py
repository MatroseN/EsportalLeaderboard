from CommandHelper import *


class Update(CommandHelper):
    def __init__(self, leaderboardJson):
        self.leaderboardJson = leaderboardJson

    def getLeaderboardJson(self):
        leaderboardJson = super.getJsonFile(self.leaderboardJson)
        return leaderboardJson

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
