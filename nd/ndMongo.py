import pymongo
import numpy
from random import randint
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

    def queryGames(self, logPath):
        print("Querying Database")
        query = self.queryLog(logPath)
        # mdb columns = id name players date publisher rating genre salesNa salesEu salesJpn salesOther salesGlobal filename
        # query = {"$and": [{'players': {"$in": [1]}, 'genre': {"$in": ['Shooter']}, 'rating': {"$gt": 0}}, {'rating': {"$lt": 10}}]}
        result = self.db['games'].find(query)
        rnd = randint(0, result.count() - 1)
        return(result[rnd]['filename\r'])

    def queryLog(self, logPath):
        print("Retrieving selections from log")
        qin = {'rMin': 0, 'rMax': 10, 'players': [], 'genres': [], 'popularity': []}

        file = open(logPath, 'r')
        lines = file.readlines()
        lines.remove('\n')

        for line in lines:
            line = line.split()
            if line[0] == 'rating':
                if line[1] == 'Min':
                    qin['rMin'] = int(line[2])
                else:
                    qin['rMax'] = int(line[2])
            elif len(line) == 3:
                if line[2] != 'False':
                    qin[line[0]].append(line[1])
        qin['players'] = [int(x) for x in qin['players']]

        query = {"$and": [{'players': {"$in": qin['players']}, 'genre': {"$in": qin['genres']}, 'rating': {"$gt": qin['rMin']}}, {'rating': {"$lt": qin['rMax']}}]}

        qPop = self.queryPopularity(qin['popularity'])
        query["$and"].extend(qPop)
        return(query)

    def queryPopularity(self, popSelections):
        query = []
        pMap = {'USA': 'salesNa', 'JAPAN': 'salesJpn', 'EUROPE': 'salesEu', 'ELSEWHERE': 'salesOther'}
        if 'USA' in popSelections:
            query.append({'salesNa': {"$gt": 0}})
        if 'JAPAN' in popSelections:
            query.append({'salesJpn': {"$gt": 0}})
        if 'EUROPE' in popSelections:
            query.append({'salesEu': {"$gt": 0}})
        if 'ELSEWHERE' in popSelections:
            query.append({'salesOther': {"$gt": 0}})
        if '...NOWHERE' in popSelections:
            query = [{'salesGlobal': {"$eq": 0.0}}]

        return(query)
