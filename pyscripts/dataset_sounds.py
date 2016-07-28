"""
    This script make a simple text search in the freesound database
    retrieves a list of sound dictionaries from all the retrieved pages
    save the output into a json file
    output the number of retrieved sounds and the file name
    NOTE: it can handle multiple words as input search
"""
import numpy as np
import json
import sys

sys.path.append('../source/extlib/')
import myToken

savepath = '/Volumes/Macintosh HD/hellska/thesis/'
#savepath = '/Volumes/ssdData/soundsAndSamples/Freesound_selected/'
searchstring = filename = ''

for i in range(1,len(sys.argv)):
    searchstring += sys.argv[i]+' '
    filename += sys.argv[i]+'_'

#print searchstring, filename

c = myToken.freesound_client()
fields = 'id,tags,username,license'
# fsfilter = 'tag:good-sounds'
# sounds = c.text_search(query="good-sounds",filter=fsfilter,fields=fields,page_size=100)
sounds = c.text_search(query=searchstring,fields=fields,page_size=150)

if len(sounds.results)>0:
    allresults = []
    pages = int(np.ceil(float(sounds.count) / len(sounds.results)))
    #pages = 3
    for i in range(pages):
        # cycle the result array
        if sounds.next:
            for k in sounds.results: allresults.append(k)
            sounds = sounds.next_page()
        else:
            for k in sounds.results: allresults.append(k)

    if len(allresults)>0:
        soundsdict = {}
        soundsdict[filename] = allresults

        with open(savepath+filename+'search.json', 'w') as jsonout:
            json.dump(soundsdict, jsonout)
            print 'Created File: '+filename+'search.json'
            print str(sounds.count)+' sounds retrieved'
