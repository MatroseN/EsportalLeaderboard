import json
import requests


class MatchFetcher:

    def getData(self, url):
        data = json.loads(requests.get(url).text)
        return data

    def getMatchIds(self, jsonData):
        idList = []
        for match in jsonData:
            for k, v in match.items():
                if k == 'id':
                    idList.append(v)
        return idList

    def getMatches(self, matchIds, player):
        matches = []
        matchURLStart = player.matchURLSTART
        matchURLMID = player.matchURLMID
        matchURLEND = player.matchURLEND

        for iD in matchIds:
            matchID = iD
            matchURL = matchURLStart + matchURLMID + str(matchID) + matchURLEND
            match = self.getData(matchURL)
            matches.append(match)
        return matches

    def getPlayerMatches(self, player):
        matchIds = self.getData(player.matchesURL)
        matchIds = self.getMatchIds(matchIds)
        matches = self.getMatches(matchIds, player)
        return matches
