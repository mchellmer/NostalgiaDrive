from os import listdir
from os.path import isfile, join

gPath = join('..', '..', 'data', 'Nintendo')
onlyfiles = [f for f in listdir(gPath) if isfile(join(gPath, f))]

outpath = join('docs', 'selections', 'all.txt')
file = open(outpath, 'w')
for name in onlyfiles:
    file.write(name + '\n')
