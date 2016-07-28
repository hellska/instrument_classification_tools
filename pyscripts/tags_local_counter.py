#!/opt/local/bin/python2.7
"""
    This script counts the most common tags for the sound classes availables
    It processes the json files produced wiht the dataset_sounds.py script
    man:
        jsondir: the directory that contains the source json files
        outfile: the json file with the dictionari of counted tags
        maxtags: maximum number of tags considered for each sound
"""


import sys, os
from os import walk
import json
from collections import Counter


jsondir = '/Volumes/Macintosh HD/hellska/thesis'
outfile = jsondir+'/tags/all_tags.json'
tagsdict = {}
maxtags = 20

for (dirpath, dirnames, filenames) in walk(jsondir):
    
    for file in filenames:
        if '.json' in file:
            with open(jsondir+'/'+file, 'r') as jsonfile:
                jsondata = json.load(jsonfile)

            all_tags = []
            for i in jsondata:
                print '### Inspect Instrument:',i
                tagsdict[i] = {}
                if len(jsondata[i])>0:
                    for sound in jsondata[i]:
                        all_tags.extend(sound['tags'])

                tagcounter = Counter(all_tags)

                if len(tagcounter)>maxtags:
                    commontags = tagcounter.most_common(maxtags)
                else:
                    commontags = tagcounter.most_common(len(tagcounter)-1)

                for c in commontags:
                    tag, cnt = c
                    tagsdict[i][tag] = cnt 
    break

if bool(tagsdict):
    if not os.path.exists(outfile):
        with open(outfile, 'w') as dictout:
            json.dump(tagsdict, dictout)
            print "File", outfile, 'created!'
    else:
        print "File", outfile, 'already exists!'
