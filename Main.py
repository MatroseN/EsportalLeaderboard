import json
import Player
import MatchFetcher
import StatsFetcher


class Main:

    def __init__(self):
        self.matchFetcher = MatchFetcher.MatchFetcher()
        self.statfetcher = StatsFetcher.StatsFetcher()

    def main(self):
        players = []

        # Fake player for correct printout to discord. Could be done better. Reason: decideTop in statsFetcher initialized topPlayer is not handled as it should. But don´t wanna bother right now.
        fake = Player.Player("fake", 182145351,
                             "https://api.esportal.com/user_profile/get_latest_matches?_=1588610491353&id=182145351&page=1")
        # Super low fake stats so that the fake player cannot get on the top list
        fake.assists = -1000
        fake.hSP = -100
        fake.openingKills = -100
        fake.clutches = -100
        fake.kdr = -100
        fake.eloChange = -1000
        fake.mostKillsInOneMatch = -10
        fake.defuses = -10
        players.append(fake)

        # MatroseN
        MatroseN = Player.Player("MatroseN", 51846782,
                                 "https://api.esportal.com/user_profile/get_latest_matches?_=1588517072982&id=51846782&page=1")
        MatroseN.matchURLSTART = "https://api.esportal.com/match/get?_=1588517099477&"
        MatroseN.machURLEND = "&_u=51846782&_t=%23BWS%2F(SJ`eViX9Yc`KRm%27CE-blVsuqH%27p%24%40I%2Frmg"
        MatroseN.matches = self.matchFetcher.getPlayerMatches(MatroseN)
        self.statfetcher.updatePlayerStats(MatroseN)
        MatroseN.printStats()
        players.append(MatroseN)

        # Limé
        Lime = Player.Player("Lime", 164476701,
                             "https://api.esportal.com/user_profile/get_latest_matches?_=1588608651953&id=164476701&page=1")
        Lime.matchURLSTART = "https://api.esportal.com/match/get?_=1588608699954&"
        Lime.matchURLEND = "&_u=51846782&_t=%23BWS%2F(SJ%60eViX9Yc%60KRm%27CE-blVsuqH%27p%24%40I%2Frmg"
        Lime.matches = self.matchFetcher.getPlayerMatches(Lime)
        self.statfetcher.updatePlayerStats(Lime)
        Lime.printStats()
        players.append(Lime)

        # Microstatic
        Micro = Player.Player("Microstatic", 93317275,
                              "https://api.esportal.com/user_profile/get_latest_matches?_=1588609604851&id=93317275&page=1")
        Micro.matchURLSTART = "https://api.esportal.com/match/get?_=1588609653415&"
        Micro.matchURLEND = "&_u=51846782&_t=%23BWS%2F(SJ%60eViX9Yc%60KRm%27CE-blVsuqH%27p%24%40I%2Frmg"
        Micro.matches = self.matchFetcher.getPlayerMatches(Micro)
        self.statfetcher.updatePlayerStats(Micro)
        Micro.printStats()
        players.append(Micro)

        # DanielBKR
        BKR = Player.Player("DanielBKR", 333977649,
                            "https://api.esportal.com/user_profile/get_latest_matches?_=1588610004919&id=333977649&page=1")
        BKR.matchURLSTART = "https://api.esportal.com/match/get?_=1588610027808&"
        BKR.matchURLEND = "&_u=51846782&_t=%23BWS%2F(SJ%60eViX9Yc%60KRm%27CE-blVsuqH%27p%24%40I%2Frmg"
        BKR.matches = self.matchFetcher.getPlayerMatches(BKR)
        self.statfetcher.updatePlayerStats(BKR)
        players.append(BKR)

        # Axzero
        Axzero = Player.Player("Axzero", 80862472,
                               "https://api.esportal.com/user_profile/get_latest_matches?_=1588610288005&id=80862472&page=1")
        Axzero.matchURLSTART = "https://api.esportal.com/match/get?_=1588610330775&"
        Axzero.matchURLEND = "&_u=51846782&_t=%23BWS%2F(SJ%60eViX9Yc%60KRm%27CE-blVsuqH%27p%24%40I%2Frmg"
        Axzero.matches = self.matchFetcher.getPlayerMatches(Axzero)
        self.statfetcher.updatePlayerStats(Axzero)
        players.append(Axzero)

        # Plixz
        Plixz = Player.Player("Plixz", 182145351,
                              "https://api.esportal.com/user_profile/get_latest_matches?_=1588610491353&id=182145351&page=1")
        Plixz.matchURLSTART = "https://api.esportal.com/match/get?_=1588610549521&"
        Plixz.matchURLEND = "&_u=51846782&_t=%23BWS%2F(SJ%60eViX9Yc%60KRm%27CE-blVsuqH%27p%24%40I%2Frmg"
        Plixz.matches = self.matchFetcher.getPlayerMatches(Plixz)
        self.statfetcher.updatePlayerStats(Plixz)
        players.append(Plixz)
        Plixz.printStats()

        topList = self.statfetcher.getToplist(self.statfetcher.getAllPlayersStats(players))

        '''
        for k, v in topList.items():
            print(k, ":")
            for m, n in v.items():
                if k == 'Headshot machine':
                    print(m, ":", n, '%')
                else:
                    print(m, ":", n)
            print("")
        '''

        playerStats = self.statfetcher.getAllPlayersStats(players)

        with open('leaderboard.json', 'w', encoding='utf-8') as f:
            json.dump(topList, f, ensure_ascii=False, indent=4)

        with open('playerStats.json', 'w', encoding='utf-8') as f:
            json.dump(playerStats, f, ensure_ascii=False, indent=4)

# comment is here
