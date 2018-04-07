import nd.ndGui
import nd.ndMongo
import subprocess
from os import path, system


# Grab mongodb and output parameters to text
mDb = nd.ndMongo.NdMongo()

# Build Gui to make selections then output to log
x = nd.ndGui.NdGui()

# Grab selections from log and query db
logPath = path.join('docs', 'log.txt')
selection = mDb.queryGames(logPath)
print(repr(selection))
gamePath = path.join('..', 'data', 'Nintendo', selection).rstrip()

# Run script
sPath = path.join('docs', 'scripts', 'basic.sh')
system("fceux " + "\"" + gamePath + "\"")

# Close connection to database
mDb.client.close()
