import pymongo
import numpy
from os import path


class NdMongo():
    """interacts with mongo db"""

    def __init__(self):
        print("NdMongo Constructed")
        self.client = pymongo.MongoClient()
        self.db = self.client.nd
        self.outSelections()

    def outSelections(self):
        print("Retrieving Games")
        games = {}
        genres = self.db['games'].distinct("genre")
        publishers = self.db['games'].distinct("publisher")
        players = self.db['games'].distinct("players")
        dates = self.db['games'].distinct("date")
        for entry in self.db['games'].find({}):
            games[entry['id']] = entry

        self.outText(publishers, 'publishers')
        self.outText(genres, 'genres')
        self.outText(players, 'players')
        self.outText(dates, 'dates')

    def outText(self, name, strName):
        filename = strName + '.txt'
        outpath = path.join('docs', 'selections', filename)
        file = open(outpath, 'w')
        for item in name:
            if (item != '') and (item != '-'):
                file.write(str(item) + '\n')
