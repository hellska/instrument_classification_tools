"""
    Read a json containing sounds data
    Download the sound preview (hq, mp3)
    Count the mumber of occurrende
"""
import sys, os, traceback, time
import json
from os import walk
from os.path import isdir 

sys.path.append('../source/extlib/')
import myToken

rootpath = '/Volumes/Macintosh HD/hellska/thesis/'
sounddir = rootpath+'sounds'

c = myToken.freesound_client()

jf = []
for (dirpath, dirnames, filenames) in walk(rootpath):
    for f in filenames:
        if 'json' in f:
            jf.append(f)

totcount = 0
if (len(jf)>0):
    for s in range(12,len(jf)):
        idcount = 0
	print "Open file: ", str(jf[s])
        with open(rootpath+jf[s], 'r') as jsonfile:
            soundsdata = json.load(jsonfile)
            subdir = str(jf[s]).split('.', 1)
            subdir = subdir[0]
            if os.path.isdir(sounddir+'/'+subdir):
                print sounddir+'/'+subdir+" already exists"
            else:
                os.mkdir(sounddir+'/'+subdir)
                print sounddir+'/'+subdir+' Created'
            for i in soundsdata.keys():
                for k in soundsdata[i]:
                    if not os.path.exists(sounddir+'/'+subdir+'/'+str(k['id'])+'.mp3'):
			print "Check the ", subdir," sound id: ", k['id']
                        try:
                            sound = c.get_sound(k['id'])
			    try: 
                                sound.retrieve_preview(sounddir+'/'+subdir, str(k['id'])+'.mp3' )
                                idcount += 1
                                print sound.previews.preview_hq_mp3, "downloaded", idcount
                                time.sleep(1)
                            except:
 				print "Error in Get Sound for: ", str(k['id'])
				traceback.print_exc()
                        except:
                            print "Freesound Errore block!"
                            print '####'
                            traceback.print_exc()
                            print 'Downloaded '+str(idcount)+' sounds for '+subdir
                            print 'Checked '+str(totcount)+' sounds - inside loop'
                            sys.exit(3)

                    totcount += 1
                
            print 'Downloaded '+str(idcount)+' sounds for '+subdir

print 'Checked '+totcount+' sounds'
