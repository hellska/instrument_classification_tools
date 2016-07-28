import os
import glob
import random
import shutil
import sys
from optparse import OptionParser

def main(datasetdir, minsize):
    print "directory: "+datasetdir+" - minsize: "+str(minsize)
    
    topdir = os.path.dirname(datasetdir)
    datasetdirname = os.path.basename(datasetdir)
    balanceddir = os.path.join(topdir, datasetdirname+"_balanced")
    if os.path.isdir(balanceddir):
        print "Directory"+balanceddir+"already exists - will be removed"
        shutil.rmtree(balanceddir)
    os.mkdir(balanceddir)

    dataset = {}
    for (dirname, dirnames, filenames) in os.walk(datasetdir):
        if dirname!=datasetdir:
            classe = os.path.basename(dirname)
            out = glob.glob(os.path.join(dirname, "*.json"))
            classcount = len(out)
            dataset[classe] = {}
            dataset[classe]['size'] = classcount
            dataset[classe]['files'] = out
    for key in dataset.keys():
        currsize = int(dataset[key]['size'])
        if currsize < minsize:
            print "Exclude class "+key+" because the number of elements is "+str(currsize)+" less than the minimum "+str(minsize)
            del dataset[key]
        else:
            allclass = dataset[key]['files']
            random.shuffle(allclass)
            balclass = allclass[:minsize]
            dataset[key]['size'] = len(balclass)
            dataset[key]['files'] = balclass
            os.mkdir(os.path.join(balanceddir,key))
            for sigfile in balclass:
                shutil.copy(sigfile,os.path.join(balanceddir,key))


if __name__ == "__main__":
    parser = OptionParser(usage=
    """
    Pass the directory containing the dataset and the minimum size of each class
    """)
    options, args = parser.parse_args()
    
    try:
        directory=args[0]
    except:
        parser.print_help()
        sys.exit(1)
    if len(args)==1:
        minsize=40
    else:
        minsize=int(args[1])
    main(directory, minsize)
