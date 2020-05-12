
class StatsFetcher:

    def getPlayerStats(self, esportalPlayer, stat):
        stats = []
        for match in esportalPlayer.matches:
            for player in match['players']:
                if player['id'] == esportalPlayer.iD:
                    stats.append(player[stat])
        return stats

    def getPlayerKDR(self, player):
        stat = 'kills'
        kills = self.getPlayerStats(player, stat)
        stat = 'deaths'
        deaths = self.getPlayerStats(player, stat)
        killCount = 0
        deathCount = 0

        for kill in kills:
            killCount += kill

        for death in deaths:
            deathCount += death
        return round((killCount / deathCount), 2)

    def getPlayerClutches(self, player):
        stat = 'clutches'
        clutchCount = 0
        clutches = self.getPlayerStats(player, stat)
        for clutch in clutches:
            clutchCount += clutch
        return clutchCount

    def getPlayerHeadshotPercentage(self, player):
        headshotCount = 0
        killCount = 0
        stat = 'headshots'
        headshots = self.getPlayerStats(player, stat)
        stat = 'kills'
        kills = self.getPlayerStats(player, stat)

        for hs in headshots:
            headshotCount += hs

        for kill in kills:
            killCount += kill
        return round((headshotCount / killCount * 100), 2)

    def getPlayerOpeningKills(self, player):
        stat = 'opening_kills'
        openingKillCount = 0
        openingKills = self.getPlayerStats(player, stat)
        for kills in openingKills:
            openingKillCount += kills
        return openingKillCount

    def getPlayerAssists(self, player):
        stat = 'assists'
        assistCount = 0
        assists = self.getPlayerStats(player, stat)
        for assist in assists:
            assistCount += assist
        return assistCount

    def getPlayerEloChange(self, player):
        stat = 'elo_change'
        eloCount = 0
        eloChanges = self.getPlayerStats(player, stat)
        for change in eloChanges:
            eloCount += change
        return eloCount

    def getPlayerHighestKillCountOneMatch(self, player):
        stat = 'kills'
        highestKillCountOneMatch = 0
        matchesKills = self.getPlayerStats(player, stat)
        for kills in matchesKills:
            if kills > highestKillCountOneMatch:
                highestKillCountOneMatch = kills
        return highestKillCountOneMatch

    def getPlayerDefuses(self, player):
        stat = 'bomb_defuses'
        defuseCount = 0
        allDefuses = self.getPlayerStats(player, stat)
        for defuseAmount in allDefuses:
            if defuseAmount is not None:
                defuseCount += defuseAmount
        return defuseCount

    def getPlayerPlants(self, player):
        stat = 'bomb_plants'
        plantCount = 0
        allPlants = self.getPlayerStats(player, stat)
        for plantAmount in allPlants:
            if plantAmount is not None:
                plantCount += plantAmount
        return plantCount

    def updatePlayerStats(self, player):
        player.kdr = self.getPlayerKDR(player)
        player.clutches = self.getPlayerClutches(player)
        player.openingKills = self.getPlayerOpeningKills(player)
        player.hSP = self.getPlayerHeadshotPercentage(player)
        player.assists = self.getPlayerAssists(player)
        player.eloChange = self.getPlayerEloChange(player)
        player.mostKillsInOneMatch = self.getPlayerHighestKillCountOneMatch(player)
        player.defuses = self.getPlayerDefuses(player)
        player.plants = self.getPlayerPlants(player)

    def decideTop(self, playerStats, stat):
        topPlayer = playerStats[0]
        topStat = 0

        for k, v in topPlayer.items():
            for m, n in v.items():
                if m == stat:
                    topStat = n

        for data in playerStats:
            for k, v in data.items():
                for m, n in v.items():
                    if m == stat and n > float(topStat):
                        topStat = n
                        topPlayer = {k: n}
        return topPlayer

    def getAllPlayersStats(self, players):
        playerStats = []
        for player in players:
            stats = {
                     'kdr': player.kdr,
                     'clutches': player.clutches,
                     'opening kills': player.openingKills,
                     'hs%': player.hSP,
                     'assists': player.assists,
                     'elo change': player.eloChange,
                     'highest kill-count': player.mostKillsInOneMatch,
                     'most defuses': player.defuses,
                     'most plants': player.plants
                     }
            player = {player.name: stats}
            playerStats.append(player)
        return playerStats

    def getToplist(self, playerStats):
        topKDR = self.decideTop(playerStats, 'kdr')
        topCLUTCHER = self.decideTop(playerStats, 'clutches')
        topOPENER = self.decideTop(playerStats, 'opening kills')
        topHSP = self.decideTop(playerStats, 'hs%')
        topASSISTER = self.decideTop(playerStats, 'assists')
        topELOCHANGE = self.decideTop(playerStats, 'elo change')
        topHighestKillCount = self.decideTop(playerStats, 'highest kill-count')
        topDefuser = self.decideTop(playerStats, 'most defuses')
        topPlanter = self.decideTop(playerStats, 'most plants')

        topList = {'Highest KDR': topKDR,
                   'Clutch king': topCLUTCHER,
                   'Most opening kills': topOPENER,
                   'Headshot machine': topHSP,
                   'The assister': topASSISTER,
                   'Elo grinder': topELOCHANGE,
                   'Most kills one match': topHighestKillCount,
                   'The defuser': topDefuser,
                   'The planter': topPlanter
                   }
        return topList

    def printTopList(self, topList):
        for item in topList:
            print("Key: {}, Value: {}".format(item, topList[item]))
