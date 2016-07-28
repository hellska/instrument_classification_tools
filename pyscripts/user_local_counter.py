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
import operator


jsondir = '/Volumes/datadisk/hellska/thesis'
outfile = jsondir+'/tags/all_tags.json'
userdict = {}
maxtags = 20

print 'here!'

for (dirpath, dirnames, filenames) in walk(jsondir):

    if dirpath == jsondir:
        for file in filenames:
            if '.json' in file:
                with open(jsondir+'/'+file, 'r') as jsonfile:
                    jsondata = json.load(jsonfile)

                all_tags = []
                for i in jsondata:
                    #print '### Inspect Instrument:',i
                    userdict[i] = {}
                    if len(jsondata[i])>0:
                        for sound in jsondata[i]:
                            user = sound['username']
                            if not user in userdict[i].keys():
                                userdict[i][user] = 1
                                #print 'initialize new user: '+user
                            else:
                                count = int(userdict[i][user]) + 1
                                userdict[i][user] = count

for key in userdict:
    instr = userdict[key]
    user, val = max(instr.iteritems(), key=lambda x:x[1])
    print key, user, val

#print userdict.keys()

#                 tagcounter = Counter(all_tags)
#
#                 if len(tagcounter)>maxtags:
#                     commontags = tagcounter.most_common(maxtags)
#                 else:
#                     commontags = tagcounter.most_common(len(tagcounter)-1)
#
#                 for c in commontags:
#                     tag, cnt = c
#                     tagsdict[i][tag] = cnt
#     break
#
# if bool(tagsdict):
#     if not os.path.exists(outfile):
#         with open(outfile, 'w') as dictout:
#             json.dump(tagsdict, dictout)
#             print "File", outfile, 'created!'
#     else:
#         print "File", outfile, 'already exists!'
