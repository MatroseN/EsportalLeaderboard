import json


class CommandHelper:

    def getJsonFile(self, fileName):
        with open(fileName, encoding='utf-8') as stat_file:
            stats = json.load(stat_file)
            return stats
