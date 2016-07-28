import json
import yaml
import sys
import os
import glob
from optparse import OptionParser

def main(yamldir, options):
    jsondir=os.path.join(os.path.dirname(yamldir),'annotation_converted')

    if not os.path.isdir(jsondir):
        os.mkdir(jsondir)

    ext_ori='yaml'
    ext_def='json'

    for (mydir, dirs, files) in os.walk(yamldir):

        if mydir != yamldir:
            files=glob.glob(os.path.join(mydir, '*.%s' % ext_ori ))
            classdir=os.path.basename(mydir)
            outdir=os.path.join(jsondir,classdir)
            if not os.path.isdir(outdir):
                os.mkdir(outdir)
    
            for file in files:
                with open(file) as yamlfile:
                    yamldata = yaml.load(yamlfile)
                    if 'freesound_extractor' in yamldata['metadata']['version']:
                        del yamldata['metadata']['version']['freesound_extractor']
                    namestr = os.path.basename(file).split(".")[:2]
                    outfilename = namestr[0]+'.'+namestr[1]+'.'+ext_def
                    txtdata = json.dumps(yamldata)
                    with open(os.path.join(outdir, outfilename), 'wb') as outfile:
                        outfile.write(txtdata)

if __name__ == "__main__":
    parser = OptionParser(usage = 
                          """
                          Pass a folder which contains the annotations
                          """)
    options, args = parser.parse_args()
    
    try:
        directory=args[0]
    except:
        parser.print_help()
        sys.exit(1)
    main(directory,options)
