import JsonFetcher


class JsonComparator:

    def __init__(self, loadedLeaderboard):
        self.loadedLeaderboard = loadedLeaderboard
        self.jsonFetcher = JsonFetcher.JsonFetcher("leaderboard.json")

    def compareAndUpdateJson(self, loadedJsonFile, jsonFileFromDiskName):
        jsonFromDisk = self.jsonFetcher.getJsonFile(jsonFileFromDiskName)
        if self.compareJson(jsonFromDisk):
            self.loadedLeaderboard = jsonFromDisk
            return True
        else:
            return False

    def compareJson(self, jsonFromDisk):
        if self.loadedLeaderboard.items() != jsonFromDisk.items():
            return True
        else:
            return False
