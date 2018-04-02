import nd.ndGui
import nd.ndMongo
from os import path


# Grab mongodb and output parameters to text
mDb = nd.ndMongo.NdMongo()

# Build Gui to make selections then output to log
x = nd.ndGui.NdGui()

# Grab selections from log and query db
logPath = path.join('docs', 'log.txt')
selection = mDb.queryGames(logPath)

# Close connection to database
mDb.client.close()
