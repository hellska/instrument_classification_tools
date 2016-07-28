#!/usr/bin/env python

import os
import sys
import essentia
import essentia.standard as estd
    

if len(sys.argv) < 5:
    print('Usage: put some parameters please!')
    sys.exit(1)
else:
    notenum = int(sys.argv[1])
    noteoffset = int(sys.argv[2])
    fileprefix = sys.argv[3]
    scalefile = sys.argv[4]

fc = 44100
notestxt = ['do', 'reb', 're', 'mib', 'mi', 'fa', 'solb', 'sol', 'lab', 'la', 'sib', 'si']
noteusa = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

if not os.path.exists(fileprefix):
    os.mkdir(fileprefix)

loader = estd.MonoLoader(filename=scalefile)
audio = loader()
slicelen = len(audio) / notenum

start = 0
startpoints = []
endpoints = []
while start < len(audio):
    if start==0:
        startpoints.append(start)
    else:
        startpoints.append(float(start)/44100)
    endpoints.append(float(start+slicelen)/44100)
    start += slicelen

notes = estd.Slicer(startTimes=essentia.array(startpoints), endTimes=essentia.array(endpoints))(audio)

for i in range(0,len(notes)):
    note = i % 12
    pitchclass = i / 12 + noteoffset
    fileName = fileprefix+'_'+str(i)+'_'+notestxt[note]+str(pitchclass)+'.wav'
    path = os.path.join(fileprefix, fileName)
    writer = estd.MonoWriter(filename=path)
    writer(notes[i])

